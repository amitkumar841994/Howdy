from channels.consumer import SyncConsumer,AsyncConsumer
from rest_framework.permissions import IsAuthenticated


class MysyncConsumer(SyncConsumer):
    permission_classes = [IsAuthenticated]


    def websocket_connect(self,event):
        print("websocket connected")
        self.send({
            'type':'websocket.accept'
            
        })
        
    def websocket_receive(self,event):

        print("websocket receive",event['text'])
        self.send({
            'type':'websocket.send',
            'text':"This is server"
            
        })

        
        

    def websocket_disconnect(self,event):
        print("websocket disconnected")
