from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'the_nightmare_we_share',
        'HOST': 'shobu.fr',
        'PORT': 27018,
        'USER': 'mongoadmin',
        'PASSWORD': 'Jioshield13#Saucisse'
    }

    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    # }
}