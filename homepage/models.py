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

class Membros(Base):
    CARGOS_CHOICES = (
        ('Presidente','Presidente'),
        ('Vice Presidente','Vice Presidente'),
        ('Secretário Geral','Secretário Geral'),
        ('Tesoureiro','Tesoureiro'),
        ('Diretor de comunicação','Diretor de comunicação'),
        ('Membro','Membro')
    )
    nome = models.CharField('Nome',max_length=100)
    image = StdImageField('Imagem', upload_to='postimage', variations={'thumb': {'width': 350, 'height': 280, 'crop': True}})
    descricao = models.TextField('Descrição', default='SOME STRING')
    cargo = models.CharField('Cargo', max_length=25, choices=CARGOS_CHOICES)
    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'

    def __str__(self):
        return self.nome
class Labs(Base):
    
    nome = models.CharField('Nome',max_length=100)
    image = StdImageField('Imagem', upload_to='postimage', variations={'thumb': {'width': 263, 'height': 130, 'crop': True}})
    
    class Meta:
        verbose_name = 'Laboratório'
        verbose_name_plural = 'Laboratórios'

    def __str__(self):
        return self.nome