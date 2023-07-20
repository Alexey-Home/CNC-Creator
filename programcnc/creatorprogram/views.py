import json

from urllib import request
from django.views.generic import ListView, FormView, CreateView
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .utils import *
from .forms import *
from .models import *
from CNCprogramСreator.milling import rectangle as rec
from CNCprogramСreator.milling import diametr as diam
from CNCprogramСreator.milling import trajectory as traj
from CNCprogramСreator.milling import thread_milling as tm
from CNCprogramСreator.drilling import centering_hole as ch
from CNCprogramСreator.drilling import drilling_hole as dh
from CNCprogramСreator.drilling import thread_tap as tt
from CNCprogramСreator.turning import turning_shaft as ts
from CNCprogramСreator.turning import turninng_trajectory as ttj
from CNCprogramСreator.turning import turn_drilling_hole as tdh


class CreatorHome(DataMixin, ListView):
    template_name = "creatorprogram/index.html"
    context_object_name = "operation"
    queryset = "operation"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


class Rectangle(DataMixin, FormView):
    form_class = RectangleForm
    template_name = "creatorprogram/figure.html"

    def post(self, req, *args, **kwargs):
        return self.get_post(RectangleForm, rec.Rectangle, req, "rectangle")

    def get(self, req, *args, **kwargs):
        data = {
            "title_context": "Фрезерование прямоугольника",
            "title_pictures": "rectangle",
            "page": 'creatorprogram/figure.html',
        }
        return render(req, data["page"], self.get_context(RectangleForm, req, data))


class Diametr(DataMixin, FormView):
    form_class = DiametrForm
    template_name = "creatorprogram/figure.html"

    def post(self, req, *args, **kwargs):
        return self.get_post(DiametrForm, diam.Diametr, req, "diametr")

    def get(self, req, *args, **kwargs):
        data = {
            "title_context": "Фрезерование диаметра",
            "title_pictures": "diametr",
            "page": 'creatorprogram/figure.html',
        }
        return render(req, data["page"], self.get_context(DiametrForm, req, data))


class Trajectory(DataMixin, FormView):
    form_class = TrajectoryForm
    template_name = "creatorprogram/lineshole.html"

    def post(self, req, *args, **kwargs):
        return self.get_post(TrajectoryForm, traj.Trajectory, req, "trajectory")

    def get(self, req, *args, **kwargs):
        data = {
            "title_context": "Фрезерование траекторий",
            "title_pictures": "trajectory",
            "page": 'creatorprogram/lineshole.html',
        }
        return render(req, data["page"], self.get_context(TrajectoryForm, req, data))


class ThreadMilling(DataMixin, FormView):
    form_class = ThreadMillingForm
    template_name = "creatorprogram/drilling.html"

    def post(self, req, *args, **kwargs):
        return self.get_post(ThreadMillingForm, tm.ThreadMill, req, "thread_milling")

    def get(self, req, *args, **kwargs):
        data = {
            "title_context": "Резьбофрезерование(по спирали)",
            "title_pictures": "threadmill",
            "page": 'creatorprogram/drilling.html',
        }
        return render(req, data["page"], self.get_context(ThreadMillingForm, req, data))


class CenteringHole(DataMixin, FormView):
    form_class = CenteringHoleForm
    template_name = "creatorprogram/drilling.html"

    def post(self, req, *args, **kwargs):
        return self.get_post(CenteringHoleForm, ch.Centering, req, "centering_hole")

    def get(self, req, *args, **kwargs):
        data = {
            "title_context": "Центровка отверстий",
            "title_pictures": "centering",
            "page": 'creatorprogram/drilling.html',
        }
        return render(req, data["page"], self.get_context(CenteringHoleForm, req, data))


class DrillingHole(DataMixin, FormView):
    form_class = DrillingForm
    template_name = "creatorprogram/drilling.html"

    def post(self, req, *args, **kwargs):
        return self.get_post(DrillingForm, dh.Drilling, req, "drilling_hole")

    def get(self, req, *args, **kwargs):
        data = {
            "title_context": "Сверление отверстий",
            "title_pictures": "drilling",
            "page": 'creatorprogram/drilling.html',
        }
        return render(req, data["page"], self.get_context(DrillingForm, req, data))


class ThreadTap(DataMixin, FormView):
    form_class = ThreadTapForm
    template_name = "creatorprogram/drilling.html"

    def post(self, req, *args, **kwargs):
        return self.get_post(ThreadTapForm, tt.Thread, req, "thread_tap")

    def get(self, req, *args, **kwargs):
        data = {
            "title_context": "Нарезание резьбы метчиком",
            "title_pictures": "drilling",
            "page": 'creatorprogram/drilling.html',
        }
        return render(req, data["page"], self.get_context(ThreadTapForm, req, data))


class TurningShaft(DataMixin, FormView):
    form_class = TurnDraftForm
    template_name = "creatorprogram/turningshaft.html"

    def post(self, req, *args, **kwargs):
        return self.get_post(TurnDraftForm, ts.TurnDraft, req, "turning_shaft")

    def get(self, req, *args, **kwargs):
        data = {
            "title_context": "Черновая проточка вала и отверстия",
            "title_pictures": "turnshaft",
            "page": 'creatorprogram/turningshaft.html',
        }
        return render(req, data["page"], self.get_context(TurnDraftForm, req, data))


class TurninngTrajectory(DataMixin, FormView):
    form_class = TrajectoryTurnForm
    template_name = "creatorprogram/lineshole.html"

    def post(self, req, *args, **kwargs):
        return self.get_post(TrajectoryTurnForm, ttj.TurnTraject, req, "turninng_trajectory")

    def get(self, req, *args, **kwargs):
        data = {
            "title_context": "Точение траекторий",
            "title_pictures": "turntrajectory",
            "page": 'creatorprogram/lineshole.html',
        }
        return render(req, data["page"], self.get_context(TrajectoryTurnForm, req, data))


class TurnDrillingHole(DataMixin, FormView):
    form_class = TurnDrillingHoleForm
    template_name = "creatorprogram/drilling.html"

    def post(self, req, *args, **kwargs):
        return self.get_post(TurnDrillingHoleForm, tdh.TurnDrilling, req, "turn_drilling_hole")

    def get(self, req, *args, **kwargs):
        data = {
            "title_context": "Сверление отверстий",
            "title_pictures": "turndrilling",
            "page": 'creatorprogram/drilling.html',
        }
        return render(req, data["page"], self.get_context(TurnDrillingHoleForm, req, data))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserform
    template_name = 'creatorprogram/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'creatorprogram/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def transform(data):
    temp = {}
    for key, value in data.items():
        if value:
            temp[key] = value
        else:
            temp[key] = 0
    return temp





