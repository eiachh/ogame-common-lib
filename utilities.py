from threading import Timer
from common_lib.const import constants

class RepeatedTimer(object):
    def __init__(self, intervalFunc, function, *args, **kwargs):
        self._timer     = None
        self.getIntervalFunc   = intervalFunc
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.getIntervalFunc(), self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

class utilities:
    def isPrerequisiteMet(ogameID, requestData):
        directPrerequisite = constants.prerequisitesDict[ogameID]

        for constructablePrereq in  directPrerequisite['constructable']:
            requiredBuildingID = constructablePrereq['buildingID']
            requiredBuildingLevel = constructablePrereq['buildingLevel']
            if(requiredBuildingID != -1):
                currentBuildingLevel = requestData['facilityLevels'][constants.convertOgameIDToAttrName(requiredBuildingID)]
                if(requiredBuildingID != -1 and currentBuildingLevel < requiredBuildingLevel):
                    return False 

        for researchablePrereq in  directPrerequisite['researchable']:
            requiredResearchID = researchablePrereq['researchID']
            requiredResearchLevel = researchablePrereq['researchLevel']
            if(requiredResearchID != -1):
                currentResearchLevel  = requestData['researchLevels'][constants.convertOgameIDToAttrName(requiredResearchID)]
                if(requiredResearchID != -1 and currentResearchLevel < requiredResearchLevel):
                    return False
        return True

    def getResourceSumInUnitPrice(priceJson, metalUnitPrice = 1, crystalUnitPrice = 2, deuUnitPrice = 3):
        sum = 0
        sum += metalUnitPrice * priceJson['Metal']
        sum += crystalUnitPrice * priceJson['Crystal']
        sum += deuUnitPrice * priceJson['Deuterium']
        return sum

    def getEnergyConsumption(levelOfBuilding, attrNameOfBuilding):
        if(attrNameOfBuilding == constants.ATTR_NAME_OF_METAL_MINE or attrNameOfBuilding == constants.ATTR_NAME_OF_CRYSTAL_MINE):
            return round(10*levelOfBuilding*1.1**levelOfBuilding) - round(10*(levelOfBuilding-1)*1.1**(levelOfBuilding-1))
        elif(attrNameOfBuilding == constants.ATTR_NAME_OF_DEU_MINE):
            return round(20*levelOfBuilding*1.1**levelOfBuilding) - round(20*(levelOfBuilding-1)*1.1**(levelOfBuilding-1))
        return -1
