
from .base import *
from .base import env

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', 
default="GqhuNsvdlYQW3mQvuDJLDp0XTK0WC60cYObtD1iPyVsmluyLao",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG_TOOLBAR_PATH = env('DEBUG_TOOLBAR_PATH', default=None)
#SECRET_KEY = 'django-insecure-u(nnc%d9z5olov%9q3e267l!hueli7b!*h_92aj#@&d)c4n$9='

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

