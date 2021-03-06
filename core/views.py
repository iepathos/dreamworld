from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def logout_redirect(request):
    """
    	Log users out and re-direct them to the homepage.
    """
    logout(request)
    return HttpResponseRedirect('/')