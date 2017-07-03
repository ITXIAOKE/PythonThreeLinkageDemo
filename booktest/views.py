from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator

from booktest.models import AreaInfo


# 分页显示地区的视图函数
def part_area(request, pindex):  # pindex是页码
    # 获取所有省级,省级的父级为null
    province = AreaInfo.objects.filter(aparent__isnull=True)
    # 对省级信息进行分页,每页有5条数据
    paginator = Paginator(province, 5)

    # 当url中没有页码的时候，默认显示第一页的数据
    if pindex == '':
        pindex = 1
    # 获取pindex页的page对象
    page = paginator.page(int(pindex))
    return render(request, 'booktest/part_area.html', {'page': page})


#省市县案例
def show_area(request):
    return render(request, 'booktest/show_area.html')

#查询所有省级地区的信息
def prov(request):
    #查询所有省级地区的信息
    areas = AreaInfo.objects.filter(aparent__isnull = True)
    list_areas = []
    for area in areas:
        list_areas.append([area.id, area.atitle])
    #json
    return JsonResponse({'data':list_areas})

# 市和县都用这个视图函数
def city(request, pid):
    #查询pid省下的所有市级地区信息
    areas = AreaInfo.objects.filter(aparent_id = int(pid))
    #拼接数据
    list_areas = []
    for area in areas:
        list_areas.append([area.id, area.atitle])
    # json
    return JsonResponse({'data': list_areas})
