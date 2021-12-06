import personalized_group_details
from django.views.generic import ListView, TemplateView
from register.models import Dog, Equipment, Member


class HomeView(TemplateView):
    template_name = "register/index.html"


class Error404(TemplateView):
    template_name = "404.html"


class TeamListView(ListView):
    paginate_by = 5
    model = Member
    template_name = "register/team.html"
    context_object_name = "member_list"
    extra_context = {"group_name_short": personalized_group_details.get_group_name_short()}


class DogListView(ListView):
    paginate_by = 5
    model = Dog
    template_name = "register/dogs.html"
    context_object_name = "dogs_list"
    extra_context = {"group_name_short": personalized_group_details.get_group_name_short()}


class EquipmentListView(ListView):
    paginate_by = 5
    model = Equipment
    template_name = "register/equipment.html"
    context_object_name = "equipment_list"
    extra_context = {"group_name_short": personalized_group_details.get_group_name_short()}
