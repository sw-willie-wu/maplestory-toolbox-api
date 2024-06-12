import asyncio
from typing import AsyncGenerator, Any

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine

from config import SETTINGS
from db.models import BaseModel


class DBInitializer():
    def __init__(self) -> None:
        do_echo: bool = True if SETTINGS.Mode == 'DEV' else False
        self.db_engine: AsyncEngine = create_async_engine(
            str(SETTINGS.Postgres.Dsn),
            pool_size=20,
            max_overflow=10,
            echo=do_echo,
        )
        self.db_session: AsyncSession = async_sessionmaker(
            bind=self.db_engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, Any]:
        async with self.db_session() as session:
            yield session

    async def migrate(self):
        async with self.db_session.begin() as sess:
            await BaseModel.metadata.create_all(
                bind=sess,
                # tables=[GeoType, MetaData, GridRawData, ShapeRawData,],
                checkfirst=True,
            )

    async def close(self):
        await self.db_engine.dispose()


DATABASE = DBInitializer()
