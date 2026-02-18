import redis
from fastapi import FastAPI

app = FastAPI()
# Подключаемся к Redis (по умолчанию localhost:6379)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.get("/get-data")
async def get_data(key: str):
    # Проверяем, есть ли данные в кэше Redis
    cached_value = r.get(key)
    if cached_value:
        return {"source": "cache", "data": cached_value}

    # Если данных нет, имитируем "тяжелую" работу
    expensive_data = f"Данные для {key}"

    # Сохраняем в Redis на 60 секунд
    r.setex(key, 60, expensive_data)

    return {"source": "database", "data": expensive_data}