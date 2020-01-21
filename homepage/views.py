from django.views.generic import TemplateView
from .models import Categoria, Noticia

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.order_by('?').all()
        context['noticias'] = Noticia.objects.all().order_by('?').all()
        return context
        

class TestetView(TemplateView):
    template_name = 'teste.html'
    
    