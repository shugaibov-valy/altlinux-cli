import asyncio
import json

from aiohttp import ClientSession

p10_url = "https://rdb.altlinux.org/api/export/branch_binary_packages/p10"
sisyphus_url = "https://rdb.altlinux.org/api/export/branch_binary_packages/sisyphus"


async def parser_data(session: ClientSession, url: str, file_path: str):
    async with session.get(url=url) as response:
        data_json = await response.json()
        with open(file_path, "w") as f:
            json.dump(data_json, f)


async def main():
    async with ClientSession() as session:
        tasks = []
        tasks.append(
            asyncio.create_task(parser_data(session, p10_url, "files/p10.json"))
        )
        tasks.append(
            asyncio.create_task(
                parser_data(session, sisyphus_url, "files/sisyphus.json")
            )
        )

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
