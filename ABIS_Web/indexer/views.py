from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    
    return render(request, 'indexer/index.html')

def import_page(request):
    # try:
    #     file = request.FILES['fileInput']
    #     fs = FileSystemStorage()
    #     fs.save("files/file.pdf", file)
    # except Exception:
    #     return False
    return render(request, 'indexer/import-page.html')

def about(request):
    return render(request , 'indexer/about.html')

def download_page(request):
    return render(request, 'indexer/download-page.html')