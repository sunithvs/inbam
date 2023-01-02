from dotenv import load_dotenv
import os

load_dotenv(".env")
settings = os.getenv('SETTINGS')
debug = os.getenv('DEBUG')

if settings == "prod":
    print("PRODUCTION SERVER")
    DEBUG = False
    from .common_settings import *

    ALLOWED_HOSTS = ["tr3dprint.com", "localhost", ""]
    STATIC_ROOT = "/var/www/html/static/"
    MEDIA_ROOT = '/var/www/html/media'

else:
    print("DEV SERVER")
    DEBUG = True
    from .common_settings import *

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
