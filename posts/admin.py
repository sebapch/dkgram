from django.contrib import admin
from posts.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	#POST ADMIN MODEL
	list_display = ('id', 'user', 'photo')
	list_display_links = ('id', 'user')
	search_fields = ('title', 'user__username', 'user__email')
	list_filter = ('created', 'modified')

