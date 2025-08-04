import asyncio

import websockets


async def client():
    uri = "ws://localhost:8765"
    # Асихр контекстный менеджер
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"
        print(f"Отправка: {message}")
        await websocket.send(message)

        for _ in range(5):
            response = await websocket.recv()
            print(f"Ответ от сервера: {response}")


asyncio.run(client())

"""
1. Формируем ссылку, uri на который мы хотим подключится к нашему серверу ws
2. Открываем здесь контекстный менеджер, формируем соединение к нашему
серверу: получаем ClientConnection
Почему используется контекстный менеджер:
 Дело все в том, что когда мы выполним подключение, мы отправим
 какое-то сообщение, потом мы получим сообщение (или несколько сообщений)
 Потом мы должны соединение закрыть (и КМ поможет это сделать)
 
3. Получаем какой-то ответ, печатаем и запускаем функцию клиента"""