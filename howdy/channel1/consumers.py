from channels.consumer import SyncConsumer,AsyncConsumer


class MysyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("websocket connected")
        self.send({
            'type':'websocket.accept'
        })
        
    def websocket_receive(self,event):
        print("websocket receive")

    def websocket_disconnect(self,event):
        print("websocket disconnected")
