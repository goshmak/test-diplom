from fastapi import FastAPI, WebSocket, Depends
from redis.asyncio import Redis
import aioredis, jinja2
from celery import Celery

app = FastAPI()
redis = Redis(host='redis', decode_responses=True)
celery = Celery('tasks', broker='redis://redis')

jinja = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

@app.websocket("/ws/{room_id}")
async def websocket(websocket: WebSocket, room_id: str):
    await websocket.accept()
    pubsub = redis.pubsub()
    await pubsub.subscribe(f"chat:{room_id}")
    async for message in pubsub.listen():
        await websocket.send_text(message['data'])

@app.post("/send_message")
async def send_message(sender_id: int, recipient_id: int, content: str):
    # Сохранить в PostgreSQL
    # Опубликовать в Redis
    await redis.publish(f"chat:{recipient_id}", content)
    # Автоуведомление
    send_notification.delay(recipient_id, "new_message", {"sender": sender_id})