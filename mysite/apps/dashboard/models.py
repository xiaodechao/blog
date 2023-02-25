from django.db import models
from django.contrib.auth.models import AbstractUser
# timezone 用于处理时间相关事务。
from django.utils import timezone
from ckeditor.fields import RichTextField




class UserInfo(AbstractUser):
    '''
    用户信息
    '''
    id = models.BigAutoField(primary_key=True)
    telephone = models.CharField(max_length=11, null=True, unique=True, verbose_name='电话')
    avatar = models.FileField(upload_to='avatars/', default='avatars/default.png', verbose_name='头像')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    by_upvote = models.IntegerField(default=0, verbose_name='被点赞')
    # gender=models.IntegerField(choices=((1,'男'),(2,'女')),verbose_name='性别')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.username

# Create your models here.
# 文章分类
class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('文章分类', max_length=100)
    user =  models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='作者',)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#文章标签
class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('文章标签',max_length=100)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='作者')
    
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='文章标题', )
    # 文章作者。参数 on_delete 用于指定数据删除的方式
    abstract = models.TextField('摘要', max_length=200, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    
    content = RichTextField(verbose_name='文章内容')
    # 文章创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    image = models.ImageField(upload_to='images')
  
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    comment_count = models.IntegerField(default=0, verbose_name='评论数')
    up_count = models.IntegerField(default=0, verbose_name='点赞数')
    down_count = models.IntegerField(default=0, verbose_name='踩一下数')
    status = models.BooleanField(default=True)

    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='作者',)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tag = models.ManyToManyField(Tag, 
                                through='Article2Tag',
                                through_fields=('article', 'tag'),
                                verbose_name='标签')

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        # ordering = ('-created',)
        # permissions = (
        #     ("publish_article", "Can publish article"),
        #     ("comment_article", "Can comment article"),
        # )
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        # return self.title 将文章标题返回
        return self.title

class Article2Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    article = models.ForeignKey(Article, verbose_name='文章', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, verbose_name='标签', on_delete=models.CASCADE)

    class Meta:
        '''
        联合唯一，两个字段不能重复
        '''
        unique_together = [
            ('article', 'tag'),
        ]
        verbose_name = '文章_标签'
        verbose_name_plural = verbose_name



    def __str__(self):
        v = self.article.title + '---' + self.tag.name
        return v

class ArticleUpDown(models.Model):
    '''
    文章点赞踩灭表
    '''
    id = models.BigAutoField(primary_key=Tag)
    user = models.ForeignKey(UserInfo, null=True, on_delete=callable, verbose_name='用户',)
    article = models.ForeignKey(Article, null=True, on_delete=callable, verbose_name='文章',)
    is_up = models.BooleanField(default=True, verbose_name='赞还是踩',)

    class Meta:
        unique_together = [
            ('article', 'user'),
        ]
        verbose_name = '文章顶踩'
        verbose_name_plural = verbose_name

class Comment(models.Model):
    '''
    评论表
    根评论：对文章的评论
    子评论：对评论的评论
    '''
    id = models.BigAutoField(primary_key=True)
    article = models.ForeignKey(Article, verbose_name='评论文章',on_delete=callable)
    user = models.ForeignKey(UserInfo, verbose_name='评论者', on_delete=callable)
    content = models.CharField(verbose_name='评论内容', max_length=255)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    parent_comment_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE, verbose_name='父评论',)
    to_user = models.CharField(max_length=50, verbose_name='评论对象', default='')


    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name
 
    def __str__(self):
        return self.content
        
