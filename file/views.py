from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import FileModel

# Create your views here.


def upload_file(request):
    pass
    '''
   if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = FileModel(file_field=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
    '''


def file_list(request):
    files_all_list = FileModel.objects.all()
    context = {}
    context['files'] = files_all_list
    return render(request, 'file/file_list.html', context)


