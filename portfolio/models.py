from django.db import models


class Project(models.Model):
    """Modelo para projetos do portfólio."""

    CATEGORY_CHOICES = [
        ('design', 'Design'),
        ('web', 'Web'),
    ]

    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    thumbnail = models.ImageField('Miniatura', upload_to='projects/thumbnails/')
    category = models.CharField(
        'Categoria',
        max_length=10,
        choices=CATEGORY_CHOICES,
        default='web',
    )
    link_url = models.URLField('Link do Projeto', max_length=500)
    github_url = models.URLField(
        'GitHub',
        max_length=500,
        blank=True,
        null=True,
    )
    technologies = models.CharField(
        'Tecnologias',
        max_length=300,
        help_text='Separadas por vírgula. Ex: Django, React, Figma',
    )
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.title

    def tech_list(self):
        """Retorna a lista de tecnologias como uma lista Python."""
        return [t.strip() for t in self.technologies.split(',') if t.strip()]
