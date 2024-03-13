from django.contrib import admin

from users.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'email',
                    'first_name',
                    'last_name',
                    'phone',
                    'avatar',
                    'city',
                    'role',
                    'is_active',
                    'id_tg',
                    )
    list_filter = ('email', 'first_name', 'last_name',)
    search_fields = ('email', 'first_name', 'last_name',)
