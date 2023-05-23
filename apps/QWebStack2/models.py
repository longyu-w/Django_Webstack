from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField("类别名称", max_length=10)
    icon = models.CharField('图标', max_length=20, default='linecons-lightbulb')

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self) -> str:
        return self.name


class SubCategory(models.Model):
    name = models.CharField("子类别名称", max_length=10)
    parent = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "子分类"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self) -> str:
        return self.name


class Site(models.Model):
    url = models.CharField('网站链接', max_length=256, default='#')
    logo_url = models.CharField('logo链接', max_length=256, default='')
    name = models.CharField('网站名称', max_length=20)
    describtion = models.TextField('网站简介', blank=True)
    is_show = models.BooleanField('是否展示', default=True)

    category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)

    class Meta:
        verbose_name = '站点'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self) -> str:
        return self.name


class titles(models.Model):
    titlea = models.CharField('标题', max_length=256, default='提瓦特爱好家协会')
    titleloader = models.CharField('加载中', max_length=256, default='提瓦特爱好家协会导航站加载中...')
    uplloadpage = models.CharField('网站提交', max_length=256, default='https://space.bilibili.com/90158726')
    about = models.CharField('关于网站', max_length=256, default='https://space.bilibili.com/90158726')
    end = models.CharField('关于网站', max_length=256,
                           default='本站内容源自互联网，如有内容侵犯了你的权益，请联系删除相关内容，联系邮箱：longyu_w@foxmail.com <br/>&copy; 2021 - {year} By [WebStack-Hugo](https://github.com/shenweiyan/WebStack-Hugo) | [Bio IT 爱好者](https://www.bioitee.com/) | [冀ICP备2022000685号-1](https://beian.miit.gov.cn)')

    class Meta:
        verbose_name = '主页设置'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self) -> str:
        return self.titlea
