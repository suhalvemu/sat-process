#!/usr/bin/env python


from setuptools import setup, find_packages
import imp


__version__ = imp.load_source('sprocess.version', 'sprocess/version.py').__version__


setup(
    name='sat-multispectral',
    version=__version__,
    description='Multispectral processing on geospatial raster data',
    packages=find_packages(),
    scripts=['bin/landsat8', 'bin/sentinel2'],
    install_requires=['gippy'],
)
