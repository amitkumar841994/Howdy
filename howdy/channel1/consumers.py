from channels.consumer import SyncConsumer,AsyncConsumer
from channels.generic.websocket import WebsocketConsumer
import json
from rest_framework.permissions import IsAuthenticated
from asgiref.sync import async_to_sync



class ChatConsumer(WebsocketConsumer):
    permission_classes = [IsAuthenticated]


    def connect(self):
        self.room_group_name='test'
        user=self.scope['user']
        print(">>>>>>>>>>>>>",self.scope["session"])
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({
        'message':"You are connected now!"
            
        }))
        
    def receive(self,text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']
        print("message",message)


        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
            'type':'chat_message',
            'message':message
            }
        )
    def chat_message(self,event):
        message=event['message']
        self.send(text_data=json.dumps({            
            'type':'chat',
            'message':message
            
        }))


        
        


