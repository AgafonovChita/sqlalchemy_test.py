import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config import Config, load_config

from db.models import Base, ChannelMember


async def main():
    config: Config = load_config()
    engine = create_async_engine(
        f"postgresql+asyncpg://{config.db.user}:{config.db.password}@{config.db.host}/{config.db.db_name}",
        future=True, echo=True)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    # model MemberChannel
    request = ChannelMember(
        request_id=43562523000,
        user_id=43562523,
        user_name="Ivan Ivanov",
        user_position="HR-manager",
        invite_link="tg://",
        user_status="kicked")

    async with async_session() as session:
        await session.merge(request)
        await session.merge(ChannelMember(1342525000, 1342525, "Alex Petrov", "DevOps", "tg://", None))
        await session.commit()


asyncio.get_event_loop().run_until_complete(main())
