import asyncio
from aiozmq import rpc


class RPCClient(object):
    """
    """

    def __init__(self, uri):
        """
        """

        self.uri = uri

    def __getattr__(self, name, *args):
        print("." * 100)
        print(name)
        print("." * 100)
        # callback = self.call(name, *args)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.call(name, *args))
        # loop.close()
        
    @asyncio.coroutine
    def call(self, function_name, *args):
        """
        """
        client = yield from rpc.connect_rpc(connect=self.uri)
        result = yield from client.call.__getattr__(function_name)(*args)
        print(result)
        return result