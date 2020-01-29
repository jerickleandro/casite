from django.views.generic import TemplateView
from .models import Categoria, Noticia, Membros, Labs

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.order_by('?').all()
        context['noticias'] = Noticia.objects.all().order_by('?').all()
        context['membros'] = Membros.objects.all().order_by('?').all()
        context['labs'] = Labs.objects.all().order_by('?').all()
        return context

    def trata_string():
        cat = Categoria.category
        return cat   

class TestetView(TemplateView):
    template_name = 'teste.html'
    
    