;based on template from https://github.com/emesene/emesene
SetCompressor /solid lzma

XPStyle on

Page license
Page directory
Page instfiles

RequestExecutionLevel admin

# set license page
LicenseText ""
LicenseData "LICENSE.txt"
LicenseForceSelection checkbox

Name "GPEC2010 beta4"
;Icon "aui.ico"
OutFile "gpec2010-setup.exe"
InstallDir "$PROGRAMFILES\GPEC"
InstallDirRegKey HKLM "Software\GPEC" "Install_Dir"

Section "Install"  
    SectionIn RO
    SetOutPath $INSTDIR
    File /r dist\*.*
    WriteRegStr HKLM "Software\GPEC" "Install_Dir" "$INSTDIR"
    WriteUninstaller "$INSTDIR\uninstall.exe"
SectionEnd

Section "Shortcuts"
    CreateDirectory "$SMPROGRAMS\GPEC"
    CreateShortCut "$SMPROGRAMS\GPEC\GPEC.lnk" "$INSTDIR\aui.exe" "" "$INSTDIR\aui.exe"
    CreateShortCut "$SMPROGRAMS\GPEC\uninstall.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe"
    ;${lnkX64IconFix} "$SMPROGRAMS\GPEC\uninstall.lnk"
    CreateShortCut "$DESKTOP\GPEC.lnk" "$INSTDIR\aui.exe" "" "$INSTDIR\aui.exe"
    ;${lnkX64IconFix} "$DESKTOP\GPEC.lnk"
SectionEnd

Section "Uninstall"
    Delete "$INSTDIR\uninstall.exe"
    RMDir /r $INSTDIR
    RMDir /r "$PROFILE\GPEC\"
    RMDir /r "$SMPROGRAMS\GPEC"
    Delete "$DESKTOP\GPEC.lnk"
    DeleteRegKey HKLM "Software\GPEC"
SectionEnd