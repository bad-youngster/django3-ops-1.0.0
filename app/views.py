from django.http import JsonResponse
from app.mysqlInstall.mysqlInstall import Mysql
from nexusControls.views import NexusStore
import json
import re
from utilitys.ssh import Ssh
from .models import UserAuth, UserType, Assets
from django.core.serializers import serialize
from django.conf import settings
# Create your views here.


def user_add(request):
    if request.method == 'POST':
        result = json.loads(request.body)
        print(result)
        user_type = UserType.objects.create(type=int(result.get('type')))
        data, code = UserAuth.objects.get_or_create(
            username=result.get('username'),
            passwd=result.get('password'),
            type=user_type)
        if code:
            return JsonResponse({'msg': '添加成功', 'code': 200})
        else:
            return JsonResponse({'msg': '添加失败', 'code': 400})
    return JsonResponse({'status': 200})


def user_get(request):
    code = UserAuth.objects.all()
    user = []
    for c in code:
        q = {}
        q['username'] = c.username
        q['passwd'] = c.passwd
        if int(c.type.type) == 1:
            q['type'] = '普通用户'
        elif int(c.type.type) == 0:
            q['type'] = '特权用户'
        else:
            q['type'] = int(c.type.type)
        user.append(q)
    return JsonResponse(user, safe=False)


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
        ip = result.get('ip')
        auth = result.get('user')
        authors = UserAuth.objects.values('username',
                                          'passwd').filter(username=auth)
        asset = Assets.objects.values('hostip', 'port').filter(hostip=ip)
        combined_results = {}
        for i in list(authors):
            combined_results['username'] = i.get('username')
            combined_results['pwd'] = i.get('passwd')
        for y in list(asset):
            combined_results['host'] = y.get('hostip')
            combined_results['port'] = y.get('port')
        down_url = result.get('download_url')
    
        res = Ssh(combined_results).run_cmd(
            'wget --user=%s --password=%s %s' %
            (settings.NEXUS_USER, settings.NEXUS_PASS, down_url))
        res_match = re.search(r"/([^/]+)$", down_url).group(1)
        

        return JsonResponse({'status': 200})
    Mysql().install()
    return JsonResponse({'status': 200})
