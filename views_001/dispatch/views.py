from django.views.generic import TemplateView
from django.shortcuts import redirect

'''
    para redirecionar use:
    from django.shortcuts import redirect
'''

class ViewNaoBloqueado(TemplateView):
    template_name = 'dispatch/ok.html'

    def dispatch(self, request, *args, **kwargs):
        if request.GET.get('acesso') == '1':
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect ('bloqueado')

class ViewBloqueado(TemplateView):
    template_name = 'dispatch/bloqueado.html'
    def dispatch(self, request, *args, **kwargs):
        if request.GET.get('acesso') == '0':
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('index')