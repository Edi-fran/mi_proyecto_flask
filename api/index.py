from vercel_wsgi import handle
from app import app

def handler(request, *args, **kwargs):
    return handle(app, request, *args, **kwargs)
