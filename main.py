
# import asyncio

# from copra.websocket import Channel, Client

# loop = asyncio.get_event_loop()

# channel = Channel('user', 'LTC-USD')

# ws = Client(loop, channel, auth=True, key=KEY, secret=SECRET, passphrase=PASSPHRASE)

# try:
#     loop.run_forever()
# except KeyboardInterrupt:
#     loop.run_until_complete(ws.close())
#     loop.close()


import asyncio

from copra.websocket import Channel, Client
from autobahn.asyncio.websocket import WebSocketClientFactory

class Client(WebSocketClientFactory):

	def on_message(self, message):
		tick = Tick(message)
		print(tick, "\n\n")
		# if message['type'] == 'ticker' and 'time' in message:



loop = asyncio.get_event_loop()

ws = Client(loop, Channel('full', 'BTC-USD'))



ticker = Ticker(loop, ws)

try:
    loop.run_forever()
except KeyboardInterrupt:
    loop.run_until_complete(ws.close())
    loop.close()


