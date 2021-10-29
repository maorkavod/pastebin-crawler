from logging import getLogger
from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
import sys
import logging
from django.views.decorators.csrf import csrf_exempt


logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


logger = getLogger(__name__)

def home(request):
    return HttpResponse("home page")

def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", status=404)

def custom_error_view(request, exception=None):
    return render(request, "errors/404.html", status=404)


def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/404.html", status=404)


def custom_bad_request_view(request, exception=None):
    return render(request, "errors/404.html", status=404)