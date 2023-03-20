# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_7=qj@548$vr5zror*th9b4+++gf1-32vxtruc7h9g_f@y5yl='

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_library_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password'
    }
}