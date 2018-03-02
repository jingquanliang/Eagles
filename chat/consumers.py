#coding=utf-8
import re
import json
import logging
from channels import Group
from channels.sessions import channel_session
from .models import Room

from django.http import HttpResponse
from channels.handler import AsgiHandler

log = logging.getLogger(__name__)



def http_consumer(message):
    # Make standard HTTP response - access ASGI path attribute directly
    response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)

@channel_session
def ws_connect(message):
    # Extract the room from the message. This expects message.path to be of the
    # form /chat/{label}/, and finds a Room if the message path is applicable,
    # and if the Room exists. Otherwise, bails (meaning this is a some othersort
    # of websocket). So, this is effectively a version of _get_object_or_404.

    print("yes,yes,yes,connect to start!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    try:
        prefix, label = message['path'].decode('ascii').strip('/').split('/')
        print("+++++++++++++++++++++++++++++++++++++++++++++:"+prefix)
        print("+++++++++++++++++++++++++++++++++++++++++++++:"+label)
        if prefix != 'chat':
            log.debug('invalid ws path=%s', message['path'])
            return
        #获取用户详细信息
        # room = Room.objects.get(label=label)
    except ValueError:
        log.debug('invalid ws path=%s', message['path'])
        return
    except Room.DoesNotExist:
        log.debug('ws room does not exist label=%s', label)
        return

    # log.debug('chat connect room=%s client=%s:%s',
        # room.label, message['client'][0], message['client'][1])
    
    # Need to be explicit about the channel layer so that testability works
    # This may be a FIXME?
    print('chat-'+label)
    Group('chat-'+label, channel_layer=message.channel_layer).add(message.reply_channel)

    message.channel_session['id'] = label #用户的id


@channel_session
def ws_receive(message):
    # Look up the room from the channel session, bailing if it doesn't exist
    try:
        label = message.channel_session['id']
        # room = Room.objects.get(label=label)
    except KeyError:
        log.debug('no id in channel_session')
        return
    except Room.DoesNotExist:
        log.debug('recieved message, buy id does not exist label=%s', label)
        return

    # Parse out a chat message from the content text, bailing if it doesn't
    # conform to the expected message format.
    try:
        data = json.loads(message['text'])

        # print(data)
        srcId = data['srcId']
        desId = data['desId']
        srcContent=data['srcContent']
    except ValueError:
        log.debug("ws message isn't json text=%s", text)
        return
    
    # if set(data.keys()) != set(('handle', 'message')):  #从前台传过来的就是这种格式的数据
    #     log.debug("ws message unexpected format data=%s", data)
    #     return

    if data:
        log.debug('chat to userid=%s messageContent=%s', desId , srcContent)
        # m = room.messages.create(**data)

        # See above for the note about Group
        Group('chat-'+str(srcId), channel_layer=message.channel_layer).send({'text': "%s" % message.content['text']})
        Group('chat-'+str(desId), channel_layer=message.channel_layer).send({'text': "%s" % message.content['text']})
        # print('chat-'+str(desId))

@channel_session
def ws_disconnect(message):
    try:
        label = message.channel_session['id']
        # room = Room.objects.get(label=label)
        Group('chat-'+label, channel_layer=message.channel_layer).discard(message.reply_channel)
    except (KeyError, Room.DoesNotExist):
        pass
