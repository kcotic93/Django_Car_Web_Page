from functools import wraps
from django.shortcuts import redirect
from django.http import HttpResponseForbidden



def admin_access():
	def decorator(f): 
		@wraps(f)
		def wrapper(request, *args, **kwargs):
			###
			if request.user.is_superuser:
				return f(request, *args, **kwargs)
			else:
				return HttpResponseForbidden("Niste ulogirani kao admin korisnik!!!")
			###
		return wrapper		
	return decorator


def staff_access():
	def decorator(f): 
		@wraps(f)
		def wrapper(request, *args, **kwargs):
			###
			if request.user.is_staff:
				return f(request, *args, **kwargs)
			else:
				return HttpResponseForbidden("Niste ulogirani kao staff korisnik!!!")
			###
		return wrapper		
	return decorator

def nonStaff_access():
	def decorator(f): 
		@wraps(f)
		def wrapper(request, *args, **kwargs):
			###
			if not (request.user.is_staff and request.user.is_superuser):
				return f(request, *args, **kwargs)
			else:
				return HttpResponseForbidden("Niste ulogirani kao obicni korisnik!!!")
			###
		return wrapper		
	return decorator