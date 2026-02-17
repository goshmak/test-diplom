from celery import Celery
from sqlalchemy.orm import Session
celery = Celery('tasks', broker='redis://redis')

@celery.task
def send_notification(user_id: int, event: str, data: dict, db: Session):
    template = db.query(Template).filter_by(name=event).first()
    if template:
        rendered = jinja.from_string(template.body).render(**data)
        # Сохранить уведомление и опубликовать в Redis/WebSocket
        redis.publish(f"notify:{user_id}", rendered)