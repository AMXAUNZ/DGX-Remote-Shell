# -*- mode: python -*-
a = Analysis(['dgx_rs.py'],
             pathex=['C:\\Users\\jim.maciejewski\\Documents\\dgx_remote_shell\\dgx_remote_shell\\dgx_remote_shell'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
##### include mydir in distribution #######
def extra_datas(icon):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % icon, files)
    extra_datas = []
    for f in files:
        extra_datas.append((f, f, 'icon'))

    return extra_datas
###########################################
a.datas += extra_datas('icon')
a.datas += extra_datas('store')
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='DGX_Remote_Shell.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False,
          icon='icon/dgx_rs.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='DGX Remote Shell')
