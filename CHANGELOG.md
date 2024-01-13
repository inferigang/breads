# 🍞 BREADS Changelog

## 2024-01-08
### 1.1.2 🎉
- Added progress bar (executes only in LDAP connection moment)
- Now the time the commands were executed will be displayed for a better report
- Banner can be italic, bold, normal or both (and added the green to the color list)
- Now the banner color match the version text color
- Added 'all_computers' module - Retrive all the computers that can be located on the domain
- Added 'get_obsolete' module - Search for for obsolete operating systems installed on computers
- Added 'trusted_delegate' module - Retrieve all the accounts that has msds-allowedtodelegateto enabled

<br>

## 2024-01-05
### 1.1.1 🎉
- Changed colors from texts
- Changed cmd apperance
- Removed highlighted texts with console.print() from Rich lib
- Fixed typo in mac_aqq_quota.py module
- Added breads demo video in the README.md (thanks asciinema)

<br>

## 2024-01-03
### 1.1.0 🎉
- Added lastLogon and lastLogoff on 'whoami' command
- Added support to convert Windows FileTime to DateTime (thanks to Mostafa-Hamdy-Elgiar) (helpers/filetime_to_date.py)
- Added more 4 banners

<br>

## 2023-12-28
### 1.0.9 🎉
- Improved UAC value context in 'whoami' command
    - '512': 'Enabled - Password Expires'
    - '514': 'Disabled - Password Expires'
    - '66048': "Enabled - Password Doesn't Expires"
    - '66050': "Disabled - Password Doesn't Expires"

<br>

## 2023-12-16
### 1.0.8 🎉
- Added 'maq_acc_quota' command
- Removed unused ldap and json library from modules

<br>

## 2023-12-14
### 1.0.7 🎉
- Added 'kerberoasting' command
- Added color 'magenta' to banner generation
- Added desc to all modules from enum and user folder

<br>

## 2023-12-09
### 1.0.6 🎉
- Added 'laps' command (ex: laps / laps SRVMACHINENAME)
- Added more information to 'administrators' module file

<br>

## 2023-12-09
### 1.0.5 🎉
- Removed unused code from pass_pol module file
- Added 'whoami' command (ex: whoami Administrator)
- Fixed a bug that 'load_profile' command does not check if .breasd directory exists
- Changed banners ascii arts and added more colors to be used
- Fixed typos in README.md (and added a meme created by a close friend)

<br>

### 1.0.4 💀
> Yes, we don't have the 1.0.4 changelog :/

<br>

## 2023-12-07
### 1.0.3 🎉
- Now is possible to install use BREADS just calling 'breads-ad' bin
- Fixed typo on code
- Added missing __init__.py on handlers and modules/enum directories

<br>

## 2023-12-04 🎉
- First BREADS beta release
