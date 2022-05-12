__version__ = "0.0.1"
__author__ = "VarMonke"
__copyright__ = "Copyright (c) 2022 - Present  VarMonke"

import asyncio
import random

from typing import List, Literal, Optional, Tuple, Dict, Any, Union
import platform

import aiohttp

from thino.abc import BaseObject


class Client:
    def __init__(self):
        self.BASE_URL = "https://thino.pics/api/v1"
        self.ENDPOINTS = ["tomboy", "neko", "femboy", "porn", "hentai", "thighs"]
        self.session = None
        self.started = False

    async def __get(self, endpoint: Optional[str] = None):
        if self.started == False:
            await self.start()
            self.started = True
        if endpoint not in self.ENDPOINTS:
            raise ValueError(
                f"{endpoint} is not a valid endpoint, please use one of {self.ENDPOINTS}"
            )
        if endpoint is None:
            endpoint = random.choice(self.ENDPOINTS)
        async with self.session.get(f"{self.BASE_URL}/{endpoint}") as response:  # type: ignore
            return BaseObject(await response.json(), endpoint)

    async def start(self):
        self.session = aiohttp.ClientSession(
            headers={
                "User-Agent": f"Thino-Client @ {__version__}/ Python/{platform.python_version()}/ aiohttp/{aiohttp.__version__} PS: VarMonke is cute"
            }
        )

    async def tomboy(self) -> BaseObject:
        return await self.__get("tomboy")

    async def neko(self) -> BaseObject:
        return await self.__get("neko")

    async def femboy(self) -> BaseObject:
        return await self.__get("femboy")

    async def thighs(self) -> BaseObject:
        return await self.__get("thighs")

    async def porn(self) -> BaseObject:
        return await self.__get("porn")

    async def hentai(self) -> BaseObject:
        return await self.__get("hentai")

    async def close(self) -> None:
        await self.session.close() #type: ignore