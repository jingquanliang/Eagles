from channels.staticfiles import StaticFilesConsumer
from . import consumers
from channels import route

channel_routing = [
    # This makes Django serve static files from settings.STATIC_URL, similar
    # to django.views.static.serve. This isn't ideal (not exactly production
    # quality) but it works for a minimal example.

    # 'http.request': consumers.http_consumer,


    # 'http.request': StaticFilesConsumer(),

    # Wire up websocket channels to our consumers:
    # 'websocket.connect': consumers.ws_connect,
    # 'websocket.receive': consumers.ws_receive,
    # 'websocket.disconnect': consumers.ws_disconnect,
    route("websocket.connect", consumers.ws_connect),
    route("websocket.receive", consumers.ws_receive),
    route("websocket.disconnect", consumers.ws_disconnect),
    # route("websocket.connect", consumers.ws_connect, path=r"^/chat/*/$"),
    #  route("websocket.receive", consumers.ws_receive, path=r"^/chat/*/$"),
    #  route("websocket.disconnect", consumers.ws_disconnect, path=r"^/chat/*/$"),
]