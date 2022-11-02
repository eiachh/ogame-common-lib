from common_lib.const import constants

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