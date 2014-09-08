import asyncio
from aiozmq import rpc


class RPCClient(object):
    """
    """

    def __init__(self, uri):
        """
        """

        self.uri = uri
        
    @asyncio.coroutine
    def __async_call(self, function_name, *args):
        """
        """
        client = yield from rpc.connect_rpc(connect=self.uri)
        result = yield from client.call.__getattr__(function_name)(*args)
        return result

    def call(self, function_name, *args):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            self.__async_call(
                function_name,
                *args
            )
        )
