from django.views import generic
from django.db.models import Q
from backend.developments.models import Development
from backend.users.models import User
from django.http import HttpResponse
import json


class HomeView(generic.TemplateView):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {
                'developments': Development.objects.order_by('title').filter(status=1, developer__is_superuser=False)
            }
        else:
            context = {
                'developments': Development.objects.order_by('title').filter(status=1, developer__is_superuser=False,
                                                                             is_private=False)
            }

        return self.render_to_response(context)


class SearchView(generic.TemplateView):
    template_name = 'home/index.html'

    def post(self, request, *args, **kwargs):
        associations = {"プログラミング": 0, "CG": 1, "MIDI": 2}
        keyword = request.POST['search']
        list = ''
        if keyword:
            developers = User.objects.filter(first_name__contains=keyword)
            condition = Q(title__contains=keyword, status=1, developer__is_superuser=False)
            for dev in developers:
                condition = condition | Q(developer=dev) | Q(co_developers=dev)
            if keyword in associations.keys():
                condition = condition | Q(associations=associations[keyword])
            if not (request.user.is_authenticated):
                condition = condition & Q(is_private=False)
            list = Development.objects.order_by('title').filter(condition).distinct()
        context = {
            'developments': list
        }
        return self.render_to_response(context)


def keywords_api(request):
    userlist = User.objects.filter(is_superuser=False).values_list('first_name', flat=True)
    devcondition = Q(status=1, developer__is_superuser=False)
    if request.GET["userstatus"] != "true":
        devcondition = devcondition & Q(is_private=False)
    devlist = Development.objects.filter(devcondition).values_list('title', flat=True)
    keywords = ["プログラミング", "CG", "MIDI"] + list(userlist) + list(devlist)
    params = {"keywords": keywords}
    json_str = json.dumps(params, ensure_ascii=False, indent=2)
    return HttpResponse(json_str, content_type="application/json")
