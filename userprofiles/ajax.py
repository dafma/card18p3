#encoding:utf-8


import json
from dajaxice.decorators import dajaxice_register
from .forms import UserProfileForm, EmailAuthenticationForm

from app.forms import OrderForm

@dajaxice_register
def switchForm(request):
	if request.COOKIES.has_key('form'):
		if request.COOKIES['form'] == "signup":
			form = EmailAuthenticationForm()
			html = form.as_p()

			cookie = "signin"
			title = "Log in"
		else:
			form = UserProfileForm()
			html = form.as_p()

			cookie = "signup"
			title = "Register"

	data = {'content': 	html,
			'cookie': 	cookie,
			'title': 	title}
	return json.dumps(data)