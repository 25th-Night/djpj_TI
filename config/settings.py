"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.19.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os

from pathlib import Path

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# .env 파일 로드
load_dotenv()

# MEDIA 경로
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# STATIC 경로
# STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# SECRET_KEY
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# TEMPLATE 경로
TEMPLATE_DIR = BASE_DIR / "templates"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'mysite.com',
    '127.0.0.1',
    'localhost',
    os.getenv("NGROK_URL")
]

CSRF_TRUSTED_ORIGINS = [
    f'https://{os.getenv("NGROK_URL")}'
]

# Debug_Toolbr
INTERNAL_IPS = [
    '127.0.0.1',
]

# SITE_ID 설정
SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    # Custom Apps,
    'account.apps.AccountConfig',

    # Local Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.postgres',

    # Thrid-party Apps
    'taggit',
    'social_django',
    'django_extensions',
    'easy_thumbnails',
    'debug_toolbar',
    'rosetta',
    'parler',
    'localflavor',

    # Custom Apps,
    'blog.apps.BlogConfig',
    'images.apps.ImagesConfig',
    'actions.apps.ActionsConfig',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'coupons.apps.CouponsConfig',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv("POSTGRES_HOST"),
        'NAME': os.getenv("POSTGRES_DBNAME"),
        'PORT': os.getenv("POSTGRES_PORT"),
        'USER': os.getenv("POSTGRES_USER"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/


LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
    ('ko', _('Korean')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# email settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'   # 메일을 발송하지 않고 콘솔 창에 출력
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")


# login settings
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


# password hash settings
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]


AUTHENTICATION_BACKENDS = [
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.naver.NaverOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

# 페이스북 인증
SOCIAL_AUTH_FACEBOOK_KEY = os.getenv("SOCIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv("SOCIAL_AUTH_FACEBOOK_SECRET")

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# 구글 인증
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")

# 네이버 소셜 로그인 설정
SOCIAL_AUTH_NAVER_KEY = os.getenv("SOCIAL_AUTH_NAVER_KEY")
SOCIAL_AUTH_NAVER_SECRET = os.getenv("SOCIAL_AUTH_NAVER_SECRET")

# 네이버 소셜 로그인 데이터 범위
SOCIAL_AUTH_NAVER_EXTRA_DATA = ['profile_image']

# 소셜 로그인 JSON Field 추가 ( Postgres 경우 )
SOCIAL_AUTH_JSONFIELD_ENABLED = True

# 소셜 인증 파이프라인 추가
SOCIAL_AUTH_PIPELINE = [
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'account.authentication.create_profile',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
]

# get_absolute_url 오버라이드
ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('user_detail', args=[u.username])
}

# Redis 설정
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1

# Cart Session 설정
CART_SESSION_ID = 'cart'


# STRIPE API 관련 설정
STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_API_VERSION = os.getenv("STRIPE_API_VERSION")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")


# django-parler settings
PARLER_LANGUAGES = {
    1: (
        {'code': 'en'},
        {'code': 'ko'},
    ),
    'default': {
        'fallback': 'en',
        'hide_untranslated': False,
    }
}