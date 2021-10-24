import isystem.connect as ic
import os
import time

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
#workspaceCtrl = ic.CWorkspaceController(cmgr)

debugCtrl.download()
#debugCtrl.setBP("main")
debugCtrl.runUntilFunction("main")
debugCtrl.run()
time.sleep(5)
debugCtrl.stop()