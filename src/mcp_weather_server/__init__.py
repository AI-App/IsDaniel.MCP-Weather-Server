from . import server
import asyncio

def main(transport: server.Transport = "stdio"):
    """Main entry point for the package."""
    asyncio.run(server.main(transport=transport))

__all__ = ['main', 'server']
