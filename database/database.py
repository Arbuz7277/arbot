# database/database.py

import aiosqlite
from contextlib import asynccontextmanager
from typing import Any, AsyncIterator

from config import Config


class Database:
    _instance: "Database | None" = None
    _conn: aiosqlite.Connection | None = None

    def __new__(cls) -> "Database":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    async def connect(self) -> aiosqlite.Connection:
        if self._conn is None:
            conn = await aiosqlite.connect(Config.db_path)
            conn.row_factory = aiosqlite.Row
            await conn.execute("PRAGMA journal_mode=WAL")
            await conn.execute("PRAGMA foreign_keys=ON")
            self._conn = conn
        return self._conn

    async def close(self) -> None:
        if self._conn is not None:
            await self._conn.close()
            self._conn = None

    @property
    def conn(self) -> aiosqlite.Connection:
        if self._conn is None:
            raise RuntimeError("connection is not open")
        return self._conn


    async def __aenter__(self) -> "Database":
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        if exc_type:
            await self.rollback()
        else:
            await self.commit()

    @asynccontextmanager
    async def cursor(self) -> AsyncIterator[aiosqlite.Cursor]:
        cur = await self.conn.cursor()
        try:
            yield cur
        finally:
            await cur.close()


    async def execute(
        self,
        sql: str,
        parameters: tuple | list = (),
    ) -> aiosqlite.Cursor:
        return await self.conn.execute(sql, parameters)

    async def executemany(
        self,
        sql: str,
        parameters: list[tuple],
    ) -> aiosqlite.Cursor:
        return await self.conn.executemany(sql, parameters)

    async def commit(self) -> None:
        if self._conn is not None:
            await self._conn.commit()

    async def rollback(self) -> None:
        if self._conn is not None:
            await self._conn.rollback()


    async def fetch_one(
        self,
        sql: str,
        parameters: tuple | list = (),
    ) -> dict[str, Any] | None:
        async with self.cursor() as cur:
            await cur.execute(sql, parameters)
            row = await cur.fetchone()
            return dict(row) if row else None

    async def fetch_all(
        self,
        sql: str,
        parameters: tuple | list = (),
    ) -> list[dict[str, Any]]:
        async with self.cursor() as cur:
            await cur.execute(sql, parameters)
            rows = await cur.fetchall()
            return [dict(row) for row in rows]

    async def fetch_val(
        self,
        sql: str,
        parameters: tuple | list = (),
        default: Any = None,
    ) -> Any:
        async with self.cursor() as cur:
            await cur.execute(sql, parameters)
            row = await cur.fetchone()
            return row[0] if row else default


db = Database()
