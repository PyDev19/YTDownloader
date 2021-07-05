; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "YT Downloader"
#define MyAppVersion "3.0"
#define MyAppPublisher "PyDev19"
#define MyAppURL "https://github.com/PyDev19/YTDownloader"
#define MyAppExeName "main.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{FB8C4045-059D-4F33-9718-6091F01A3528}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=C:\Users\User\Desktop\LICENSE.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputDir=C:\Users\User\Desktop\PythonProjects\Personal Projects\YTDownloader
OutputBaseFilename=YTDownloader-3.0-windows
SetupIconFile=C:\Users\User\Desktop\PythonProjects\Personal Projects\YTDownloader\icons\icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\User\Desktop\PythonProjects\Personal Projects\YTDownloader\installer_files\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\PythonProjects\Personal Projects\YTDownloader\installer_files\icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\PythonProjects\Personal Projects\YTDownloader\installer_files\main.qss"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\PythonProjects\Personal Projects\YTDownloader\installer_files\menu_bar.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\PythonProjects\Personal Projects\YTDownloader\installer_files\menu_bar.qss"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\PythonProjects\Personal Projects\YTDownloader\installer_files\python3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\PythonProjects\Personal Projects\YTDownloader\installer_files\python39.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\User\Desktop\PythonProjects\Personal Projects\YTDownloader\installer_folders\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:ProgramOnTheWeb,{#MyAppName}}"; Filename: "{#MyAppURL}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
