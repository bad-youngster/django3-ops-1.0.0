from django.http import JsonResponse
from aliyunControls.views import aliyunEcs
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
            nickname=result.get('nickname'),
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
        q['nickname'] = c.nickname
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
        assets = []
        for i in result.get('items'):
            for asset in i.get('assets'):
                c = {}
                if path_name.get('type') == asset.get('path').split('/')[0]:
                    c['downlaod_url'] = asset.get('downloadUrl')
                    c['path'] = asset.get('path').split('/')[0]
                    assets.append(c)
        return JsonResponse(assets, safe=False)
    result = NexusStore().nexus_upload()
    assets = []
    for i in result.get('items'):
        for asset in i.get('assets'):
            c = {}
            c['downlaod_url'] = asset.get('downloadUrl')
            c['path'] = asset.get('path').split('/')[0]
            assets.append(c)
    return JsonResponse(assets, safe=False)


def nexus_mysql_script(request):
    result = NexusStore().nexus_mysql_script()
    assets = []
    for i in result.get('items'):
        for asset in i.get('assets'):
            c = {}
            c['downlaod_url'] = asset.get('downloadUrl')
            c['path'] = asset.get('path').split('/')[1]
            assets.append(c)
    return JsonResponse(assets, safe=False)


def mysql_install(request):
    if request.method == 'POST':
        result = json.loads(request.body)
        ip = result.get('ip')
        auth = result.get('user')
        authors = UserAuth.objects.values('username',
                                          'passwd').filter(nickname=auth)
        asset = Assets.objects.values('hostip', 'port').filter(hostip=ip)
        combined_results = {}
        for i in list(authors):
            combined_results['username'] = i.get('username')
            combined_results['pwd'] = i.get('passwd')
        for y in list(asset):
            combined_results['host'] = y.get('hostip')
            combined_results['port'] = y.get('port')
        down_url = result.get('download_url')
        script_url = result.get('script_download_url')

        script_cmd = 'wget --user=%s --password=%s %s ' % (
            settings.NEXUS_USER, settings.NEXUS_PASS, script_url)
        down_cmd = 'wget --user=%s --password=%s %s' % (
            settings.NEXUS_USER, settings.NEXUS_PASS, down_url)

        res_match_down = re.search(r"/([^/]+)$", down_url).group(1)
        res_match_script = re.search(r"/([^/]+)$", script_url).group(1)

        res = Ssh(combined_results).run_cmd('%s;%s' % (script_cmd, down_cmd))
        print(res)
        res1 = Ssh(combined_results).run_cmd(
            'mv %s %s /opt/' % (res_match_down, res_match_script))
        print(res_match_down, res_match_script)
        res2 = Ssh(combined_results).run_cmd(
            'cd /opt;sh -x %s %s' % (res_match_script, res_match_down))
        print(res2)

        return JsonResponse({'status': 200})
    Mysql().install()
    return JsonResponse({'status': 200})


def get_single_ecs(request):
    result = aliyunEcs().aliyun_ecs_assets()
    return JsonResponse(result, safe=False)


def get_describe_regions(request):
    result = aliyunEcs().aliyun_ecs_regions()
    return JsonResponse(result, safe=False)


def select_single_ecs(request):
    if request.method == 'POST':
        result_body = json.loads(request.body)
        result_data = aliyunEcs().aliyun_select_single_ecs(result_body)
        result_instances = result_data.body.instances.instance
        result_snap_data = aliyunEcs().select_snapshots_single_ecs(result_body)
        for s in result_snap_data:
            if s.get('SourceDiskType') == 'data':
                data_snapshotId = s.get('SnapshotId')
        result_snap_image = aliyunEcs().aliyun_create_image(result_snap_data)
        if result_snap_image.status_code == 200:
            image_id = result_snap_image.body.image_id
        instances = []
        for i in result_instances:
            instance = {}
            instance['InstanceType'] = i.instance_type
            instance['KeyPairName'] = i.key_pair_name
            instance['Tags'] = i.tags
            instance['VSwitchId'] = i.vpc_attributes.v_switch_id
            instance[
                'SecurityGroupIds'] = i.security_group_ids.security_group_id
            instance['imageId'] = image_id
            instance['data_snapid'] = data_snapshotId
            instances.append(instance)
            aliyunEcs().aliyun_create_single_ecs(instance)

        return JsonResponse({'status': 200})

    return JsonResponse({'status': 200})


def mysql_to_slave(request):
    aliyunEcs().aliyun_create_single_ecs()

    return JsonResponse({'status': 200})


def aliyun_ecs_assets(request):
    if request.method == 'POST':
        results = json.loads(request.body)
        try:
            region_result = aliyunEcs().aliyun_region_instance_ecs(
                results['regionid'])
            return JsonResponse(region_result, safe=False)
        except Exception as error:
            return error

    result = aliyunEcs().aliyun_ecs_assets()
    return JsonResponse(result, safe=False)


def aliyun_ecs_vpc(request):
    aliyunEcs().aliyun_get_vpc()

    return JsonResponse({'status': 200})
