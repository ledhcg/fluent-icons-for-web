##Terminal

#Install python
pip install beautifulsoup4
pip install requests

#Pull icons from microsoft
python getSVGs.py

#url: https://github.com/microsoft/fluentui-system-icons/blob/master/icons_filled.md
#folder: assets

#Create font
npm install
fantasticon sources -o fonts -n fluent-icons-for-web -g scss css json -p fiw

https://yunusozcan.medium.com/how-to-create-icon-font-like-font-awesome-ce32ea7c7385

#FIX

1. "npm\fantasticon.ps1 cannot be loaded because running scripts is disabled on this system."
   This could be due to the current user having an undefined ExecutionPolicy.

In PowerShell as Administrator, you could try the following:

```sh
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```
