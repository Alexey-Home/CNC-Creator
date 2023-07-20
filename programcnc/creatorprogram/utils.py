import json

from django.shortcuts import render, redirect

from .models import *

menu = [{"title": "На главную", "url_name": "home"},
        {"title": "Регистрация", "url_name": "registration"},
        {"title": "Войти","url_name": "login"}
]



operation_mill = [{"title": "Фрезерование прямоугольника", "url_name": "rectangle"},
                  {"title": "Фрезерование диаметра", "url_name": "diametr"},
                  {"title": "Фрезерование траектории", "url_name": "trajectory"},
                  {"title": "Резьбофрезерование(по спирали)", "url_name": "thread_milling"},
                  {"title": "Центровка отверстий", "url_name": "centering_hole"},
                  {"title": "Сверление отверстий", "url_name": "drilling_hole"},
                  {"title": "Нарезание резьбы метчиком", "url_name": "thread_tap"},
]

operation_turn = [
    {"title": "Черновая проточка вала и отверстия", "url_name": "turning_shaft"},
    {"title": "Траектории", "url_name": "turninng_trajectory"},
    {"title": "Сверление отверстий", "url_name": "turn_drilling_hole"},
]

out_field_traj = ["Лин.ход", "Координата по X", "Координата по Y", "Координата по Z", "Координата по R", "Подача"]

out_field_threadmill = ["Координата по X", "Координата по Y", "Координата по Z", "Глубина диаметра", "Диаметр детали",
                        "Глубина отверстия", "Координата по С"]

not_filed_out = ["Программа", "Траектория", "Координаты", "Деталь", "Сохраненные программы"]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        operation_milling = operation_mill.copy()
        operation_turning = operation_turn.copy()
        operation_all = operation_milling + operation_turning
        output_field = out_field_traj.copy()
        not_filed_output = not_filed_out.copy()
        context["operation_mill"] = operation_milling
        context["operation_turn"] = operation_turning
        context["operation_all"] = operation_all
        context["output_field"] = output_field
        context["not_filed_output"] = not_filed_output
        context["out_field_threadmill"] = out_field_threadmill.copy()
        context["menu"] = menu.copy()
        return context

    def get_post(self, modelform, classview, req, page):
        message_form = modelform(req.POST or None, user_id=req.user.pk)
        program = "Вывод программы..."
        coordinate = ""
        if "load_prog" in req.POST:
            if req.POST['list_program']:
                print(req.POST["list_program"])
                text = Program.objects.values('program').filter(id=req.POST["list_program"])
                program = text[0]['program']
            else:
                program = "Выберите программу..."
            if "trajectory" in req.POST:
                coordinate = req.POST["trajectory"]
        if "del_prog" in req.POST:
            if req.POST['list_program']:
                print(req.POST["list_program"])
                Program.objects.filter(id=req.POST["list_program"]).delete()
            else:
                program = "Выберите программу..."
            if "trajectory" in req.POST:
                coordinate = req.POST["trajectory"]
        if "clean" in req.POST:
            if "trajectory" in req.POST:
                coordinate = req.POST["trajectory"]
            program = "Вывод программы..."
        if "add" in req.POST:
            line = get_line(req.POST)
            coordinate = req.POST["trajectory"] + line
            program = req.POST["program"]
        if "clean_tr" in req.POST:
            coordinate = ""
            program = req.POST["program"]
        if 'save' in req.POST:
            if "trajectory" in req.POST:
                coordinate = req.POST["trajectory"]
            if req.user.pk:
                progrm = Program(name=req.POST["name_program"], program=req.POST["program"], id_user=req.user.pk)
                progrm.save()
                program = req.POST["program"]
            else:
                program = "Сохранять программу разрешено только авторизованным пользователям..."
        if 'generate' in req.POST:
            data = transform(req.POST)
            if "trajectory" in data and data["trajectory"] == 0:
                data["trajectory"] = get_line(req.POST)
            class_view = classview(data)
            program = class_view.create()
            if "trajectory" in data:
                coordinate = req.POST["trajectory"]
        if message_form.is_valid():
            message_form.cleaned_data["program"] = program
            if "trajectory" in message_form.cleaned_data:
                message_form.cleaned_data["trajectory"] = coordinate
            clean_form = json.dumps(message_form.cleaned_data, default=str)
            req.session['save_form'] = clean_form
        else:
            if 'save_form' in req.session:
                del req.session['save_form']
        return redirect(page)

    def get_context(self, modelform, req, data):
        if 'save_form' in req.session:
            saved_form = json.loads(req.session.get('save_form', ''))
            form = modelform(initial=saved_form, user_id=req.user.pk)
        else:
            form = modelform(user_id=req.user.pk)
        context = self.get_user_context(title=data["title_context"])
        pictures = Pictures.objects.filter(title=data["title_pictures"])
        context["pictures"] = pictures
        context["form"] = form
        return context


def transform(data):
    temp = {}
    for key, value in data.items():
        if value:
            temp[key] = value
        else:
            temp[key] = 0
    return temp


def get_line(post):
    if "interpolicia" in post:
        if "coord_y" in post:
            line = f"G{post['interpolicia']}" \
                   f"X{post['coord_x']}" \
                   f"Y{post['coord_y']}" \
                   f"Z{post['coord_z']}" \
                   f"F{post['feed']}" \
                   f"R{post['coord_r']}\n"
        else:
            line = f"G{post['interpolicia']}" \
                   f"X{post['coord_x']}" \
                   f"Z{post['coord_z']}" \
                   f"F{post['feed']}" \
                   f"R{post['coord_r']}\n"
    elif "coord_c" in post:
        line = f"X{post['coord_x']}" \
               f"Z{post['coord_z']}" \
               f"C{post['coord_c']}"
    elif "coord_z" in post:
        line = f"X{post['coord_x']}" \
               f"Z{post['coord_z']}\n"
    else:
        line = f"X{post['coord_x']}" \
               f"Y{post['coord_y']}\n"
    return line

