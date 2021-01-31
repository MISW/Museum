from django.views import generic

from ..views import OnlyAdminMixin


class ManageHomeView(OnlyAdminMixin, generic.TemplateView):
    template_name = 'manage/home/index.html'
