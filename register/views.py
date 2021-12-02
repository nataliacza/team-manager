from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "register/index.html"

class Error404(TemplateView):
    template_name = "404.html"
