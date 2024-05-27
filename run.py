import asyncio
import logging
import sys

from core.main import init_bot

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(init_bot())
