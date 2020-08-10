from setuptools import setup

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
    name="urlify",
    app=APP,
    data_files=DATA_FILES,
    options={
        'py2app': OPTIONS,
    },
    setup_requires=['py2app'],
)
