from django.shortcuts import render, HttpResponse
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
import dashboard.models as dashboard_models
from django.db.models.aggregates import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Count
from django.db.models import F
import json
from django.db import transaction
from django.utils import timezone


# Create your views here.
class Blog(View):

    def get(self, request, **kwargs):
        data = {}
        if request.user.is_authenticated:
            user = request.user
            num_article = dashboard_models.Article.objects.filter(user=user, status=True).aggregate(Count('id'))
            
            data['num_article'] = num_article['id__count']
        

        param = kwargs.get('param', '')
        condition = kwargs.get('condition', '')

        page = request.GET.get('page', 1)# 获取分页数
        
        if condition == 'category':
            if param == '': 
                articles = dashboard_models.Article.objects.filter(status=True).order_by('-create_time')
            else:
                articles = dashboard_models.Article.objects.filter(category__id=param, status=True).order_by('-create_time')
        elif condition == 'tag':
            if param == '': 
                articles = dashboard_models.Article.objects.filter(status=True).order_by('-create_time')
            else:
                articles = dashboard_models.Article.objects.filter(tag__id=param, status=True).order_by('-create_time')
        else:
            if param == '': 
                articles = dashboard_models.Article.objects.filter(status=True).order_by('-create_time')
            else:
                articles = dashboard_models.Article.objects.filter(archive__id=param, status=True).order_by('-create_time')
        
        paginator = Paginator(articles, 4)
        num_pages = paginator.num_pages
        
        page_list = paginator.page_range
        if int(float(page)) > num_pages:
            page = num_pages
        elif int(float(page)) <1 :
            page = 1
        
        try:
            page_article = paginator.page(page)  # 获取当前页码的记录
        except PageNotAnInteger:
            page_article = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
        
        data['page_article'] = page_article
        data['num_pages'] = num_pages
        data['page_list'] = page_list
        data['apage'] = int(float(page))
        data['redue_page'] = int(float(page))-2
        data['improve_page'] = int(float(page))+2
        # article_list = {'articles': articles} 
        # print(article_list)
        data['articles'] = articles
        
        # 热门文章

        hot_article = dashboard_models.Article.objects.filter(status=True).order_by('up_count')[:10]
        data['hot_article'] = hot_article





        tag_list = dashboard_models.Tag.objects.values('name').annotate(c=Count('article__id')).values('id', 'name', 'c')
        categroy_list = dashboard_models.Category.objects.values('name').annotate(c=Count('article__id')).values('id', 'name', 'c')

        data['tag_list'] = tag_list
        data['category_list'] = categroy_list
        return render(request, 'blog/index.html', data)

    # def post(self, request):
    #     pass


class Condition_blog(View):

    def get(self, request, **kwargs):
        pass
        

    def post(self, request):
        pass

# class User_admin(View):

#     def get(self, request):
#         if not request.user.is_authenticated:
#             return render(request, 'login_logout_register/login.html')
#         data = {}
#         category_list = dashboard_models.Category.objects.filter()
#         tag_list = dashboard_models.Tag.objects.filter()
#         data['category_list'] = category_list
#         data['tag_list'] = tag_list
#         return render(request, 'blog/user_admin.html', data)
        
#     @csrf_exempt
#     def post(self, request):
        
#         article_title = request.POST.get('article_title')
#         article_abstract = request.POST.get('article_abstract')
#         article_content = request.POST.get('article_content')
#         article_category = request.POST.get('article_category')
#         article_tag = request.POST.get('article_tag')
#         user = request.user
#         create_time = timezone.now()
#         article = dashboard_models.Article.objects.create(title=article_title, abstract=article_abstract, content=article_content, category=article_category, user=user, create_time=create_time)
#         article.tag.add(tag=article_tag)

#         return HttpResponse('创建成功')
        


class Article_detail(View):

    def get(self, request, **kwargs):
        data = {}
        id = kwargs.get('article_id')
        article = dashboard_models.Article.objects.filter(id=id).first()
        data['article'] = article

        comment_list = dashboard_models.Comment.objects.filter(article=article)
        data['comment_list'] = comment_list
        return render(request, 'blog/article_detail.html', data)
        

    def post(self, request):
        pass


class Comment(View):

    def get(self, request):
        pass
        
    @csrf_exempt
    def post(self, request):
        if not request.user.is_authenticated:
            return render(request, 'login_logout_register/login.html')
        data= {}
        if not request.user.is_authenticated:
            return render(request, 'login_logout_register/login.html')

        article_id = request.POST.get('article_id')
        content = request.POST.get('content')
        pid = request.POST.get('pid')
        
        to_user = request.POST.get('to_user', '')
        user_id = request.user.id
        print(article_id, content, pid, to_user, user_id)

        with transaction.atomic():
            comment = dashboard_models.Comment.objects.create(article_id=article_id, content=content, parent_comment_id_id=pid, user_id=user_id, to_user=to_user)
            dashboard_models.Article.objects.filter(id=article_id).update(comment_count=F("comment_count") + 1)
            data['comment_id'] = comment.id
            data['username'] = comment.user.username
            data['content'] = comment.content
            data['to_user'] = comment.to_user

            data["create_time"] = comment.create_time.strftime("%Y-%m-%d %S")

        return JsonResponse(data)


def return_request(request):
    return {'return_request': request}
        



