"""
Setup File for the Logger Package
"""
from setuptools import setup, find_packages

setup(
    name='logger',
    version='0.1',
    description='Logger Python Package allows you to log to the terminal',
    packages=find_packages(include=['logger', 'logger.*'])
)
