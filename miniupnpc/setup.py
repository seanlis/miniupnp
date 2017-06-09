#! /usr/bin/python
# vim: tabstop=8 shiftwidth=8 expandtab
# $Id: setup.py,v 1.9 2012/05/23 08:50:10 nanard Exp $
# the MiniUPnP Project (c) 2007-2014 Thomas Bernard
# http://miniupnp.tuxfamily.org/ or http://miniupnp.free.fr/
#
# python script to build the miniupnpc module under unix
#
# replace libminiupnpc.a by libminiupnpc.so for shared library usage
from skbuild import setup
from setuptools import Extension
from distutils import sysconfig
from distutils.util import get_platform

sysconfig.get_config_vars()["OPT"] = ''
sysconfig.get_config_vars()["CFLAGS"] = ''

platform = get_platform()
lib = ['miniupnpc']
if platform.startswith('win'):
    lib += ['ws2_32', 'iphlpapi']

setup(name="miniupnpc",
      version=open('VERSION').read().strip(),
      author='Thomas BERNARD',
      author_email='miniupnp@free.fr',
      license=open('LICENSE').read(),
      url='http://miniupnp.free.fr/',
      description='miniUPnP client',
      ext_modules=[
         Extension(name="miniupnpc", sources=["miniupnpcmodule.c"],
                   #extra_objects=["libminiupnpc.a"])
                   #library_dirs=['build/cmakevc'],
                   library_dirs=['_skbuild/cmake-install/lib'],
                   libraries=lib)
      ],
      install_requires=[
          'cmake', 'scikit-build'
      ],
      cmake_args=['-DUPNPC_BUILD_SHARED=FALSE']
)

