from channels.consumer import SyncConsumer


class SyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("websocket connected")
        
    def websocket_receive(self,event):
        print("websocket receive")

    def websocket_disconnect(self,event):
        print("websocket disconnected")
