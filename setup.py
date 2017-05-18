import sys
import platform

from distutils.core import setup
from setuptools import find_packages
from distutils.extension import Extension

import numpy
from Cython.Distutils import build_ext
from Cython.Build import cythonize

if sys.platform == 'darwin':
    # OS X
    version, _, _ = platform.mac_ver()
    parts = version.split('.')
    v1 = int(parts[0])
    v2 = int(parts[1])
    v3 = int(parts[2]) if len(parts) == 3 else None

    if v2 >= 10:
        # More than 10.10
        extra_compile_args=['-I/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/Headers']
    else:
        extra_compile_args=['-I/System/Library/Frameworks/vecLib.framework/Headers']

    ext_modules = [Extension(name='tsne.bh_sne',
                   sources=['tsne/bh_sne_src/quadtree.cpp', 'tsne/bh_sne_src/tsne.cpp', 'tsne/bh_sne.pyx'],
                   include_dirs=[numpy.get_include(), 'tsne/bh_sne_src/'],
                   extra_compile_args=extra_compile_args,
                   extra_link_args=['-Wl,-framework', '-Wl,Accelerate', '-lcblas'],
                   language='c++')]
else:
    extra_link_args = ['-lcblas']
    dist = platform.linux_distribution(full_distribution_name=0)[0]
    redhat_dists = set(["redhat", "fedora", "centos"])
    if dist in redhat_dists:
        extra_link_args = ['-lsatlas']

    # LINUX
    ext_modules = [Extension(name='tsne.bh_sne',
                   sources=['tsne/bh_sne_src/quadtree.cpp', 'tsne/bh_sne_src/tsne.cpp', 'tsne/bh_sne.pyx'],
                   include_dirs=[numpy.get_include(), '/usr/local/include', 'tsne/bh_sne_src/'],
                   library_dirs=['/usr/local/lib'],
                   extra_compile_args=['-msse2', '-O3', '-fPIC', '-w'],
                   extra_link_args=extra_link_args,
                   language='c++')]

ext_modules = cythonize(ext_modules)

with open('requirements.txt') as f:
    required = f.read().splitlines()

# cmdclass = versioneer.get_cmdclass()
# cmdclass['build_ext'] = build_ext

setup(name='barnes-hut-tsne',
      version="0.2.0",
      # cmdclass=versioneer.get_cmdclass(),
      author='Rob Speer',
      author_email='rob@luminoso.com',
      url='https://github.com/rspeer/barnes-hut-tsne',
      description='TSNE implementations for python',
      license='Apache License Version 2.0, January 2004',
      packages=find_packages(),
      ext_modules=ext_modules,
      install_requires=required
)
