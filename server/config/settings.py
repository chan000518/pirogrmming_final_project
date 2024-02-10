"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import environ
from pathlib import Path
import os
# from dotenv import load_dotenv

# load_dotenv()

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-09^97!th1@2z^k6v-_$bujzzk(oh53722q2_9#6x%o%0rp#thl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 사이트 기능 앱
    'apps.region',
    'apps.users',
    'apps.communitys',
    'apps.locations',
    'apps.score',
    'apps.games',
    'apps.search',

    # 소셜 로그인에 관련된 처리를 하는 어플리케이션
    'social_django',

    # 게시물에 html형식의 글을 쓰게 해주는 앱
    'tinymce',
]

AUTHENTICATION_BACKENDS = [
    'apps.users.backends.CustomModelBackend',  # 커스텀 모델 백엔드 추가
    'social_core.backends.kakao.KakaoOAuth2',  # 카카오
    'social_core.backends.naver.NaverOAuth2',  # 네이버
    'django.contrib.auth.backends.ModelBackend',  # 소셜로그인 정보를 User 모델 클래스에 저장
]

# 소셜 로그인을 위한 설정
SITE_ID = 1
SOCIALACCOUNT_LOGIN_ON_GET = True
LOGIN_REDIRECT_URL = 'communitys:board_list'  # 로그인 후 이동할 페이지
# ACCOUNT_LOGOUT_REDIRECT_URL = 'index' # 로그아웃 후 이동할 페이지
ACCOUNT_LOGOUT_ON_GET = True  # 로그 아웃 요청 시 바로 로그아웃 되도록
# 소셜 로그인 후 추가정보 입력을 위한 페이지로 이동
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "users:social_login"
SOCIAL_AUTH_URL_NAMESPACE = 'social'
#############################
# 1. 카카오
SOCIAL_AUTH_KAKAO_KEY = os.environ.get('SOCIAL_AUTH_KAKAO_KEY').strip()
SOCIAL_AUTH_KAKAO_SECRET = os.environ.get('SOCIAL_AUTH_KAKAO_SECRET').strip()

# 2. 네이버
SOCIAL_AUTH_NAVER_KEY = os.environ.get('SOCIAL_AUTH_NAVER_KEY').strip()
SOCIAL_AUTH_NAVER_SECRET = os.environ.get('SOCIAL_AUTH_NAVER_SECRET').strip()
##############################


#### 소셜로그인 후 필요한 정보 추가용 ####
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'apps.users.pipeline.set_username',
    'social.pipeline.debug.debug',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
AUTH_USER_MODEL = 'users.User'
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# 1. local db.sqlite3 사용할 경우
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 2. db 서버와 연결
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ.get('MYSQL_DBNAME'),
#         'USER': os.environ.get('MYSQL_USERNAME'),
#         'PASSWORD': os.environ.get('MYSQL_PASSWD'),
#         'HOST': os.environ.get('MYSQL_HOST'),
#         'PORT': int(os.environ.get('MYSQL_PORT')),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'


TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# 게시물에 html형식의 글을 쓰게 해주는 앱
# 커스텀 가능
# TINYMCE_DEFAULT_CONFIG = {
#     'cleanup_on_startup': True,
#     'custom_undo_redo_levels': 20,
#     'selector': 'textarea',
#     'theme': 'silver',
#     'plugins': '''
#             textcolor save link image media preview codesample contextmenu
#             table code lists fullscreen  insertdatetime  nonbreaking
#             contextmenu directionality searchreplace wordcount visualblocks
#             visualchars code fullscreen autolink lists  charmap print  hr
#             anchor pagebreak
#             ''',
#     'toolbar1': '''
#             fullscreen preview bold italic underline | fontselect,
#             fontsizeselect  | forecolor backcolor | alignleft alignright |
#             aligncenter alignjustify | indent outdent | bullist numlist table |
#             | link image media | codesample |
#             ''',
#     'toolbar2': '''
#             visualblocks visualchars |
#             charmap hr pagebreak nonbreaking anchor |  code |
#             ''',
#     'contextmenu': 'formats | link image',
#     'menubar': True,
#     'statusbar': True,
#     'theme_advanced_resizing': True,
#     "images_upload_url": "upload_image",
#     'width': '100%',
#     'height': 600
# }
