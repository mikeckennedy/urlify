import io
import os
import re

from setuptools import find_packages, setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type('')
    with io.open(filename, mode='r', encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


APP = ['app.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'urlify.icns',
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps', 'pyperclip', 'pyperclip', 'colorama'],
}

setup(
    name='urlify',
    version='2024.10.1',
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    url='https://github.com/mikeckennedy/urlify',
    license='MIT',
    author='Michael Kennedy',
    author_email='michael@talkpython.fm',
    description='A simple macOS app to create file and url names from clipboard text.',
    long_description=read('README.md'),
    packages=find_packages(exclude=('tests',)),
    install_requires=[],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)
