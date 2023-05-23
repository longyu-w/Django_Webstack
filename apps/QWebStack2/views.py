from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Category, SubCategory, Site,titles

# Create your views here.

def index_view(request):
    cates = Category.objects.all()
    titless = titles.objects.all()
    total = []
    for cate in cates:
        subcates = SubCategory.objects.filter(parent=cate)
        c_res = {'cate':cate, 'subcate':[]}
        for subcate in subcates:
            sites = Site.objects.filter(category=subcate)
            c_res['subcate'].append({'subcate':subcate,'sites':sites})
        total.append(c_res)
    context = {
        "titles": titless,
        "data": total
    }
    return render(request, 'Qwebstack2/index.html', context=context)
#最后格式为 [{'cate':大分类, 'subcate':[{'subcate':子分类,'sites':数据}]}]

def test_view(request):
    # with open('data.csv','r',encoding='utf-8') as f:
    #     for item in f.readlines():
    #         data = item.split(',')
    #         data[-1].replace('\n','')
    #         if data[0] == '摄影图库':
    #             sub = SubCategory.objects.filter(name='摄影资源')
    #             if len(sub) != 0:
    #                 s = Site(name=data[-2],describtion=data[-1],url=data[1],logo_url=data[2],category=sub.first())
    #                 s.save()
    return