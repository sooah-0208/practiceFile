from fastapi import FastAPI
from kafka import KafkaConsumer
from settings import settings
import threading
from typing import List
from starlette.responses import JSONResponse
from pydantic import EmailStr, BaseModel
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
import asyncio
import json

class EmailModel(BaseModel):
    email: List[EmailStr]
    msg: str
    title: str

conf = ConnectionConfig(
    MAIL_USERNAME = settings.mail_username,
    MAIL_PASSWORD = settings.mail_password,
    MAIL_FROM = settings.mail_from,
    MAIL_PORT = settings.mail_port,
    MAIL_SERVER = settings.mail_server,
    MAIL_FROM_NAME=settings.mail_from_name,
    MAIL_STARTTLS = settings.mail_starttls,
    MAIL_SSL_TLS = settings.mail_ssl_tls,
    USE_CREDENTIALS = settings.use_credentials,
    VALIDATE_CERTS = settings.validate_certs
)

app=FastAPI()

@app.post("/email")
async def simple_send(model: EmailModel) -> JSONResponse:
    html = f"""<h1>{model.title}</h1>
<p>{model.msg}</p>
"""

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=model.dict().get("email"),
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)


def consumer():
    cs = KafkaConsumer(settings.kafka_topic, bootstrap_servers=settings.kafka_server)
    for msg in cs:
        print(msg.value.decode('utf-8'))
        data = json.loads(msg.value.decode("utf-8"))
        model = EmailModel(**data)
        asyncio.run(simple_send(model))

@app.on_event('startup')
def start_consumer():
    thread = threading.Thread(target=consumer, daemon=True)
    thread.start()


@app.get("/")
def read_root():
    return{"msg":"Consumer"}

# @app.get("/start")
# def start():
#     startCousumer()

