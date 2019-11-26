#USERS VIEWS

#DJANGO 
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
#MODELS
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile
#EXEPTIONS

#FORMS
from users.forms import SignupForm


class UserDetailView(LoginRequiredMixin,DetailView):
	#USER DETAIL VIEW

	template_name = 'users/detail.html'
	slug_field = 'username'
	slug_url_kwarg = 'username'
	queryset = User.objects.all()

	context_object_name = 'user'

	def get_context_data(self, **kwargs):
		#ADD USER POSTS TO CONTEXT
		context = super().get_context_data(**kwargs)
		user = self.get_object()
		context['posts'] = Post.objects.filter(user=user).order_by('-created')
		return context

class SignupView(FormView):
	#USERS SIGNUP VIEW
	template_name = 'users/signup.html'
	form_class = SignupForm
	success_url = reverse_lazy('users:login')

	def form_valid(self, form):
		#SAVE FROM DATA
		form.save()
		return super().form_valid(form)

class LoginView(auth_views.LoginView):
	#LOGIN VIEW

	template_name = 'users/login.html'


def signup(request):
	#SIGNUP VIEW
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = SignupForm()

	return render(
		request=request, template_name='users/signup.html', context={'form': form}
	)

@login_required
def logout_view(request):
	#LOGOUT A USER
	logout(request)
	return redirect ('users:login')


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})

class LogoutView(LoginRequiredMixin,auth_views.LogoutView):

	template_name = 'users/logged_out.html'