from django.db import models
from stdimage.models import StdImageField
from ckeditor.fields import RichTextField

# Create your models here.

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificados = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

class Categoria(Base):
    category = models.CharField('Categoria', max_length=100)
    

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.category
        
class Noticia(Base):
    titulo = models.CharField('Titulo', max_length=100)
    descricao = RichTextField()
    imagem = StdImageField('Imagem', upload_to='postsimage', variations={'thumb': {'width': 350, 'height': 280, 'crop': True}})
    link = models.CharField('Link', max_length=200)
    category = models.ForeignKey('homepage.Categoria', verbose_name ='Categoria', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.titulo