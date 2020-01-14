from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from hospital.models import HospitalUser

class HospitalUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = HospitalUser
    list_display = ('full_name','email', 'phone','address','status',)
    list_filter = ('status',)
    list_per_page = 5   #For Pagination

    fieldsets = (
        (None, {'fields': ('full_name','email','phone','address','status','password1','password2')}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name','email','phone','status','password1', 'password2', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('full_name',)

admin.site.register(HospitalUser,HospitalUserAdmin)