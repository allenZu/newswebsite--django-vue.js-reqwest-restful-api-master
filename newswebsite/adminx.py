from extra_apps import xadmin
from newswebsite.models import *
# Register your models here.

class ArticleAdmin(object):
    # list_display = ['title', 'intro', 'abstract','category','publish_time','image','source_link',
    # 'author_name','author_avatar','author_desc']  # 列表显示
    search_fields = ['title', 'intro','abstract']  # 搜索
    list_filter = ['title', 'intro', 'abstract','category']   # 筛选Admin(object):

class CategoryAdmin(object):
    # list_display = ['Title:', 'Intro', 'Abstract','Category','Content','Publish time',]  # 列表显示
    search_fields = ['name']  # 搜索
    list_filter = ['name']   # 筛选Admin(object):

class BestAdmin(object):
    # list_display = ['Title:', 'Intro', 'Abstract','Category','Content','Publish time',]  # 列表显示
    # search_fields = ['select_article']  # 搜索
    list_filter = ['select_article']   # 筛选Admin(object):

class UserProfileAdmin(object):
    # list_display = ['Title:', 'Intro', 'Abstract','Category','Content','Publish time',]  # 列表显示
    search_fields = ['belong_to']  # 搜索
    list_filter = ['belong_to']   # 筛选Admin(object):

class CommentAdmin(object):
    # list_display = ['Title:', 'Intro', 'Abstract','Category','Content','Publish time',]  # 列表显示
    search_fields = ['words']  # 搜索
    list_filter = ['belong_article']   # 筛选Admin(object):


xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Best,BestAdmin)
xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(Comment,CommentAdmin)
