from typing import List
from fastapi import FastAPI ,WebSocket, WebSocketDisconnect
from fastapi.testclient import TestClient
app = FastAPI()

 

class ConnectionManager:

    def __init__(self):
        """ init the active_clients
        """
        self.active_clients : List[WebSocket] = []

 

    async def connect(self, websocket: WebSocket):
        """add new client for connecting
        """
        await websocket.accept()

        self.active_clients.append(websocket)

 

    def disconnect(self, websocket: WebSocket):
        """disconnect the client
        """
        self.active_clients.remove(WebSocket)

 

    async def broadcast(self, message: str):
        """broadcast the message
        """
        for connection in self.active_clients:
            await connection.send_text(message)

 

manager = ConnectionManager()

 

@app.websocket("/ws/{username}")

async def websocket_endpoint(websocket: WebSocket, username: str):

    await manager.connect(websocket)

    await manager.broadcast(f"{username}")

    try:
        while True:

            data = await websocket.receive_text()
            await manager.broadcast(f"{username}:{data}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)
