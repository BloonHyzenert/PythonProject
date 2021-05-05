
from aiohttp import  web
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport 
import yaml
from datetime import datetime
import aiohttp
import asyncio
import os
from rich import print


# /echo GET _echo_
# handler

#async def _tick_(request):
    #try:
        # 0 : extract payload dict
        #json = await request.json()



        #
        #return web.json_response(dict(json=json))

    # $>
    #except Exception as exp:
    # <!
        # !0 return what's wrong in string and the type of the exception should be enough to understand where you're wrong noobs
        #return web.json_response({'err':{'str':str(exp),'typ':str(type(exp))}}, status=500)
#`< - - - - - - - - - - - -

URL = 'https://dbschool.alcyone.life/graphql'

async def tick_all(request):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://51.15.17.205:9000/tick/AyeWai') as resp:
                info = await resp.json()
                ticks = info['data']
                # now = datetime.now()
                # filename = now.strftime("%Y%m%d")
                # info["timestamp"] = f'{datetime.timestamp(now)}'
                # data = yaml.dump(info)
                # file_path = f"./tick/data/{filename}.yaml"
                # mode = 'a' if os.path.exists(file_path) else 'w'
                # with open(file_path, mode) as f:
                #     f.write(data)

            transport = AIOHTTPTransport(url=URL)
            client = Client(transport=transport, fetch_schema_from_transport=True)

            for tick in ticks:
                query = gql("""mutation {
                                createTicker(input: { data: { symbol: "%s", price: %f } }) {
                                    ticker {
                                    symbol
                                    price
                                    }
                                }
                            }""" % (tick["symbol"], float(tick["price"]))
                        )

                result = await client.execute_async(query)
                print(result)

        return web.json_response(info)
    except Exception as e:
        print(e)
        raise e