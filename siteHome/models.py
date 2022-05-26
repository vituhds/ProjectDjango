from django.db import models

#   classe padrão todos  os models vão ter esta configurações.

class Base(models.Model):
    Criados = models.DateField('Criação', auto_now_add=True)
    Modificado = models.DateField('Atualização', auto_now=True)
    Ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class PaginaInicial(Base):
    titulo = models.CharField('titulo', max_length=100, blank=True)
    subTitulo = models.CharField('subTitulo', max_length=100, blank=True)
    treinamento = models.Charfield('tituloTreinamento', max_lenght=100, blank=True)

    class Meta:
        verbose_name = 'PaginaInicial'
        verbose_name_plural = 'PaginasIniciais'

        def __str__(self):
            return self.titulo
