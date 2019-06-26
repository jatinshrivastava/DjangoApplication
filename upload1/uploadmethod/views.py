import os
from django.conf import settings
from django.http import HttpResponse,Http404
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import uploadFileForm
from package.orchestrator import ConvertTextFileToPPT

def uploadtxtfiles(request):
       #return HttpResponse('Hello_WOrld')
       if request.method == 'POST':
       	doc = request.FILES['document']
       	fs = FileSystemStorage()
       	filename = fs.save(doc.name,doc)
       	#return HttpResponse (doc.name)
       	name = filename+".pptx"
       	file_path = os.path.join(settings.MEDIA_ROOT,name)
       	in_path = os.path.join(settings.MEDIA_ROOT,filename)
       	out_path = os.path.join(settings.MEDIA_ROOT,filename+".pptx") #combine the directory with file
       	ConvertTextFileToPPT(in_path,out_path)
       	if os.path.exists(file_path):
       		with open(file_path,'rb') as fh:
       			response = HttpResponse(fh.read(),content_type = "application/vnd.openxmlformats-officedocument.presentationml.presentation")
       			response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
       			return response
       return render(request,'uploadmethod/upload.html')
