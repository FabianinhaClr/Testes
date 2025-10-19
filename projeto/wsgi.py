"""
WSGI config for projeto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

# Cria a aplicação padrão do Django
application = get_wsgi_application()

# Adiciona uma rota /ping simples (útil para health check)
def ping_application(environ, start_response):
    if environ.get('PATH_INFO') == '/ping':
        status = '200 OK'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        return [b'Ping response']
    # Caso contrário, processa normalmente pelo Django
    return application(environ, start_response)

# O que o Vercel (ou servidor WSGI) usará como entrada
app = ping_application
