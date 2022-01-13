from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from x_personalized_settings import group_details
from register.models import Dog, Fleet, Equipment, Member
from register.forms import MemberForm, DogForm, FleetForm


class HomeView(TemplateView):
    template_name = "register/index.html"


class Error404(TemplateView):
    template_name = "404.html"


class TeamListView(ListView):
    paginate_by = 5
    model = Member
    template_name = "register/team.html"
    context_object_name = "member_list"
    extra_context = {"group_name_short": group_details.get_group_name_short()}


class DogListView(ListView):
    paginate_by = 5
    model = Dog
    template_name = "register/dogs.html"
    context_object_name = "dog_list"
    extra_context = {"group_name_short": group_details.get_group_name_short()}


class FleetListView(ListView):
    paginate_by = 5
    model = Fleet
    template_name = "register/fleet.html"
    context_object_name = "fleet_list"
    extra_context = {"group_name_short": group_details.get_group_name_short()}


class EquipmentListView(ListView):
    paginate_by = 5
    model = Equipment
    template_name = "register/equipment.html"
    context_object_name = "equipment_list"
    extra_context = {"group_name_short": group_details.get_group_name_short()}


class MemberCreateView(LoginRequiredMixin, CreateView):
    model = Member
    form_class = MemberForm
    template_name = "register/member-form.html"
    success_url = reverse_lazy("register:zespol")
    extra_context = {"group_name_short": group_details.get_group_name_short()}


class DogCreateView(LoginRequiredMixin, CreateView):
    model = Dog
    form_class = DogForm
    template_name = "register/dog-form.html"
    success_url = reverse_lazy("register:psy")
    extra_context = {"group_name_short": group_details.get_group_name_short()}


class FleetCreateView(LoginRequiredMixin, CreateView):
    model = Fleet
    form_class = FleetForm
    template_name = "register/fleet-form.html"
    success_url = reverse_lazy("register:flota")
    extra_context = {"group_name_short": group_details.get_group_name_short()}
