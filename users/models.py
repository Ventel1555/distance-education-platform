from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from edu.models import Classes

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    CHOICES_ROLE = (
    ('S', 'Ученик'),
    ('T', 'Учитель'),
    ('A', 'Администратор'),
    )
    login = models.CharField(_('Логин'), max_length=18, unique=True)
    email = models.EmailField(_('Почта'), max_length=28, blank=True)
    first_name = models.CharField(_('Имя'), max_length=30, blank=True)
    last_name = models.CharField(_('Фамилия'), max_length=30, blank=True)
    patronymic = models.CharField(_('Отчество'), max_length=30, blank=True)
    class_id = models.ManyToManyField(Classes, verbose_name=_('Классы'))
    is_active = models.BooleanField(_('Активный'), default=True)
    role = models.CharField(_('Роль'), max_length=8, choices=CHOICES_ROLE)
    feedback = models.BooleanField(_('Доступ к обрат. связи'), default=False)
    # need to discusings!!!...

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name
    
    @property
    def is_staff(self):
        return self.is_superuser

    objects = UserManager()