import os,sys
from .settings import BASE_DIR

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
INSTALLED_APPS = [
    'simpleui',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     
    'dashboard',
    'blog',
    'login_logout_register',
    'ckeditor',#富文本编辑器
    'ckeditor_uploader'#富文本编辑器上传图片模块
    


    
    
]



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'blog.context_processors.return_request'
                
            ],
        },
    },
]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite',
        'USER': 'root',
        'PASSWORD': 'xiao1314',
        'HOST': '',
        'PORT': '3306',
    }
}

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',  # 工具条功能
        'height': 300,  # 编辑器高度
        'width': 800,  # 编辑器宽
    },
}

CKEDITOR_UPLOAD_PATH = '/media/'  # 上传图片保存路径，如果没有图片存储或者使用自定义存储位置，那么则直接写  ' ' ,如果是使用django本身的存储方式，那么你就指名一个目录用来存储即可。

CKEDITOR_INAGE_BACKEND='pillow' 







AUTH_USER_MODEL = "dashboard.UserInfo"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 隐藏右侧SimpleUI广告链接和使用分析
SIMPLEUI_HOME_INFO = False 
SIMPLEUI_ANALYSIS = False 

 # 隐藏首页的快捷操作和最近动作
# SIMPLEUI_HOME_QUICK = False 
# SIMPLEUI_HOME_ACTION = False

# # 修改左侧菜单首页设置
# SIMPLEUI_HOME_PAGE = '百度一下，你就知道'  # 指向页面
# SIMPLEUI_HOME_TITLE = '百度欢迎你!' # 首页标题
# SIMPLEUI_HOME_ICON = 'fa fa-code' # 首页图标
 
#  # 设置右上角Home图标跳转链接，会以另外一个窗口打开
 