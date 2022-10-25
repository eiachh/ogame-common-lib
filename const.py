class constants:
    #FOR BUILDING MANAGER    
    METAL_MINE = 1
    CRYSTAL_MINE = 2
    DEU_MINE = 3
    SOLAR_PLANT = 4
    FUSION_REACTOR = 12
    SOLAR_SATELLITE = 212
    METAL_STORAGE = 22
    CRYSTAL_STORAGE = 23
    DEU_STORAGE = 24

    #Facilities
    ROBOT_FACTORY = 14
    SHIPYARD = 21
    RESEARCH_LAB = 31
    NANITE_FACTORY = 15
    TERRAFORMER = 33
    MISSILE_SILO = 44

    #Research
    ENERGY_TECH = 113
    LASER_TECH = 120
    ION_Tech = 121
    HYPER_SPACE_TECH = 114
    PLASMA_TECH = 122
    COMBUSTION_DRIVE = 115
    IMPULSE_DRIVE = 117
    HYPERSPACE_DRIVE = 118
    SPY_TECH = 106
    COMPUTER_TECH = 108
    ASTROPHYSICS = 124
    INT_GAL_RESEARCH = 123
    GRAVITON_TECH = 199

    WEAPON_TECH = 109
    SHIELD_TECH = 110
    ARMOUR_TECH = 111

    #Resource buildings
    ATTR_NAME_OF_METAL_MINE = 'MetalMine'
    ATTR_NAME_OF_CRYSTAL_MINE = 'CrystalMine'
    ATTR_NAME_OF_DEU_MINE = 'DeuteriumSynthesizer'
    ATTR_NAME_OF_SOLAR_PLANT = 'SolarPlant'
    ATTR_NAME_OF_FUSION_REACTOR = 'FusionReactor'
    ATTR_NAME_OF_SOLAR_SATELLITE = 'SolarSatellite'
    ATTR_NAME_OF_METAL_STORAGE = 'MetalStorage'
    ATTR_NAME_OF_CRYSTAL_STORAGE = 'CrystalStorage'
    ATTR_NAME_OF_DEU_STORAGE = 'DeuteriumTank'

    #Facilities
    ATTR_NAME_OF_ROBOT_FACTORY = 'RoboticsFactory'
    ATTR_NAME_OF_SHIPYARD = 'Shipyard'
    ATTR_NAME_OF_RESEARCH_LAB = 'ResearchLab'
    ATTR_NAME_OF_NANITE_FACTORY = 'NaniteFactory'
    ATTR_NAME_OF_TERRAFORMER = 'Terraformer'
    ATTR_NAME_OF_MISSILE_SILO = 'MissileSilo'

    #Researches
    ATTR_NAME_OF_ENERGY_TECH = 'EnergyTechnology'
    ATTR_NAME_OF_LASER_TECH = 'LaserTechnology'
    ATTR_NAME_OF_ION_Tech = 'IonTechnology'
    ATTR_NAME_OF_HYPER_SPACE_TECH = 'HyperspaceTechnology'
    ATTR_NAME_OF_PLASMA_TECH = 'PlasmaTechnology'
    ATTR_NAME_OF_COMBUSTION_DRIVE = 'CombustionDrive'
    ATTR_NAME_OF_IMPULSE_DRIVE = 'ImpulseDrive'
    ATTR_NAME_OF_HYPERSPACE_DRIVE = 'HyperspaceDrive'
    ATTR_NAME_OF_SPY_TECH = 'EspionageTechnology'
    ATTR_NAME_OF_COMPUTER_TECH = 'ComputerTechnology'
    ATTR_NAME_OF_ASTROPHYSICS = 'Astrophysics'
    ATTR_NAME_OF_INT_GAL_RESEARCH = 'IntergalacticResearchNetwork'
    ATTR_NAME_OF_GRAVITON_TECH = 'GravitonTechnology'
    ATTR_NAME_OF_WEAPON_TECH = 'WeaponsTechnology'
    ATTR_NAME_OF_SHIELD_TECH = 'ShieldingTechnology'
    ATTR_NAME_OF_ARMOUR_TECH = 'ArmourTechnology'

    prerequisitesDict = {
        SHIPYARD : 
        {'constructable' : 
            {'buildingID': ROBOT_FACTORY, 'buildingLevel': 2},
        'researchable' : 
            {'researchID' : -1, 'researchLevel' : -1}
        },
        ROBOT_FACTORY : 
        {'constructable' : 
            {'buildingID': -1, 'buildingLevel': -1},
        'researchable' : 
            {'researchID' : -1, 'researchLevel' : -1}
        },
        COMBUSTION_DRIVE : 
        {'constructable' : 
            {'buildingID': RESEARCH_LAB, 'buildingLevel': 1},
        'researchable' : 
            {'researchID' : ENERGY_TECH, 'researchLevel' : 1}
        },
        ENERGY_TECH : 
        {'constructable' : 
            {'buildingID': RESEARCH_LAB, 'buildingLevel': 1},
        'researchable' : 
            {'researchID' : -1, 'researchLevel' : -1}
        }
    }

    def convertOgameIDToAttrName(ogameID):
        if(ogameID == 1):
            return constants.ATTR_NAME_OF_METAL_MINE
        if(ogameID == 2):
            return constants.ATTR_NAME_OF_CRYSTAL_MINE
        if(ogameID == 3):
            return constants.ATTR_NAME_OF_DEU_MINE
        if(ogameID == 4):
            return constants.ATTR_NAME_OF_SOLAR_PLANT
        if(ogameID == 12):
            return constants.ATTR_NAME_OF_FUSION_REACTOR
        if(ogameID == 212):
            return constants.ATTR_NAME_OF_SOLAR_SATELLITE
        if(ogameID == 22):
            return constants.ATTR_NAME_OF_METAL_STORAGE
        if(ogameID == 23):
            return constants.ATTR_NAME_OF_CRYSTAL_STORAGE
        if(ogameID == 24):
            return constants.ATTR_NAME_OF_DEU_STORAGE

    def getPrerequisiteOf(ogameID):
        constructibleId = -1
        constructibleLevel = -1
        researchId = -1
        researchLevel = -1


        return {'constructible' : 
                    {'id' : constructibleId, 'level': constructibleLevel}, 
                'research' : 
                    {'id' : researchId, 'level': researchLevel}}

    def getResourceSumInUnitPrice(priceJson):
        sum = 0
        sum += 1 * priceJson['Metal']
        sum += 2 * priceJson['Crystal']
        sum += 3 * priceJson['Deuterium']
        return sum

print(constants.getPrerequisiteOf(2))