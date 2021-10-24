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
sys.stdout.flush()
debugCtrl.download()
debugCtrl.run()
sys.stdout.write("Run main for 5 s. LED pulse 1000 ms.\n")
sys.stdout.flush()
time.sleep(5)
debugCtrl.stop()
debugCtrl.modify(ic.IConnectDebug.fMonitor, "delayTime", "100")
debugCtrl.run()
sys.stdout.write("LED pulse 100 ms.\n")
workspaceCtrl.closeDiscard()
cmgr.disconnect(ic.IConnect.dfCloseServerUnconditional, ic.IConnect.dfCloseAutoSaveNone)
