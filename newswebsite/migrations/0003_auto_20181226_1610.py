# Generated by Django 2.0 on 2018-12-26 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newswebsite', '0002_remove_comment_to_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='best',
            options={'verbose_name': '精选分类', 'verbose_name_plural': '精选分类'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '分类', 'verbose_name_plural': '分类'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
    ]
