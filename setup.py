from setuptools import setup
import os
import re 

# get_version and conditional adding of pytest-runner
# are taken from 
# https://github.com/mark-adams/pyjwt/blob/b8cc504ee09b4f6b2ba83a3db95206b305fe136c/setup.py

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    with open(os.path.join(package, '__init__.py'), 'rb') as init_py:
        src = init_py.read().decode('utf-8')
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", src).group(1)

version = get_version('ParticleDataTool')

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    long_description = readme.read()


def parse_requirements(req_file):
    with open(req_file) as f:
        reqs = []
        for r in f.readlines():
            if not r.startswith("http"):
                reqs.append(r)
            elif ";" in r:
                continue # FIXME: find better solution
                #data = r.split(";")       
                #reqs.append(data[0]) 
        return reqs

try:
    requirements = parse_requirements("requirements.txt")
except Exception as e:
    print ("Failed parsing requiremnts, installing dummy requirements...")
    requirements = ['numpy>=1.9.0']

setup(name='ParticleDataTool',
      version=version,
      description='This single Python module around an XML data file provides some convinient functions for people working with (physical) particles',
      #long_description='Manages bookkeeping for different simulation datasets, developed for the use with IceCube data',
      long_description=long_description,
      author='Anatoli Fedynitch',
      author_email="",
      url='https://github.com/achim1/ParticleDataTool',
      install_requires=requirements, 
      license="MIT",
      #cmdclass={'install': full_install},
      platforms=["Ubuntu 14.04","Ubuntu 16.04", "Ubuntu 16.10", "SL6.1"],
      classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Scientific/Engineering :: Physics"
              ],
      keywords=["hep", "particle physics"],
      packages=['ParticleDataTool'],
      package_data={'ParticleDataTool': ["ParticleData.xml"]}
      )
