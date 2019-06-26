import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, Http404
from uploadmethod.forms import uploadFileForm
from django.core.files.storage import FileSystemStorage
