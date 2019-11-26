
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
# Create your views here.
#FORMS
from posts.forms import PostForm
#MODEL
from posts.models import Post


#POSTS VIEWS
class PostsFeedView(LoginRequiredMixin, ListView):
	#RETURN AL PUBLISHED POSTS
	template_name = 'posts/feed.html'
	model = Post
	ordering = ('-created')
	paginate_by = 10
	context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
	#RETURN POST DETAIL
	template_name= 'posts/detail.html'
	queryset = Post.objects.all()
	context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
	#CREATE NEW POST
	template_name = 'posts/new.html'
	form_class = PostForm
	success_url = reverse_lazy('posts:feed')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user'] = self.request.user
		context['profile'] = self.request.user.profile
		return context

