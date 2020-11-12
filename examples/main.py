from xCore import xCore
from xSG33 import xSG33

SG33 = xSG33()

while True:
    if SG33.dataAvailable() == True:
        SG33.getAlgorithmResults()

        print(SG33.getTVOC())
        print(SG33.getCO2())
    xCore.sleep(1000)