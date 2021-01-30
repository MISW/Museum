from django.shortcuts import redirect
from django.views import generic

from backend.developments.models import Development

class DevelopmentPendingHomeView(generic.TemplateView):
    template_name = 'manage/development/pending/index.html'

    def get(self, *args, **kwargs):
        context = {
            'developments': Development.objects.filter(status=0)
        }

        return self.render_to_response(context)


class DevelopmentPublicHomeView(generic.TemplateView):
    template_name = 'manage/development/public/index.html'

    def get(self, *args, **kwargs):
        context = {
            'developments': Development.objects.filter(status=1)
        }

        return self.render_to_response(context)


class DevelopmentClosedHomeView(generic.TemplateView):
    template_name = 'manage/development/closed/index.html'

    def get(self, *args, **kwargs):
        context = {
            'developments': Development.objects.filter(status=2)
        }

        return self.render_to_response(context)

# class ManageHomeView(generic.TemplateView):
#     template_name = 'admin-page.html'
#
#     def get(self, request, **kwargs):
#         if request.user.isadmin == False:
#             return redirect('/')
#         context = {
#             'apps': GameInf.objects.filter(status=0)
#         }
#         return self.render_to_response(context)
#
#
# class ManageGameDetailView(generic.TemplateView):
#     template_name = 'admin-game-detail.html'
#
#     def get(self, request, **kwargs):
#         if request.user.isadmin == False:
#             return redirect('/')
#         context = {
#             'development': GameInf.objects.filter(id=self.kwargs['pk'])[0]
#         }
#         return self.render_to_response(context)
#
#
# class ManageNonPublicGameDetailView(generic.TemplateView):
#     template_name = 'admin-nopublic-game-detail.html'
#
#     def get(self, request, **kwargs):
#         if request.user.isadmin == False:
#             return redirect('/')
#         context = {
#             'development': GameInf.objects.filter(id=self.kwargs['pk'])[0]
#         }
#         return self.render_to_response(context)
#
#
# class ManagePublicGameDetailView(generic.TemplateView):
#     template_name = 'admin-public-game-detail.html'
#
#     def get(self, request, **kwargs):
#         if request.user.isadmin == False:
#             return redirect('/')
#         context = {
#             'development': GameInf.objects.filter(id=self.kwargs['pk'])[0]
#         }
#         return self.render_to_response(context)
#
#
# class ManageNonPublicView(generic.TemplateView):
#     template_name = 'admin-page-nopublic.html'
#
#     def get(self, request, **kwargs):
#         if request.user.isadmin == False:
#             return redirect('/')
#         context = {
#             'apps': GameInf.objects.filter(status=2)
#         }
#         return self.render_to_response(context)
#
#
# class ManagePublicView(generic.TemplateView):
#     template_name = 'admin-page-public.html'
#
#     def get(self, request, **kwargs):
#         if request.user.isadmin == False:
#             return redirect('/')
#         context = {
#             'apps': GameInf.objects.filter(status=1)
#         }
#         return self.render_to_response(context)
#
#
# def DeleteApplication(request, id):
#     if request.user.isadmin == False:
#         return redirect('/')
#     GameInf.objects.get(id=id).delete()
#     return redirect('/manage')
#
#
# def PublishApplication(request, id):
#     if request.user.isadmin == False:
#         return redirect('/')
#     GameInf.objects.filter(id=id).update(status=1)
#     return redirect('/manage')
#
#
# def HideApplication(request, id):
#     if request.user.isadmin == False:
#         return redirect('/')
#     GameInf.objects.filter(id=id).update(status=2)
#     return redirect('/manage')
