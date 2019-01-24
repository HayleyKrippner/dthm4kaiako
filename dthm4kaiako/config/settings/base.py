"""Base settings to build other settings files upon."""

import os.path
import environ
from datetime import datetime
import pytz


# dthm4kaiako/dthm4kaiako/config/settings/base.py - 3 = dthm4kaiako/dthm4kaiako/
ROOT_DIR = environ.Path(__file__) - 3

env = environ.Env()

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)

# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = 'NZ'
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-NZ'
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = False
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

DATE_FORMAT = 'j M Y'                   # '25 Oct 2006'
TIME_FORMAT = 'P'                       # '2:30 p.m.'
DATETIME_FORMAT = 'j M Y, P'            # '25 Oct 2006, 2:30 p.m.'
YEAR_MONTH_FORMAT = 'F Y'               # 'October 2006'
MONTH_DAY_FORMAT = 'j F'                # '25 October'
SHORT_DATE_FORMAT = 'd/m/Y'             # '25/10/2006'
SHORT_DATETIME_FORMAT = 'd/m/Y P'       # '25/10/2006 2:30 p.m.'
FIRST_DAY_OF_WEEK = 0                   # Sunday

# The *_INPUT_FORMATS strings use the Python strftime format syntax,
# see https://docs.python.org/library/datetime.html#strftime-strptime-behavior
DATE_INPUT_FORMATS = [
    '%d/%m/%Y', '%d/%m/%y',             # '25/10/2006', '25/10/06'
    # '%b %d %Y', '%b %d, %Y',          # 'Oct 25 2006', 'Oct 25, 2006'
    # '%d %b %Y', '%d %b, %Y',          # '25 Oct 2006', '25 Oct, 2006'
    # '%B %d %Y', '%B %d, %Y',          # 'October 25 2006', 'October 25, 2006'
    # '%d %B %Y', '%d %B, %Y',          # '25 October 2006', '25 October, 2006'
]
DATETIME_INPUT_FORMATS = [
    '%Y-%m-%d %H:%M:%S',                # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',             # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M',                   # '2006-10-25 14:30'
    '%Y-%m-%d',                         # '2006-10-25'
    '%d/%m/%Y %H:%M:%S',                # '25/10/2006 14:30:59'
    '%d/%m/%Y %H:%M:%S.%f',             # '25/10/2006 14:30:59.000200'
    '%d/%m/%Y %H:%M',                   # '25/10/2006 14:30'
    '%d/%m/%Y',                         # '25/10/2006'
    '%d/%m/%y %H:%M:%S',                # '25/10/06 14:30:59'
    '%d/%m/%y %H:%M:%S.%f',             # '25/10/06 14:30:59.000200'
    '%d/%m/%y %H:%M',                   # '25/10/06 14:30'
    '%d/%m/%y',                         # '25/10/06'
]
DECIMAL_SEPARATOR = '.'
THOUSAND_SEPARATOR = ','
NUMBER_GROUPING = 3


# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres:///dthm4kaiako'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'config.urls'
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    # Handy template tags
    'django.contrib.humanize',
    'django.contrib.admin',
]
THIRD_PARTY_APPS = [
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'markdownx',
    'ckeditor',
    'ckeditor_uploader',
    'django_activeurl'
]
LOCAL_APPS = [
    'general.apps.GeneralAppConfig',
    'users.apps.UsersAppConfig',
    'dtta.apps.DttaAppConfig',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {
    'sites': 'contrib.sites.migrations'
}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = 'users.User'
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = 'users:redirect'
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = 'account_login'

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
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

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = os.path.join(str(ROOT_DIR.path('staticfiles')), '')

# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/staticfiles/'
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
BUILD_ROOT = os.path.join(str(ROOT_DIR.path('build')), '')
STATICFILES_DIRS = [
    BUILD_ROOT,
]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.join(str(ROOT_DIR.path('media')), '')
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(ROOT_DIR.path('templates')),
        ],
        'OPTIONS': {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'config.context_processors.version_number.version_number',
                'config.context_processors.dtta_flat_pages.dtta_flat_pages',
            ],
            'libraries': {
                'markdown': 'config.filters.markdown',
            },
        },
    },
]
# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (
    str(ROOT_DIR.path('fixtures')),
)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = 'DENY'

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = 'admin/'
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [
    ("""UCCSER""", 'csse-education-research@canterbury.ac.nz'),
]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS


# django-allauth
# ------------------------------------------------------------------------------
# ACCOUNT_ALLOW_REGISTRATION = env.bool('DJANGO_ACCOUNT_ALLOW_REGISTRATION', True)
ACCOUNT_ALLOW_REGISTRATION = False
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = 'username'
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = 'users.adapters.AccountAdapter'
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_ADAPTER = 'users.adapters.SocialAccountAdapter'


# ckeditor
# ------------------------------------------------------------------------------
timezone = pytz.timezone(TIME_ZONE)
CKEDITOR_UPLOAD_PATH = datetime.now(timezone).strftime('%Y/%m/%d')
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
        'clipboard_defaultContentType': 'text',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            # 'devtools',  # Used for development
            'a11yhelp',
            'uploadimage',
            'image2',
            'div',
            'autolink',
            'autogrow',
            'clipboard',
            'codesnippet',
            'pastefromword',
            'widget',
            'dialog',
            'dialogui',
        ]),
    }
}

# django-activeurl
# ------------------------------------------------------------------------------
ACTIVE_URL_KWARGS = {
    'css_class': 'active',
    'parent_tag': 'li',
    'menu': 'yes',
    'ignore_params': 'no'
}
