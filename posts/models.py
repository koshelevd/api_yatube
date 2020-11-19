"""Contains models to provide an Object-relational Mapping in 'posts' app."""
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    """
    Stores a single post entry.

    Related to :model:'auth.User'.
    """
    text = models.TextField(
        verbose_name='Содержание записи',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True,
        verbose_name='Изображение',
    )

    def __str__(self):
        """Return post's info."""
        return (f'pk={self.pk} by {self.author}, {self.pub_date}, '
                f'text="{self.text[:50]}...", image="{self.image}"')

    class Meta():
        """Adds meta-information."""

        ordering = ('-pub_date',)
        verbose_name_plural = 'Записи'
        verbose_name = 'Запись'


class Comment(models.Model):
    """
    Stores a single Comment entry.

    Related to :model:'auth.User' and :model:'posts.Post'.
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
    )
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Запись',
    )
    text = models.TextField(
        verbose_name='Комментарий',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        db_index = True,
        verbose_name='Дата добавления',
    )

    def __str__(self):
        """Return comments's info."""
        return (f'Comment by {self.author}, {self.created}, '
                f'text="{self.text[:50]}..."')

    class Meta():
        """Adds meta-information."""

        ordering = ('-created',)
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
