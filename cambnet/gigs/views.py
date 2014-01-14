from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.views.generic import edit

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .forms import GigForm
from .models import Gig, SignUp

class IndexView(generic.ListView):
	template_name = 'gigs/index.html'
	context_object_name = 'gigs_list' 

	def get_queryset(self):
		return Gig.objects.order_by('-start_datetime')
		

class DetailView(generic.DetailView):
	model = Gig
	template_name = 'gigs/detail.html'


class ResultsView(generic.DetailView):
	model = Gig
	template_name = 'gigs/results.html'


class GigCreate(LoginRequiredMixin, PermissionRequiredMixin, edit.CreateView):
	permission_required = "gigs.add_gig"
	raise_exception = True

	form_class = GigForm
	#model = Gig
	#fields = ['name', 'description', 'uniform', 'start_datetime', 'end_datetime', 'extra_credit', 'cars']
	template_name = 'gigs/gig_form.html'
	success_url = reverse_lazy('gigs:index')



class GigUpdate(LoginRequiredMixin, PermissionRequiredMixin, edit.UpdateView):
	permission_required = "gigs.change_gig"
	raise_exception = True
	model = Gig
	fields = ['name', 'description', 'uniform', 'start_datetime', 'end_datetime', 'extra_credit', 'cars']
	template_name_suffix = "_update_form"

	def get_success_url(self):
		return reverse_lazy('gigs:detail', kwargs={'pk': self.get_object().id })


class GigDelete(LoginRequiredMixin, PermissionRequiredMixin, edit.DeleteView):
	permission_required = "gigs.delete_gig"
	raise_exception = True
	model = Gig
	success_url = reverse_lazy('gigs:index')


class GigSignUp(LoginRequiredMixin, PermissionRequiredMixin, generic.RedirectView):
	permission_required = "gigs.add_signup"
	raise_exception = True
	url = reverse_lazy('gigs:index')

	def get(self, request, *args, **kwargs):
		sign_up = SignUp.objects.create(gig=Gig.objects.get(id=kwargs['pk']), user=request.user)
		return HttpResponse("success!")