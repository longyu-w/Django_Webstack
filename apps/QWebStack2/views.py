from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.

from django.shortcuts import render
from .models import Category, SubCategory, Site, Titles, friendlink
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
import os

# Create your views here.
# context = {}
# @cache_page(60 * 15)
def index_view(request):
    cates = Category.objects.all()
    titless = Titles.objects.all()
    titless = titless[0]
    friendlinks = friendlink.objects.all()
    fritotal = []
    for links in friendlinks:
        fritotal.append(links)

    total = []
    for cate in cates:
        subcates = SubCategory.objects.filter(parent=cate)
        c_res = {'cate': cate, 'subcate': []}
        for subcate in subcates:
            sites = Site.objects.filter(category=subcate)
            c_res['subcate'].append({'subcate': subcate, 'sites': sites})
        total.append(c_res)
    context = {
        "fritotal": fritotal,
        "titles": titless,
        "data": total
    }
    return render(request, 'Qwebstack2/index.html', context=context)


# 最后格式为 [{'cate':大分类, 'subcate':[{'subcate':子分类,'sites':数据}]}]

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


def static_my_view(request):
    # 非管理员用户不显示静态化页面
    if not request.user.is_superuser:
        return index_view(request)

    # 静态化
    html_content = render_to_string('my_template.html', context)
    file_path = os.path.join(settings.STATIC_ROOT, 'html', 'my_template.html')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        f.write(html_content)
    return HttpResponse(html_content)