#USER ADMIN CLASES

#DJANGO
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#MODELS
from users.models import Profile
from django.contrib.auth.models import User

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	#PROFILE ADMIN
	list_display = ('id','user', 'phone_number', 'website', 'picture')
	list_display_links = ('id','user')
	list_editable = ('phone_number', 'website', 'picture')

	search_fields = ('user__username','user__email','user__first_name','user__last_name', 'phone_number')
	list_filter = ('created', 'modified','user__is_active', 'user__is_staff')

	fieldsets = (
		('Profile', {
			'fields': (('user','picture'),
			
			),
		}),
		('Extra info', {
			'fields': (
				('website', 'phone_number'),
				('biography')
			)
		}),
		('Metadata', {
			'fields' : (('created', 'modified'),),
			})
		)
	readonly_fields = ('created', 'modified',)

class ProfileInLine(admin.StackedInline):
	#PROFILE IN-LINE ADMIN FOR USERS
	model = Profile
	can_delete = False
	verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
	#ADD PROFILE ADMIN TO BASE USER ADMIN
	inlines = (ProfileInLine,)
	list_display = (
		'username',
		'email',
		'first_name',
		'last_name',
		'is_active',
		'is_staff'
		)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


