from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse,Http404
from django.core.files.storage import FileSystemStorage
from .forms import uploadFileForm
from TextToPPT.orchestrator import TextToPPTOrchestrator

def uploadtxtfiles(request):
    if request.method == 'POST':
        form = uploadFileForm(request.POST, request.FILES)
        doc = request.FILES['document']
        shape = form.data['shapeType']
        authorName = form.data['authorName']

        startDate = form.data['startDate']
        endDate = form.data['endDate']

        fontSize = form.data['fontSize']
        Left = form.data['Left']
        Top = form.data['Top']
        Height = form.data['Height']
        Width = form.data['Width']
        filestorage = FileSystemStorage()
        filename = filestorage.save(doc.name,doc)
        name = filename+".pptx"
        file_path = os.path.join(settings.MEDIA_ROOT,name)
        in_path = os.path.join(settings.MEDIA_ROOT,filename)
        out_path = os.path.join(settings.MEDIA_ROOT,filename+".pptx") #combine the directory with file
        TextToPPTLibrary_class = TextToPPTOrchestrator()
        TextToPPTLibrary_class.SetShapeType(shape)
        TextToPPTLibrary_class.SetMessageAuthor(authorName)

        TextToPPTLibrary_class.SetStartDate(startDate)
        TextToPPTLibrary_class.SetEndDate(endDate)      

        TextToPPTLibrary_class.SetFontSize(fontSize)
        TextToPPTLibrary_class.SetShapeLeft(Left)
        TextToPPTLibrary_class.SetShapeTop(Top)
        TextToPPTLibrary_class.SetShapeHeight(Height)
        TextToPPTLibrary_class.SetShapeWidth(Width)
        TextToPPTLibrary_class.ConvertTextFileToPPT(in_path,out_path)
        if os.path.exists(file_path):
            with open(file_path,'rb') as file:
                response = HttpResponse(file.read(),content_type = "application/vnd.openxmlformats-officedocument.presentationml.presentation")
                response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
                return response
    return render(request,'uploadmethod/upload.html')