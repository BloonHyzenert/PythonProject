# 
from tick.src.tick import (
  tick_all
)

#
from aiohttp import web

#
app_tick = web.Application()

#
app_tick.add_routes([

  web.get('/', tick_all),
  
  
])
