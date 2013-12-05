import datetime
import json

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import edit, base

from gigs.models import Gig, SignUp

class IndexView(base.TemplateView):
	template_name = 'home/index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['upcoming_gigs'] = Gig.objects.filter(start_datetime__gte=datetime.datetime.now())
		return context

class ContactsView(base.TemplateView):
	template_name = 'home/contacts.html'

class LoginView(base.TemplateView):
	template_name = 'home/login.html'

	def post(self, request, *args, **kwargs):
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		try:
			has_user = User.objects.get(username=username)
		except:
			return HttpResponse( json.dumps({"error": "User {0} was not found!".format(username)}) )

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse_lazy('home:index'))
			else:
				return HttpResponse(  json.dumps({"error": "This user account is disabled"}) )
		else:
			return HttpResponse( json.dumps({"error": "Your password was incorrect! Try Again."}) )

class LogoutView(base.RedirectView):
	url = reverse_lazy('home:index')

	def get(self, request, *args, **kwargs):
		logout(request)
		return HttpResponseRedirect(reverse_lazy('home:index'))