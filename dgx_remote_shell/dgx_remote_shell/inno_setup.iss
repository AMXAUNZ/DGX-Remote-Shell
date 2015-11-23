; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "DGX Remote Shell"
#define MyAppVersion "v0.1.2"
#define MyAppPublisher "ItsMagic Software"
#define MyAppURL "http://www.ornear.com/dgx_rs"
#define MyAppExeName "DGX_Remote_Shell.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{F1DA10BA-E531-49FC-A595-CCDA446B7D08}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=C:\Users\jim.maciejewski\Documents\dgx_remote_shell\dgx_remote_shell\dgx_remote_shell\output
OutputBaseFilename=DGX_Remote_Shell_Setup_{#MyAppVersion}
SetupIconFile=C:\Users\jim.maciejewski\Documents\dgx_remote_shell\dgx_remote_shell\dgx_remote_shell\dist\DGX Remote Shell\icon\dgx_rs.ico
Compression=lzma
SolidCompression=yes
UninstallDisplayIcon={app}\icon\dgx_rc.ico

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\jim.maciejewski\Documents\dgx_remote_shell\dgx_remote_shell\dgx_remote_shell\dist\DGX Remote Shell\DGX_Remote_Shell.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\jim.maciejewski\Documents\dgx_remote_shell\dgx_remote_shell\dgx_remote_shell\dist\DGX Remote Shell\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

