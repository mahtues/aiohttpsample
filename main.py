import logging
import time
import os

from aiohttp import web
from aiohttp_session import setup, get_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from base64 import urlsafe_b64decode

from auth import home, login, signup, logout, welcome


app = web.Application()

setup(app, EncryptedCookieStorage(urlsafe_b64decode(os.environ['KNSITE_SECRET_KEY'])))

app.add_routes([
    web.get('/auth/', home),
    web.post('/auth/login', login),
    web.post('/auth/signup', signup),
    web.get('/auth/logout', logout),
    web.get('/auth/welcome', welcome),
])

if __name__ == '__main__':
    web.run_app(app)
else:
    logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = logger.handlers
    app.logger.setLevel(logger.level)
