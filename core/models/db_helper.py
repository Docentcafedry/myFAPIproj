from ..settings import settings
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)
from asyncio import current_task
from sqlalchemy.ext.asyncio import AsyncSession


class DBHelper:
    def __init__(self, url: str, echo: bool):
        self.connection = create_async_engine(url=url, echo=echo)
        self.session = async_sessionmaker(
            bind=self.connection,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    # def get_scoped_session():
    #     session = async_scoped_session(
    #         session_factory=self.session,
    #         scopefunc=current_task
    #     )
    #     return session

    async def session_dependency(self) -> AsyncSession:
        async with self.session.begin() as session:
            yield session
            await session.close()


db_helper = DBHelper(
    url=settings.url,
    echo=settings.echo,
)
