from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

class DatabaseHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False,
        echo_pool: bool = False,
        pool_size: int = 5,
        max_overflow: int = 10,
    ):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False, # выключаем потому что работаем асинхронно
            autocommit=False,
            expire_on_commit=False,
        )
    async def dispose(self):
        await self.engine.dispose()