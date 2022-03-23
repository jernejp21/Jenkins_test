import isystem.connect as ic
import os
import time
import sys

folderPath = os.path.abspath(os.path.curdir)
winIDEAPath = os.path.join(folderPath, "Jenkins_iC5000.xjrf")

print(winIDEAPath)

cmgr = ic.ConnectionMgr()
cmgr.connectMRU()
ideCtrl = ic.CIDEController(cmgr)
debugCtrl = ic.CDebugFacade(cmgr)
#loaderCtrl = ic.CLoaderController(cmgr)
#dataCtrl = ic.CDataController2(cmgr)
#projCtrl = ic.CProjectController(cmgr)
workspaceCtrl = ic.CWorkspaceController(cmgr)


debugCtrl.download()
debugCtrl.setBP("main")


