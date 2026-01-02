from django.conf import settings
from apps.app_info import APP_VERSION

def cfg_assets_root(request):

    return { 'ASSETS_ROOT' : settings.ASSETS_ROOT }


def global_settings(request):
    return {
        'APP_VERSION' : APP_VERSION
    }