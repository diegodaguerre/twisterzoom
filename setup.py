from setuptools import setup, find_packages

setup(
    name = 'twisterzoom',
    version = '0.1',
    packages = find_packages(),
    scripts = ['bin/twisterzoom-ctl'],
)
