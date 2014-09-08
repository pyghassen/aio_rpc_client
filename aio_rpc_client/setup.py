from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='aio_rpc_client',
      version=version,
      description="Asyncio RPC client",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='asyincio rpc',
      author='Ghassen Telmoudi',
      author_email='ghassen.telmoudi@gmail.com',
      url='https://github.com/pyghassen/aio_rpc_client',
      license='Apache License Version 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "aiozmq",
          "msgpack-python"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
