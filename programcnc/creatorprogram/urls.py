from django.urls import path

from.views import *

urlpatterns = [
    path("", CreatorHome.as_view(), name='home'),
    path("rectangle", Rectangle.as_view(), name='rectangle'),
    path("diametr", Diametr.as_view(), name='diametr'),
    path("trajectory", Trajectory.as_view(), name='trajectory'),
    path("thread_milling", ThreadMilling.as_view(), name='thread_milling'),
    path("centering_hole", CenteringHole.as_view(), name='centering_hole'),
    path("drilling_hole", DrillingHole.as_view(), name='drilling_hole'),
    path("thread_tap", ThreadTap.as_view(), name='thread_tap'),
    path("turning_shaft", TurningShaft.as_view(), name="turning_shaft"),
    path("turninng_trajectory", TurninngTrajectory.as_view(), name="turninng_trajectory"),
    path("turn_drilling_hole", TurnDrillingHole.as_view(), name="turn_drilling_hole"),
    path("register", RegisterUser.as_view(), name="register"),
    path("login", LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name='logout'),
    ]
