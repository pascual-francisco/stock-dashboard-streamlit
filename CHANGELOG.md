# 📦 Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### 🔢 Versioning Guide

Version numbers follow this format: `MAJOR.MINOR.PATCH`
| Type of Change     | Description                                      | Example Version |
|--------------------|--------------------------------------------------|-----------------|
| **PATCH**          | Bug fixes, small tweaks, minor improvements      | `0.1.1`         |
| **MINOR**          | New features that don't break existing code      | `0.2.0`         |
| **MAJOR**          | Breaking changes, big redesigns or overhauls     | `1.0.0`         |

Use `0.x.x` while the project is still in early development. Move to `1.0.0` when it's ready for public release.

## Explanation of Sections
## [Unreleased]: A section for changes you're working on but haven't released yet
### Added: New features
### Changed: Updates or improvements
### Fixed: Bug fixes
### Removed: Features that were taken out
### Notes: Important information

# [0.2.0]
### Added: New features

### Changed: Updates or improvements

### Fixed: Bug fixes

### Removed: Features that were taken out

### Notes: Important information
- These changes are in progress and will be included in version `0.2.0`

## [0.1.2]
### Added
- Load data from Yahoo Finance
- Manual ticker selection
- Period selection
- Custom date range selector
- Interval selection
- Stock Ticker Symbol Selection
- Load Data Button
- Display historical price charts
- Error handling for invalid tickers
- Basic Streamlit interface
### Changed
- N/A
### Fixed
- N/A
### Removed
- `FEAUTRESLOG.md` file
### Tests
- Unit test: valid ticker loads data
- Unit test: invalid ticker triggers error message
- Integration test: chart renders with valid data
- UI test: Streamlit components respond correctly
### Notes
- These changes are in progress and will be included in version `0.1.1`

## [0.1.1] - 2025-10-07
### Added
- `FEATURESLOG.md` file
- `test_main.py` file
- Manual ticker selection using `st.text_input`
- Unit tests for valid and invalid ticker inputs in `test_main.py`
### Changed
- Updated `features_log.md` to reflect completed features and tests
### Fixed: 
- N/A
### Removed: 
- N/A
### Notes
- Chart display and Streamlit layout still pending

## [0.1.0] - 2025-10-04
### Added
- Initial version of the stock dashboard
- `main.py` file


## [0.2.0] - Unreleased  
### Added  
- Multi-asset comparison  
- Export charts to image or CSV  
- Technical indicators: SMA, EMA, RSI  
- Dashboard visual improvements  

### Changed  
- UI layout enhancements for better readability  
- Refactored chart rendering logic for multi-asset support  

### Fixed  
- N/A  

### Removed  
- N/A  

### Tests  
- ⬜ Multi-asset chart rendering  
- ⬜ Export functionality  
- ⬜ Indicator accuracy  
- ⬜ Dashboard responsiveness  
- ⬜ UI consistency  
- ⬜ Error handling  
- ⬜ Performance under load  
- ⬜ Mobile layout test  
- ⬜ API response validation  

### Notes  
- This version introduces advanced analytics and export capabilities. Still under development.

---

## [0.3.0] - Planned  
### Added  
- Save user preferences  
- Basic user authentication  
- External API integration (news, analysis)  
- Dark/light mode toggle  
- Mobile-optimized layout  

### Changed  
- N/A  

### Fixed  
- N/A  

### Removed  
- N/A  

### Tests  
- ⬜ Preference persistence  
- ⬜ Auth flow validation  
- ⬜ API integration test  
- ⬜ Theme toggle behavior  
- ⬜ Mobile layout rendering  
- ⬜ Security checks  
- ⬜ Session management  
- ⬜ Data caching  
- ⬜ Accessibility compliance  
