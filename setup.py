import io
import os
import re

from setuptools import setup

"""
Usage:
    python setup.py py2app
"""


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type("")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())


APP = ["app.py"]
DATA_FILES = []
OPTIONS = {}

setup(
    name="urlify",
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
    url="https://github.com/mikeckennedy/urlify",
    description="A simple macOS app to create file and url names from clipboard text.",
    long_description=read("README.md"),
    license="MIT",
    author="Michael Kennedy",
    author_email="michael@talkpython.fm",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
