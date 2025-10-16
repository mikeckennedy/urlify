# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project uses [Calendar Versioning](https://calver.org/) with the format YYYY.MM.DD.

## [Unreleased]

### Added
- 

### Changed
- 

### Deprecated
- 

### Removed
- 

### Fixed
-

### Security
- 

---

## [2025.10.16]

### Added
- New CLI functionality with full command-line interface support
  - Files: `cli.py`, `WARP.md`
- Comprehensive unit tests for converter functionality
  - Files: `tests/test_converter.py`, `pytest.ini`
- Development dependencies management with piptools
  - Files: `requirements-development.piptools`, `requirements-development.txt`
- Colored help output for better CLI user experience
  - Files: `cli.py`
- Feature to remove query strings from URLs
  - Files: `app.py`, `converter.py`
- Ruff configuration for consistent code formatting
  - Files: `ruff.toml`

### Changed
- Migrated from setup.py to pyproject.toml for modern Python packaging
  - Files: `pyproject.toml`, removed `setup.py`
- Updated minimum Python version requirement to 3.10
  - Files: `pyproject.toml`, `cli.py`
- Made clipboard copy the default behavior in CLI
  - Files: `cli.py`
- Improved apostrophe handling in URL conversion (e.g., "let's go" → "lets-go")
  - Files: `converter.py`
- Reorganized project structure with tests in dedicated folder
  - Files: moved `test_converter.py` to `tests/test_converter.py`
- Updated dependencies: pyobjc, pyperclip, setuptools to latest compatible versions
  - Files: `requirements.txt`
- Enhanced README with comprehensive CLI documentation
  - Files: `README.md`
- Applied ruff formatting across codebase
  - Files: `app.py`, `cli.py`, `converter.py`, `build_app.py`
- Improved build configuration for latest macOS compatibility
  - Files: `setup.py`, `requirements.piptools`, `requirements.txt`

### Removed
- Removed shebang from Python files per project standards
  - Files: `cli.py`
- Removed setup.py in favor of pyproject.toml
  - Files: `setup.py`
- Cleaned up .idea configuration files
  - Files: `.idea/inspectionProfiles/profiles_settings.xml`, `.idea/modules.xml`, `.idea/vcs.xml`, `.idea/ruff.xml`

### Fixed
- Improved compatibility with latest macOS builds
  - Files: `setup.py`, `requirements.txt`

### Notes
- This release represents a major enhancement with the addition of CLI functionality
- Project now follows modern Python packaging standards with pyproject.toml
- Enhanced testing infrastructure with comprehensive test coverage
- Breaking change: Minimum Python version is now 3.10

---

## Template for Future Entries

<!--
## [YYYY.MM.DD]

### Added
- New features or capabilities
- Files: `path/to/new/file.ext`, `another/file.ext`

### Changed
- Modifications to existing functionality
- Files: `path/to/modified/file.ext` (summary if many files)

### Deprecated
- Features that will be removed in future versions
- Files affected: `path/to/deprecated/file.ext`

### Removed
- Features or files that were deleted
- Files: `path/to/removed/file.ext`

### Fixed
- Bug fixes and corrections
- Files: `path/to/fixed/file.ext`

### Security
- Security patches or vulnerability fixes
- Files: `path/to/security/file.ext`

### Notes
- Additional context or important information
- Major dependencies updated
- Breaking changes explanation
-->
