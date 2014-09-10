import asyncio
from aiozmq import rpc


class RPCClient(object):
    """
    High level AIOZMQ rpc client
    """

    def __init__(self, uri, timeout=10):
        """
        Args:
          uri: URI of the RPC server.
          timeout (int) -- optional: Connection timeout in seconds (default=10)
        """

        self.uri = uri
        self.timeout = timeout
        
    @asyncio.coroutine
    def __async_call(self, function_name, *args, **kwargs):
        """
        Runs the rpc call in coroutine.
        """

        client = yield from rpc.connect_rpc(
            connect=self.uri,
            timeout=self.timeout
        )
        result = yield from client.call.__getattr__(
            function_name
        )(*args, **kwargs)

        return result

    def call(self, function_name, *args, **kwargs):
        """
        Runs the remote function on the event loop.

        Agrs:
            function_name: Name of the remote function.
            args -- optional: positional arguments that will passed
              to the remote function.
            kwargs --optional: keyword arguments that will be passed
              to the remote function.

        Returns:
          Returned result from the remote excution of the function.
        """

        loop = asyncio.get_event_loop()
        return loop.run_until_complete(
            self.__async_call(function_name, *args, **kwargs)
        )

    def help(self, function_name):
        """
        Get some information about how to use the remote function.

        Args:
          function_name: Name of the remote function.

        Prints:
           Docstring of the remote function.
        """
        loop = asyncio.get_event_loop()
        print(
            loop.run_until_complete(
                self.__async_call("help", function_name)
            )
        )
