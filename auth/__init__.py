import time

from aiohttp import web
from aiohttp_session import get_session


async def home(request):
    session = await get_session(request)

    if 'user_id' in session:
        return web.HTTPFound('/auth/welcome')

    last_visit = session.get('last_visit', 'never')
    session['last_visit'] = time.asctime()
    return web.Response(text='[home] your last visit was ' + last_visit)


async def login(request):
    session = await get_session(request)
    last_visit = session.get('last_visit', 'never')
    session['last_visit'] = time.asctime()
    session['user_id'] = 'anonymous'
    return web.Response(text='[login] your last visit was ' + last_visit)


async def signup(request):
    session = await get_session(request)
    last_visit = session.get('last_visit', 'never')
    session['last_visit'] = time.asctime()
    session['user_id'] = 'anonymous'
    return web.Response(text='[signup] your last visit was ' + last_visit)


async def logout(request):
    session = await get_session(request)
    last_visit = session.get('last_visit', 'never')
    session['last_visit'] = time.asctime()
    session.pop('user_id')
    return web.Response(text='[logout] your last visit was ' + last_visit)


async def welcome(request):
    session = await get_session(request)

    if 'user_id' not in session:
        return web.HTTPFound('/auth/')

    last_visit = session.get('last_visit', 'never')
    session['last_visit'] = time.asctime()
    return web.Response(text='[welcome] your last visit was ' + last_visit)
