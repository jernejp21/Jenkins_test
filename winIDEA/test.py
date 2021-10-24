import isystem.connect as ic
import os
import time
import sys

folderPath = os.path.abspath(os.path.curdir)
winIDEAPath = os.path.join(folderPath, "Jenkins_iC5000.xjrf")

print(winIDEAPath)

cmgr = ic.ConnectionMgr()
cmgr.connectMRU(winIDEAPath)
ideCtrl = ic.CIDEController(cmgr)
debugCtrl = ic.CDebugFacade(cmgr)
#loaderCtrl = ic.CLoaderController(cmgr)
#dataCtrl = ic.CDataController2(cmgr)
#projCtrl = ic.CProjectController(cmgr)
workspaceCtrl = ic.CWorkspaceController(cmgr)

sys.stdout.write("Downloading file...\n")
debugCtrl.download()
debugCtrl.runUntilFunction("main")
sys.stdout.write("Stopped at main for 5 s.\n")
time.sleep(5)
debugCtrl.run()
debugCtrl.stop()
workspaceCtrl.closeDiscard()
cmgr.disconnect(ic.IConnect.dfCloseServerUnconditional, ic.IConnect.dfCloseAutoSaveNone)
