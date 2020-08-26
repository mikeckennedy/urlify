# URLify

A simple macOS app to create valid file and url names from clipboard text.

![](readme_resources/screenshot.png)

## Introduction

If you ever need to take text like this:

**Fastest drivers' times**

And convert it to something you could use in a URL or filename, such as:

**fastest-drivers-times**

Then here's a simple macOS menubar app that does text transforms such as these with a single click. It just takes the text in the clipboard and replaces it with a filename friendly version.

## Installation

Just download the latest release .zip file, uncompress it and copy `urlify.app` into your Applications folder. 

Latest release at: [github.com/mikeckennedy/urlify/releases](https://github.com/mikeckennedy/urlify/releases/latest)

If you want URLify to start when you login, 
just [follow these steps](https://www.idownloadblog.com/2015/03/24/apps-launch-system-startup-mac/):

1. Open System Preferences
2. Click Users & Groups
3. Click Login Items
4. Click the ‘+‘ sign and find urlify.app
5. click the Add button

## Launching app

The first time you download the app, macOS may give you a warning that the developer is not verified and it can't run. You're welcome to heed that warning, but if you trust it enough, right-click and choose open rather than double-clicking it and then you'll get a prompt where you can run anyway.

After running once, macOS will allow it to run without complaining afterwards.

## Building locally

If you want to build the app from source, it's pretty standard Python:

```bash
# Create and activate a virtual environment
$ pip install -r requirements.txt
$ python build_app.py py2app 
```

The output `.app` file will be the `dist` folder.