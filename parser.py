import asyncio
import json

from aiohttp import ClientSession

from consts import P10_FILE_PATH, SISYPHUS_FILE_PATH


async def parser_data_url(session: ClientSession, url: str, file_path: str):
    async with session.get(url=url) as response:
        data_json = await response.json()
        with open(file_path, "w") as f:
            json.dump(data_json, f)


async def create_tasks_parse(p10_url: str, sisyphus_url: str):
    async with ClientSession() as session:
        tasks = []
        tasks.append(
            asyncio.create_task(parser_data_url(session, p10_url, P10_FILE_PATH))
        )
        tasks.append(
            asyncio.create_task(
                parser_data_url(session, sisyphus_url, SISYPHUS_FILE_PATH)
            )
        )

        await asyncio.gather(*tasks)
