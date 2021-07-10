from django.http.response import HttpResponseBadRequest
from django.shortcuts import render

from django.http import HttpResponseForbidden, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import os
import json

# Create your views here.
from rest_framework import generics, status
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

import urllib.parse
from datetime import datetime, timedelta, time
from django.db.models import Q


from .functions import submit_rest_requests,get_scheduls


@api_view(['POST'])  # POSTやなんやら色々設定できる。
def register_rest_requests(request):
    val = submit_rest_requests(request.data)
    return Response(val)


@api_view(['POST'])  # POSTやなんやら色々設定できる。
def get_rest_scheduls(request):
    val = get_scheduls(request.data)
    return Response(val)



