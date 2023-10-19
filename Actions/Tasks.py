import asyncpg


async def connect():
    conn = await asyncpg.connect(host='localhost', user="postgres", password="working", database="BusinessAssistent")
    return conn


async def add_task(title: str):
    conn = await connect()
    query = "INSERT INTO Tasks(title) VALUES($1), title RETURNING *"
    task = await conn.fetchrow(query, title)
    return task
