from django.http import JsonResponse
from nexusControls.views import NexusStore

# Create your views here.

def nexus_downfile(request):
    NexusStore().nexus_upload()
    return JsonResponse({'status': 200})
