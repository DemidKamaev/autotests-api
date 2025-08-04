import websockets
from websockets import ServerConnection
import asyncio


async def webs_server(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")

        for num in range(1, 6):
            await websocket.send(f"{num} Сообщение пользователя: {message}")


async def main():
    server = await websockets.serve(webs_server, "localhost", 8765)
    print("WS сервер запущен на ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())
