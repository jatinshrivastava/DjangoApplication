from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse,Http404
from django.core.files.storage import FileSystemStorage
from .forms import uploadFileForm
from TextToPPTLibrary.texttoppt.orchestrator import TextToPPTOrchestrator
#from package.orchestrator import TextToPPTOrchestrator

# Create your views here.

def uploadtxtfiles(request):
    if request.method == 'POST':
		# create a form instance and populate it with data from the request:
        form = uploadFileForm(request.POST, request.FILES)
        doc = request.FILES['document']
        shape = form.data['shapeType']
        filestorage = FileSystemStorage()
        filename = filestorage.save(doc.name,doc)
        name = filename+".pptx"
        file_path = os.path.join(settings.MEDIA_ROOT,name)
        in_path = os.path.join(settings.MEDIA_ROOT,filename)
        out_path = os.path.join(settings.MEDIA_ROOT,filename+".pptx") #combine the directory with file
        TextToPPTLibrary_class = TextToPPTOrchestrator()
        TextToPPTLibrary_class.SetShapeType(shape)
        TextToPPTLibrary_class.ConvertTextFileToPPT(in_path,out_path)
        if os.path.exists(file_path):
            with open(file_path,'rb') as file:
                response = HttpResponse(file.read(),content_type = "application/vnd.openxmlformats-officedocument.presentationml.presentation")
                response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
                return response
    return render(request,'uploadmethod/upload.html')