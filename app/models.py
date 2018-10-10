
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Channel(models.Model):
    """Model definition for Message."""

    name = models.CharField('Nome', max_length=255)

    users = models.ManyToManyField(User, related_name='channels')

    private = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Message."""

        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        """Unicode representation of Message."""
        return '{}'.format(self.name)


class Message(models.Model):
    """Model definition for Message."""

    writter = models.ForeignKey(User, on_delete=models.CASCADE)

    send_at = models.DateField('enviado em', auto_now=False, auto_now_add=True)
    updated_at = models.DateField('atualizado em', auto_now=False, auto_now_add=False)

    read = models.BooleanField(default=False)

    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    message = models.TextField('mensagem')

    class Meta:
        """Meta definition for Message."""

        ordering = ['send_at']

        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        """Unicode representation of Message."""
        return '{}'.format(message)
