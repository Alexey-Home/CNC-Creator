from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

directions = [
    ("climb", "попутное"),
    ("up", "встречное")
]

contours = [
    ("inner", "внутрений"),
    ("outer", "внешний")
]

cncdevice = [
    ("fanuc", "fanuc"),
    ("heidenhain", "heidenhain")
]

rad_comp = [
    ("left", "левая"),
    ("right", "правая")
]
spind_direct = [
    ("clockwise", "по часовой"),
    ("counterclock", "против часовой")
]

mode_spindle = [
    ("constant_turns", "постоянные обороты"),
    ("constant_speed", "постоянная скорость резания")
]

drive = [
    ("spindle", "шпиндель"),
    ("drive_unit", "приводной интсрумент")
]

interpolicia = [
    (1, "рабочий ход"),
    (0, "быстрый ход"),
    (2, "круговой ход по часовой"),
    (3, "круговой ход против часвовой")
]

choises = [
    (0, "нет"),
    (1, "да"),
]

numbers_tool = [(i, i) for i in range(1, 41)]

colomns_prog = 30
rows_prog = 45

colomns_traj = 30
rows_traj = 5

feed = 50
coord = 0
depth = 10
rebound = 10
step = 1
start_h = 0
spindle_rot = 200
long = 100
width = 100
diametr = 10
height_transition = 15
pause_down = 0
allow = 0.2



class Basic(forms.Form):
    list_program = forms.ModelChoiceField(label="Сохраненные программы", queryset=Program.objects.none(),
                                          required=False)
    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super(Basic, self).__init__(*args, **kwargs)
        self.fields["list_program"].queryset = Program.objects.filter(id_user=user_id)

    program = forms.CharField(label="Программа", widget=forms.Textarea(attrs={'cols': colomns_prog, 'rows': rows_prog}),
                              required=False, initial="Вывод программы...", )
    cncDevice = forms.ChoiceField(label="Устройство ЧПУ", choices=cncdevice)
    name_program = forms.CharField(label="Номер программы", required=False, initial="O0001",)
    num_tool = forms.ChoiceField(label="Номер инструмента", choices=numbers_tool)



class BasicMilling(Basic):
    spindle_rotation = forms.IntegerField(label="Обороты шпинделя", required=False, initial=spindle_rot)

class RectangleForm(BasicMilling):
    direction = forms.ChoiceField(label="Направление", choices=directions)
    radius_compensation = forms.ChoiceField(label="Коррекция на радиус", choices=rad_comp)
    contour = forms.ChoiceField(label="Контур", choices=contours)
    start_height = forms.FloatField(label="Координата поверхности", required=False, initial=start_h)
    depth = forms.FloatField(label="Глубина", required=False, initial=depth)
    step = forms.FloatField(label="Шаг", required=False, initial=step)
    rebound = forms.FloatField(label="Отскок", required=False, initial=rebound)
    feed = forms.IntegerField(label="Подача", required=False, initial=feed)
    long = forms.FloatField(label='Длина прямоугольника(X)', required=False, initial=long)
    width = forms.FloatField(label='Ширина прямоугольника(Y)', required=False, initial=width)
    centr_x = forms.FloatField(label='Центр прямоугольника по X', required=False, initial=coord)
    centr_y = forms.FloatField(label='Центр прямоугольника по Y', required=False, initial=coord)


class DiametrForm(BasicMilling):
    direction = forms.ChoiceField(label="Направление", choices=directions)
    radius_compensation = forms.ChoiceField(label="Коррекция на радиус", choices=rad_comp)
    contour = forms.ChoiceField(label="Контур", choices=contours)
    start_height = forms.FloatField(label="Координата поверхности", required=False, initial=start_h)
    depth = forms.FloatField(label="Глубина", required=False, initial=depth)
    step = forms.FloatField(label="Шаг", required=False, initial=step)
    rebound = forms.FloatField(label="Отскок", required=False, initial=rebound)
    feed = forms.IntegerField(label="Подача", required=False, initial=feed)
    diametr = forms.FloatField(label="Диаметр", required=False, initial=diametr)
    centr_x = forms.FloatField(label='Центр диаметра по X', required=False, initial=coord)
    centr_y = forms.FloatField(label='Центр диаметра по Y', required=False, initial=coord)


class TrajectoryForm(BasicMilling):
    interpolicia = forms.ChoiceField(label="Лин.ход", choices=interpolicia)
    coord_x = forms.FloatField(label="Координата по X", required=False, initial=coord)
    coord_y = forms.FloatField(label="Координата по Y", required=False, initial=coord)
    coord_z = forms.FloatField(label="Координата по Z", required=False, initial=coord)
    coord_r = forms.FloatField(label="Координата по R", required=False, initial=coord)
    feed = forms.IntegerField(label="Подача", required=False, initial=feed)
    radius_compensation = forms.ChoiceField(label="Коррекция на радиус", choices=rad_comp)

    trajectory = forms.CharField(label="Траектория", required=False, widget=forms.Textarea(attrs={'cols': colomns_traj,
                                                                                                  'rows': rows_traj,
                                                                                                  'readonly': True}),)


class ThreadMillingForm(BasicMilling):
    direction = forms.ChoiceField(label="Направление", choices=directions)
    radius_compensation = forms.ChoiceField(label="Коррекция на радиус", choices=rad_comp)
    contour = forms.ChoiceField(label="Контур", choices=contours)
    start_height = forms.FloatField(label="Координата поверхности", required=False, initial=start_h)
    depth = forms.FloatField(label="Глубина", required=False, initial=depth)
    step = forms.FloatField(label="Шаг", required=False, initial=step)
    rebound = forms.FloatField(label="Отскок", required=False, initial=rebound)
    coord_x = forms.FloatField(label="Координата по X", required=False, initial=coord)
    coord_y = forms.FloatField(label="Координата по Y", required=False, initial=coord)
    trajectory = forms.CharField(label="Координаты", required=False, widget=forms.Textarea(attrs={'cols': colomns_traj,
                                                                                                  'rows': rows_traj,
                                                                                                  'readonly': True}),)
    diametr = forms.FloatField(label="Диаметр", required=False, initial=diametr)
    height_transition = forms.FloatField(label="Высота перехода", required=False, initial=height_transition)
    feed = forms.IntegerField(label="Подача", required=False, initial=feed)


class BasicDrill(Basic):
    spindle_rotation = forms.IntegerField(label="Обороты шпинделя", required=False, initial=spindle_rot)
    coord_x = forms.FloatField(label="Координата по X", required=False, initial=coord)
    coord_y = forms.FloatField(label="Координата по Y", required=False, initial=coord)
    trajectory = forms.CharField(label="Координаты", required=False, widget=forms.Textarea(attrs={'cols': colomns_traj,
                                                                                                  'rows': rows_traj,
                                                                                                  'readonly': True}),)
    rebound = forms.FloatField(label="Отскок", required=False, initial=rebound)
    height_transition = forms.FloatField(label="Высота перехода", required=False, initial=height_transition)
    start_height = forms.FloatField(label="Координата поверхности", required=False, initial=start_h)
    depth = forms.FloatField(label="Глубина", required=False, initial=depth)


class CenteringHoleForm(BasicDrill):
    feed = forms.IntegerField(label="Подача", required=False, initial=feed)
    pause_in_down = forms.FloatField(label="Пауза внизу", required=False, initial=pause_down)


class DrillingForm(BasicDrill):
    feed = forms.IntegerField(label="Подача", required=False, initial=feed)
    step = forms.FloatField(label="Шаг", required=False, initial=2)
    pause_in_down = forms.FloatField(label="Пауза внизу", required=False, initial=pause_down)


class ThreadTapForm(BasicDrill):
    step = forms.FloatField(label="Шаг", required=False, initial=step)
    step_tr = forms.FloatField(label="Шаг резьбы", required=False, initial=step)
    feed = forms.IntegerField(label="Подача", widget=forms.HiddenInput(), required=False, initial=feed)


class BasicTurn(Basic):
    rebound = forms.FloatField(label="Отскок", required=False, initial=rebound)
    z_start = forms.FloatField(label="Начальная Z", required=False, initial=coord)
    feed = forms.FloatField(label="Подача", required=False, initial=feed)
    corrector = forms.ChoiceField(label="Корректор инструмента", choices=numbers_tool)
    spindle_rotation = forms.IntegerField(label="Обороты шпинделя", required=False, initial=spindle_rot)
    direct_spindle = forms.ChoiceField(label="Направление вращения шпинделя", choices=spind_direct)
    mode_spindle = forms.ChoiceField(label="Режим шпинделя", choices=mode_spindle)


class TurnDraftForm(BasicTurn):
    coord_x = forms.FloatField(label="Диаметр детали", required=False, initial=diametr)
    coord_z = forms.FloatField(label="Глубина диаметра", required=False, initial=depth)
    trajectory = forms.CharField(label="Деталь", required=False, widget=forms.Textarea(attrs={'cols': colomns_traj,
                                                                                              'rows': rows_traj,
                                                                                              'readonly': True}),)
    diametrs_billet = forms.FloatField(label="Диаметр заготовки", required=False, initial=diametr + 5)
    trimming = forms.ChoiceField(label="Торцовка", required=False, choices=choises)
    allowence = forms.FloatField(label="Припуск на чистовой проход", required=False, initial=allow)
    finishing_pass = forms.ChoiceField(label="Чистовой проход", required=False, choices=choises)
    step = forms.FloatField(label="Шаг", required=False, initial=step)


class TrajectoryTurnForm(BasicTurn):
    interpolicia = forms.ChoiceField(label="Лин.ход", choices=interpolicia)
    coord_x = forms.FloatField(label="Координата по X", required=False, initial=coord)
    coord_z = forms.FloatField(label="Координата по Z", required=False, initial=coord)
    coord_r = forms.FloatField(label="Координата по R", required=False, initial=coord)
    feed = forms.IntegerField(label="Подача", required=False, initial=feed)
    trajectory = forms.CharField(label="Траектория", required=False, widget=forms.Textarea(attrs={'cols': colomns_traj,
                                                                                                  'rows': rows_traj,
                                                                                                  'readonly': True}),)


class TurnDrillingHoleForm(BasicTurn):
    coord_x = forms.FloatField(label="Координата по X", required=False, initial=coord)
    coord_c = forms.FloatField(label="Координата по С", required=False, initial=coord)
    coord_z = forms.FloatField(label="Глубина отверстия", required=False, initial=coord)
    trajectory = forms.CharField(label="Координаты", required=False, widget=forms.Textarea(attrs={'cols': colomns_traj,
                                                                                                  'rows': rows_traj,
                                                                                                  'readonly': True}),)
    step = forms.FloatField(label="Шаг", required=False, initial=step)
    pause_in_down = forms.FloatField(label="Пауза внизу", required=False, initial=pause_down)
    drive = forms.ChoiceField(label="Вращение", choices=drive)


class RegisterUserform(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "form-input"}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': "form-input"}))

    class Meta:
        model = User
        fields = ('username', "email", 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "form-input"}))




