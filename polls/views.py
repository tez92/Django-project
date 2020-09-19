

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FileForm
from django.core.files.storage import FileSystemStorage
from  .models import File
from django.contrib.auth.decorators import login_required



def home(request):
	context = {
		'files': files
	}
	return render(request, 'polls/home.html', context)

def delete_file(request, pk):
	if request.method == 'POST':
		file = File.objects.get(pk=pk)
		file.delete()
	return redirect('file_list')	


def file_list(request):
	files = File.objects.all()
	return render(request, 'polls/file_list.html', { 'files': files  })

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()    
    return render(request, 'polls/upload_file.html', {
        'form': form
    })

