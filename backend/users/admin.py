from django.contrib import admin

from core.admin import BaseAdminModel
from users.models import User


@admin.register(User)
class UserAdmin(BaseAdminModel):

    list_display = (
        'id',
        'email',
    )

    readonly_fields = (
        'date_joined',
        'last_login',
        'confirmation_code',
    )

    search_fields = ('first_name', 'last_name', 'email')
    search_help_text = 'Fiend by first / last names, email'

    fieldsets = (
        (None,
         {
             'classes': ['extrapretty'],
             'fields': (
                 'is_staff',
                 'is_superuser',
             )
         }),
        ('General',
         {
             'classes': ['extrapretty'],
             'fields':
                 (
                     (
                         'email',
                         'confirmation_code',
                     ),
                     (
                         'first_name',
                         'last_name',
                     ),
                 ),
         }),
        ('Permissions',
         {
             'classes': ['collapse'],
             'fields': (
                 'groups',
                 'user_permissions',
             ),
         }),
        ('Dates',
         {
             'fields': (
                 'date_joined',
                 'last_login',
             )
         }),
    )

    add_fieldsets = (
        (None,
         {
             'classes': ['extrapretty'],
             'fields': (
                 'is_staff',
                 'is_superuser',
             )}),
        ('General',
         {
             'classes': ['extrapretty'],
             'fields':
                 (
                     (
                         'email',
                     ),
                     (
                         'first_name',
                         'last_name',
                     ),
                 ),
         }),
        ('Permissions',
         {
             'classes': ['collapse'],
             'fields': (
                 'groups',
                 'user_permissions',
             ),
         }),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return self.fieldsets
