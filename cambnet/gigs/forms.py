from django import forms

from .models import Gig

class GigForm(forms.ModelForm):
	
	class Meta:
		model = Gig
		fields = ['name', 'description', 'uniform', 'start_datetime', 'end_datetime', 'extra_credit', 'cars']

	def __init__(self, *args, **kwargs):
		super(GigForm, self).__init__(*args, **kwargs)
		split_widget = forms.SplitDateTimeWidget()
		split_widget.widgets[0].attrs = {'class':'datetime date', 'size':'10', 'maxlength':'10', 'placeholder':'Date'}
		split_widget.widgets[1].attrs = {'class':'datetime time', 'size':'5', 'maxlength':'5', 'placeholder':'Time'}
		self.fields["start_datetime"].widget = split_widget
		self.fields["end_datetime"].widget = split_widget