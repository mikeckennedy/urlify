# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

URLify is a macOS menubar application that transforms clipboard text for URL/filename usage. It's built with Python, using the Rumps library for macOS menu bar integration and py2app for application packaging.

## Development Commands

### Environment Setup
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
# Run directly for development/testing - displays menubar icon
python app.py

# The app runs as a background menubar utility
# Use Ctrl+C to stop when running in terminal
```

### Building the Application
```bash
# Build the macOS .app bundle
python build_app.py py2app

# The output urlify.app will be in the dist/ folder
# For distribution: copy dist/urlify.app to Applications folder
```

### Development Maintenance
```bash
# Clean build artifacts
rm -rf build dist *.egg-info

# Update dependencies (if using uv)
uv pip compile requirements.piptools --output-file requirements.txt

# Check current version (defined in app.py)
grep "VERSION =" app.py
```

## Architecture Overview

- **`app.py`** - Main application using Rumps library for macOS menubar integration. Defines the `UrlifyApp` class with menu item callbacks that process clipboard text through converter functions and display notifications.

- **`converter.py`** - Pure text transformation functions (`to_url_style`, `strip`, `lowercase`, `uppercase`, `excel_friendly`, `capitalize_first`, `capitalize_all`, `strip_querystring_from_url`). Each function takes a string and returns the transformed version.

- **`build_app.py` & `setup.py`** - py2app configuration for packaging the Python application into a macOS .app bundle. Includes icon file, background app settings (`LSUIElement: True`), and package dependencies.

- **`requirements.txt`** - Lock file generated from `requirements.piptools` using uv/pip-compile for reproducible environments. Key dependencies: rumps (macOS integration), pyperclip (clipboard access), colorama (terminal colors).

- **Clipboard Workflow** - App monitors clipboard via pyperclip, applies text transformations, updates clipboard with results, and shows macOS notifications for feedback.

## Installation & Usage Notes

### For Testing Built Applications
- Download latest release .zip from GitHub releases
- Extract and copy `urlify.app` to `/Applications`
- First run: macOS will show "unverified developer" warning - right-click app and select "Open" to bypass
- Optional: Add to Login Items in System Preferences > Users & Groups for auto-launch

### Menu Functions
- **🌟 URLify Text**: Converts text to URL-friendly format (removes special chars, converts spaces to hyphens, lowercase)
- **🌐 Remove query string**: Strips everything after `?` in URLs
- **↹ Trim Text**: Removes leading/trailing whitespace
- **↧/↥ Case conversion**: Lowercase/uppercase transformation
- **🧾 Excel friendly**: Extracts only numbers and periods
- **Aa/Aa Aa Capitalize**: First word or all words capitalization
