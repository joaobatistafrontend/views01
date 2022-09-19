from django.views.generic import TemplateView
from django.shortcuts import redirect

'''
    para redirecionar use:
    from django.shortcuts import redirect
'''

class ViewNBloqueado(TemplateView):
    template_name = 'dispatch/ok.html'


    def get(self, request, *args,**kwargs):
        print(request.GET)
        if request.GET.get == {'action','1'}:
            return redirect('bloqueado')
        else:
            return redirect('index')
            


class ViewBloqueado(TemplateView):
    template_name = 'dispatch/bloqueado.html'
    