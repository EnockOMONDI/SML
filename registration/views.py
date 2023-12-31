import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from registration.form import RegisterForm
# from .tokens import account_activation_token





def register_modal(request):
    form = RegisterForm()
    return render(request, 'register/modal.html',{
        'form': form,
    })

def redirectedregister(request):
    form = RegisterForm()
    return render(request, 'register/register.html',{
        'local_css_urls' : settings.SB_ADMIN_2020UI_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2020UI_JS_LIBRARY_URLS,
        'form': form
    })




@csrf_exempt  # Only if you want to allow CSRF for this view
def register(request):
    response_data = {}
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
        form = RegisterForm(request.POST)
        
        # Validate the form: the captcha field will automatically check the input
        if form.is_valid():
            response_data = create_user(form)  # Create the user (replace with actual logic)
            response_data['status'] = 'success'
        else:
            response_data = {'status': 'failed', 'message': json.dumps(form.errors)}
    else:
        response_data = {'status': 'failure', 'message': 'Not acceptable request made.'}

    return JsonResponse(response_data)



def create_user(form):
    # Create the user in our database
    email = form['email'].value().lower()
    try:
        user = User.objects.create_user(
            email,  # Username
            email,  # Email
            form['password'].value(),
        )
        user.first_name = form['first_name'].value()
        user.last_name = form['last_name'].value()
        # user.is_active = False  # Need email verification to change status.
        user.save()
    except Exception as e:
        return {
            'status' : 'failure',
            'message' : 'An unknown error occured, failed registering user.'
    }

    # Return success status
    return {
        'status' : 'success',
        'message' : 'user registered'
    }

