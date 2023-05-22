# Generated by Django 4.1.7 on 2023-05-23 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='类别名称')),
                ('icon', models.CharField(default='linecons-lightbulb', max_length=20, verbose_name='图标')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='子类别名称')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='QWebStack2.category')),
            ],
            options={
                'verbose_name': '子分类',
                'verbose_name_plural': '子分类',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='#', max_length=256, verbose_name='网站链接')),
                ('logo_url', models.CharField(default='', max_length=256, verbose_name='logo链接')),
                ('name', models.CharField(max_length=20, verbose_name='网站名称')),
                ('describtion', models.TextField(blank=True, verbose_name='网站简介')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='QWebStack2.subcategory')),
            ],
            options={
                'verbose_name': '站点',
                'verbose_name_plural': '站点',
                'ordering': ['id'],
            },
        ),
    ]
