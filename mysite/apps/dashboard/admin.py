from django.contrib import admin
from . import models
from django.utils.html import format_html


admin.site.site_header = "个人博客管理网站"
admin.site.index_title = "新闻后台"
 

class ArticleAdmin(admin.ModelAdmin):
    # Custom admin list view
    list_display = ('title', 'user', 'create_time','status', )
    # 设置列表可显示的字段

    '''设置过滤选项'''
    list_filter = ('status', )
    date_hierarchy = 'create_time'
    '''define which fields are editable on list view'''
    list_editable = ('status', )
    '''10 items per page'''
    list_per_page = 5

    '''Max 200 when clicking show all'''
    list_max_show_all = 200 #default
    # '''Calling select related objects to reduce SQL queries'''
    # list_select_related = ('user', )
 
    # '''Render a search box at top. ^, =, @, None=icontains'''
    search_fields = ['title', 'abstract']

 
    # '''Replacement value for empty field'''
    empty_value_display = 'NA'
 
    # '''filter options'''
    # list_filter = ('status', 'author__is_superuser', ) 
 
 
admin.site.register(models.Article, ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user' )
    # 设置列表可显示的字段

    '''设置过滤选项'''
    # list_filter = ('status', )
    # date_hierarchy = 'create_time'
    '''define which fields are editable on list view'''
    # list_editable = ('status', )
    '''10 items per page'''
    list_per_page = 5

    '''Max 200 when clicking show all'''
    list_max_show_all = 200 #default
    # '''Calling select related objects to reduce SQL queries'''
    # list_select_related = ('user', )
 
    # '''Render a search box at top. ^, =, @, None=icontains'''
    search_fields = ['name', 'user']

 
    # '''Replacement value for empty field'''
    empty_value_display = 'NA'
    

admin.site.register(models.Category, CategoryAdmin)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'create_time', 'is_staff', 'is_active',)
    # 设置列表可显示的字段

    '''设置过滤选项'''
    # list_filter = ('status', )
    # date_hierarchy = 'create_time'
    '''define which fields are editable on list view'''
    # list_editable = ('status', )
    '''10 items per page'''
    list_per_page = 10

    '''Max 200 when clicking show all'''
    list_max_show_all = 200 #default
    # '''Calling select related objects to reduce SQL queries'''
    # list_select_related = ('user', )
 
    # '''Render a search box at top. ^, =, @, None=icontains'''
    search_fields = ['username', 'is_staff']

 
    # '''Replacement value for empty field'''
    empty_value_display = 'NA'
    

admin.site.register(models.UserInfo, UserInfoAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'user' )
    # 设置列表可显示的字段

    '''设置过滤选项'''
    # list_filter = ('status', )
    # date_hierarchy = 'create_time'
    '''define which fields are editable on list view'''
    # list_editable = ('status', )
    '''10 items per page'''
    list_per_page = 5

    '''Max 200 when clicking show all'''
    list_max_show_all = 200 #default
    # '''Calling select related objects to reduce SQL queries'''
    # list_select_related = ('user', )
 
    # '''Render a search box at top. ^, =, @, None=icontains'''
    search_fields = ['name', 'user']

 
    # '''Replacement value for empty field'''
    empty_value_display = 'NA'
    

admin.site.register(models.Tag, TagAdmin)

class Article2TagAdmin(admin.ModelAdmin):
    list_display = ('article', 'tag' )
    # 设置列表可显示的字段

    '''设置过滤选项'''
    # list_filter = ('status', )
    # date_hierarchy = 'create_time'
    '''define which fields are editable on list view'''
    # list_editable = ('status', )
    '''10 items per page'''
    list_per_page = 10

    '''Max 200 when clicking show all'''
    list_max_show_all = 200 #default
    # '''Calling select related objects to reduce SQL queries'''
    # list_select_related = ('user', )
 
    # '''Render a search box at top. ^, =, @, None=icontains'''
    search_fields = ['article', 'tag']

 
    # '''Replacement value for empty field'''
    empty_value_display = 'NA'
    

admin.site.register(models.Article2Tag, Article2TagAdmin)


class ArticleUpDownAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'is_up')
    # 设置列表可显示的字段

    '''设置过滤选项'''
    # list_filter = ('status', )
    # date_hierarchy = 'create_time'
    '''define which fields are editable on list view'''
    # list_editable = ('status', )
    '''10 items per page'''
    list_per_page = 10

    '''Max 200 when clicking show all'''
    list_max_show_all = 200 #default
    # '''Calling select related objects to reduce SQL queries'''
    # list_select_related = ('user', )
 
    # '''Render a search box at top. ^, =, @, None=icontains'''
    search_fields = ['user', 'article',]

 
    # '''Replacement value for empty field'''
    empty_value_display = 'NA'
    

admin.site.register(models.ArticleUpDown, ArticleUpDownAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'create_time', 'to_user', )
    # 设置列表可显示的字段

    '''设置过滤选项'''
    # list_filter = ('status', )
    # date_hierarchy = 'create_time'
    '''define which fields are editable on list view'''
    # list_editable = ('status', )
    '''10 items per page'''
    list_per_page = 10

    '''Max 200 when clicking show all'''
    list_max_show_all = 200 #default
    # '''Calling select related objects to reduce SQL queries'''
    # list_select_related = ('user', )
 
    # '''Render a search box at top. ^, =, @, None=icontains'''
    search_fields = ['user', 'article', 'to_user',]

 
    # '''Replacement value for empty field'''
    empty_value_display = 'NA'
    

admin.site.register(models.Comment, CommentAdmin)

