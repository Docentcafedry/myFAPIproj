from ..settings import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class DBHelper:
    def __init__(self, url: str, echo: bool):
        self.connection = create_async_engine(url=url, echo=echo)
        self.session = async_sessionmaker(
            bind=self.connection,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


db_helper = DBHelper(
    url=settings.url,
    echo=settings.echo,
)
