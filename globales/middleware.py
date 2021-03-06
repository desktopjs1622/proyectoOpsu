# Standard Library
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
from datetime import datetime, timedelta

# Librerias Django
# Django Library
from django.conf import settings
from django.contrib import auth


class AutoLogout:
    def process_request(self, request):
        if not request.user.is_authenticated():
            return
        try:
            if datetime.now() - request.session['last_touch'] > timedelta(0, settings.AUTO_LOGOUT_DELAY * 60, 0):
                auth.logout(request)
                del request.session['last_touch']
                return
        except KeyError:
            pass
        request.session['last_touch'] = datetime.now()
