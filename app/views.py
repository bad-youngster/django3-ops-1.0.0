from django.http import JsonResponse
from app.mysqlInstall.mysqlInstall import Mysql
from nexusControls.views import NexusStore
import json

# Create your views here.


def user_add(request):
    if request.method == 'POST':
        return JsonResponse({'status': 200})

    return JsonResponse({'status': 200})


def nexus_infofile(request):
    if request.method == 'POST':
        path_name = json.loads(request.body)
        result = NexusStore().nexus_upload()
        infofile = []
        for i in result.get('items'):
            for asset in i.get('assets'):
                assets = {}
                if path_name.get('type') == asset.get('path').split('/')[0]:
                    assets['downlaod_url'] = asset.get('downloadUrl')
                    assets['path'] = asset.get('path').split('/')[0]
                    infofile.append(assets)
        return JsonResponse(infofile, safe=False)
    result = NexusStore().nexus_upload()
    infofile = []
    for i in result.get('items'):
        for asset in i.get('assets'):
            assets = {}
            assets['downlaod_url'] = asset.get('downloadUrl')
            assets['path'] = asset.get('path').split('/')[0]
            infofile.append(assets)
    return JsonResponse(infofile, safe=False)


def mysql_install(request):
    if request.method == 'POST':
        result = json.loads(request.body)
        print(result)
        return JsonResponse({'status': 200})
    Mysql().install()
    return JsonResponse({'status': 200})
