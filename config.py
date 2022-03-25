from dataclasses import dataclass
from os import getenv
from pydantic import BaseModel
import dotenv

dotenv.load_dotenv()


class Bot(BaseModel):
    token: str


class DB(BaseModel):
    host: str
    db_name: str
    user: str
    password: str
    port: str


class Config(BaseModel):
    bot: Bot
    db: DB


def load_config():
    return Config(
        bot=Bot(token=getenv("BOT_TOKEN")),
        db=DB(
            host=getenv("DB_HOST"),
            db_name=getenv("DB_NAME"),
            user=getenv("DB_USER"),
            password=getenv("DB_PASS"),
            port=getenv("DB_PORT")
        )
    )
