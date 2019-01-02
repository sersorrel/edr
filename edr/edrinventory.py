# coding= utf-8
from edri18n import _

class EDRInventory(object):

    MATERIALS_LUT = {
        "zinc": {"localized": _(u"Zinc"), "category": "raw", "grade": 2},
        "mercury": {"localized": _(u"Mercury"), "category": "raw", "grade": 3},
        "polonium": {"localized": _(u"Polonium"), "category": "raw", "grade": 4},
        "tellurium": {"localized": _(u"Tellurium"), "category": "raw", "grade": 4},
        "yttrium": {"localized": _(u"Yttrium"), "category": "raw", "grade": 4},
        "antimony": {"localized": _(u"Antimony"), "category": "raw", "grade": 4},
        "selenium": {"localized": _(u"Selenium"), "category": "raw", "grade": 4},
        "ruthenium": {"localized": _(u"Ruthenium"), "category": "raw", "grade": 4},
        "zirconium": {"localized": _(u"Zirconium"), "category": "raw", "grade": 2},
        "vanadium": {"localized": _(u"Vanadium"), "category": "raw", "grade": 2},
        "manganese": {"localized": _(u"Manganese"), "category": "raw", "grade": 2},
        "chromium": {"localized": _(u"Chromium"), "category": "raw", "grade": 2},
        "molybdenum": {"localized": _(u"Molybdenum"), "category": "raw", "grade": 3},
        "technetium": {"localized": _(u"Technetium"), "category": "raw", "grade": 3},
        "tin": {"localized": _(u"Tin"), "category": "raw", "grade": 3},
        "arsenic": {"localized": _(u"Arsenic"), "category": "raw", "grade": 2},
        "cadmium": {"localized": _(u"Cadmium"), "category": "raw", "grade": 3},
        "iron": {"localized": _(u"Iron"), "category": "raw", "grade": 1},
        "niobium": {"localized": _(u"Niobium"), "category": "raw", "grade": 3},
        "phosphorus": {"localized": _(u"Phosphorus"), "category": "raw", "grade": 1},
        "germanium": {"localized": _(u"Germanium"), "category": "raw", "grade": 2},
        "tungsten": {"localized": _(u"Tungsten"), "category": "raw", "grade": 3},
        "sulphur": {"localized": _(u"Sulphur"), "category": "raw", "grade": 1},
        "carbon": {"localized": _(u"Carbon"), "category": "raw", "grade": 1},
        "nickel": {"localized": _(u"Nickel"), "category": "raw", "grade": 1},
        "rhenium": {"localized": _(u"Rhenium"), "category": "raw", "grade": 1},
        "boron": {"localized": _(u"Boron"), "category": "raw", "grade": 3},
        "lead": {"localized": _(u"Lead"), "category": "raw", "grade": 1},
        "focuscrystals": {"localized": _(u"Focus Crystals"), "category": "manufactured", "grade": 3},
        "compoundshielding": {"localized": _(u"Compound Shielding"), "category": "manufactured", "grade": 4},
        "galvanisingalloys": {"localized": _(u"Galvanising Alloys"), "category": "manufactured", "grade": 2},
        "heatvanes": {"localized": _(u"Heat Vanes"), "category": "manufactured", "grade": 4},
        "configurablecomponents": {"localized": _(u"Configurable Components"), "category": "manufactured", "grade": 4},
        "biotechconductors": {"localized": _(u"Biotech Conductors"), "category": "manufactured", "grade": 5},
        "chemicalmanipulators": {"localized": _(u"Chemical Manipulators"), "category": "manufactured", "grade": 4},
        "mechanicalcomponents": {"localized": _(u"Mechanical Components"), "category": "manufactured", "grade": 3},
        "fedproprietarycomposites": {"localized": _(u"Proprietary Composites"), "category": "manufactured", "grade": 4},
        "highdensitycomposites": {"localized": _(u"High Density Composites"), "category": "manufactured", "grade": 3},
        "protoradiolicalloys": {"localized": _(u"Proto Radiolic Alloys"), "category": "manufactured", "grade": 5},
        "chemicaldistillery": {"localized": _(u"Chemical Distillery"), "category": "manufactured", "grade": 3},
        "chemicalprocessors": {"localized": _(u"Chemical Processors"), "category": "manufactured", "grade": 2},
        "imperialshielding": {"localized": _(u"Imperial Shielding"), "category": "manufactured", "grade": 5},
        "gridresistors": {"localized": _(u"Grid Resistors"), "category": "manufactured", "grade": 1},
        "heatconductionwiring": {"localized": _(u"Heat Conduction Wiring"), "category": "manufactured", "grade": 1},
        "militarygradealloys": {"localized": _(u"Military Grade Alloys"), "category": "manufactured", "grade": 5},
        "hybridcapacitors": {"localized": _(u"Hybrid Capacitors"), "category": "manufactured", "grade": 2},
        "heatexchangers": {"localized": _(u"Heat Exchangers"), "category": "manufactured", "grade": 3},
        "conductivepolymers": {"localized": _(u"Conductive Polymers"), "category": "manufactured", "grade": 4},
        "shieldingsensors": {"localized": _(u"Shielding Sensors"), "category": "manufactured", "grade": 3},
        "heatdispersionplate": {"localized": _(u"Heat Dispersion Plate"), "category": "manufactured", "grade": 2},
        "electrochemicalarrays": {"localized": _(u"Electrochemical Arrays"), "category": "manufactured", "grade": 1},
        "conductiveceramics": {"localized": _(u"Conductive Ceramics"), "category": "manufactured", "grade": 3},
        "conductivecomponents": {"localized": _(u"Conductive Components"), "category": "manufactured", "grade": 2},
        "militarysupercapacitors": {"localized": _(u"Military Supercapacitors"), "category": "manufactured", "grade": 5},
        "mechanicalequipment": {"localized": _(u"Mechanical Equipment"), "category": "manufactured", "grade": 2},
        "phasealloys": {"localized": _(u"Phase Alloys"), "category": "manufactured", "grade": 3},
        "pharmaceuticalisolators": {"localized": _(u"Pharmaceutical Isolators"), "category": "manufactured", "grade": 5},
        "fedcorecomposites": {"localized": _(u"Core Dynamics Composites"), "category": "manufactured", "grade": 5},
        "basicconductors": {"localized": _(u"Basic Conductors"), "category": "manufactured", "grade": 1},
        "mechanicalscrap": {"localized": _(u"Mechanical Scrap"), "category": "manufactured", "grade": 1},
        "salvagedalloys": {"localized": _(u"Salvaged Alloys"), "category": "manufactured", "grade": 1},
        "protolightalloys": {"localized": _(u"Proto Light Alloys"), "category": "manufactured", "grade": 4},
        "refinedfocuscrystals": {"localized": _(u"Refined Focus Crystals"), "category": "manufactured", "grade": 4},
        "shieldemitters": {"localized": _(u"Shield Emitters"), "category": "manufactured", "grade": 1},
        "precipitatedalloys": {"localized": _(u"Precipitated Alloys"), "category": "manufactured", "grade": 3},
        "wornshieldemitters": {"localized": _(u"Worn Shield Emitters"), "category": "manufactured", "grade": 1},
        "exquisitefocuscrystals": {"localized": _(u"Exquisite Focus Crystals"), "category": "manufactured", "grade": 5},
        "polymercapacitors": {"localized": _(u"Polymer Capacitors"), "category": "manufactured", "grade": 4},
        "thermicalloys": {"localized": _(u"Thermic Alloys"), "category": "manufactured", "grade": 4},
        "improvisedcomponents": {"localized": _(u"Improvised Components"), "category": "manufactured", "grade": 5},
        "crystalshards": {"localized": _(u"Crystal Shards"), "category": "manufactured", "grade": 1},
        "heatresistantceramics": {"localized": _(u"Heat Resistant Ceramics"), "category": "manufactured", "grade": 2},
        "temperedalloys": {"localized": _(u"Tempered Alloys"), "category": "manufactured", "grade": 1},
        "uncutfocuscrystals": {"localized": _(u"Flawed Focus Crystals"), "category": "manufactured", "grade": 2},
        "filamentcomposites": {"localized": _(u"Filament Composites"), "category": "manufactured", "grade": 2},
        "compactcomposites": {"localized": _(u"Compact Composites"), "category": "manufactured", "grade": 1},
        "chemicalstorageunits": {"localized": _(u"Chemical Storage Units"), "category": "manufactured", "grade": 1},
        "guardian_powerconduit": {"localized": _(u"Guardian Power Conduit"), "category": "manufactured", "grade": 2},
        "guardian_powercell": {"localized": _(u"Guardian Power Cell"), "category": "manufactured", "grade": 1},
        "guardian_techcomponent": {"localized": _(u"Guardian Technology Component"), "category": "manufactured", "grade": 3},
        "guardian_sentinel_wreckagecomponents": {"localized": _(u"Guardian Wreckage Components"), "category": "manufactured", "grade": 1},
        "guardian_sentinel_weaponparts": {"localized": _(u"Guardian Sentinel Weapon Parts"), "category": "manufactured", "grade": 3},
        "classifiedscandata": {"localized": _(u"Classified Scan Fragment"), "category": "encoded", "grade": 5},
        "securityfirmware": {"localized": _(u"Security Firmware Patch"), "category": "encoded", "grade": 4},
        "dataminedwake": {"localized": _(u"Datamined Wake Exceptions"), "category": "encoded", "grade": 5},
        "compactemissionsdata": {"localized": _(u"Abnormal Compact Emissions Data"), "category": "encoded", "grade": 5},
        "shieldpatternanalysis": {"localized": _(u"Aberrant Shield Pattern Analysis"), "category": "encoded", "grade": 4},
        "adaptiveencryptors": {"localized": _(u"Adaptive Encryptors Capture"), "category": "encoded", "grade": 5},
        "emissiondata": {"localized": _(u"Unexpected Emission Data"), "category": "encoded", "grade": 3},
        "industrialfirmware": {"localized": _(u"Cracked Industrial Firmware"), "category": "encoded", "grade": 3},
        "scandatabanks": {"localized": _(u"Classified Scan Databanks"), "category": "encoded", "grade": 3},
        "legacyfirmware": {"localized": _(u"Specialised Legacy Firmware"), "category": "encoded", "grade": 1},
        "embeddedfirmware": {"localized": _(u"Modified Embedded Firmware"), "category": "encoded", "grade": 5},
        "shieldcyclerecordings": {"localized": _(u"Distorted Shield Cycle Recordings"), "category": "encoded", "grade": 1},
        "decodedemissiondata": {"localized": _(u"Decoded Emission Data"), "category": "encoded", "grade": 4},
        "bulkscandata": {"localized": _(u"Anomalous Bulk Scan Data"), "category": "encoded", "grade": 1},
        "scanarchives": {"localized": _(u"Unidentified Scan Archives"), "category": "encoded", "grade": 2},
        "shieldsoakanalysis": {"localized": _(u"Inconsistent Shield Soak Analysis"), "category": "encoded", "grade": 2},
        "encodedscandata": {"localized": _(u"Divergent Scan Data"), "category": "encoded", "grade": 4},
        "shielddensityreports": {"localized": _(u"Untypical Shield Scans"), "category": "encoded", "grade": 3},
        "shieldfrequencydata": {"localized": _(u"Peculiar Shield Frequency Data"), "category": "encoded", "grade": 5},
        "encryptioncodes": {"localized": _(u"Tagged Encryption Codes"), "category": "encoded", "grade": 2},
        "consumerfirmware": {"localized": _(u"Modified Consumer Firmware"), "category": "encoded", "grade": 2},
        "archivedemissiondata": {"localized": _(u"Irregular Emission Data"), "category": "encoded", "grade": 2},
        "symmetrickeys": {"localized": _(u"Open Symmetric Keys"), "category": "encoded", "grade": 3},
        "encryptedfiles": {"localized": _(u"Unusual Encrypted Files"), "category": "encoded", "grade": 1},
        "scrambledemissiondata": {"localized": _(u"Exceptional Scrambled Emission Data"), "category": "encoded", "grade": 1},
        "fsdtelemetry": {"localized": _(u"Anomalous FSD Telemetry"), "category": "encoded", "grade": 2},
        "hyperspacetrajectories": {"localized": _(u"Eccentric Hyperspace Trajectories"), "category": "encoded", "grade": 4},
        "disruptedwakeechoes": {"localized": _(u"Atypical Disrupted Wake Echoes"), "category": "encoded", "grade": 1},
        "wakesolutions": {"localized": _(u"Strange Wake Solutions"), "category": "encoded", "grade": 3},
        "encryptionarchives": {"localized": _(u"Atypical Encryption Archives"), "category": "encoded", "grade": 4},
        "ancientbiologicaldata": {"localized": _(u"Pattern Alpha Obelisk Data"), "category": "encoded", "grade": 3},
        "ancienthistoricaldata": {"localized": _(u"Pattern Gamma Obelisk Data"), "category": "encoded", "grade": 4},
        "guardian_moduleblueprint": {"localized": _(u"Guardian Module Blueprint Fragment"), "category": "encoded", "grade": 5},
        "ancientculturaldata": {"localized": _(u"Pattern Beta Obelisk Data"), "category": "encoded", "grade": 2},
        "ancientlanguagedata": {"localized": _(u"Pattern Delta Obelisk Data"), "category": "encoded", "grade": 4},
    }

    #TODO guardian vessel blueprint segment, G5 guardian_vesselblueprint, Guardian Starship Blueprint Fragment
    #TODO guardian weapon bluepring segment, g5, guardian_weaponblueprint, Guardian Weapon Blueprint Fragment
    #TODO guardian pattern epsilon, g5, ancienttechnologicaldata", "Name_Localised":"Pattern Epsilon Obelisk Data
    #TODO ship systems data, g3, tg_shipsystemsdata, Ship Systems Data
    #TODO ship flight data, g3, tg_shipflightdata, Ship Flight Data
    #TODO thargoid ship signature, g3, unknownshipsignature", "Name_Localised":"Thargoid Ship Signature
    #TODO thargoid structural data, g2, tg_structuraldata", "Name_Localised":"Thargoid Structural Data
    #TODO thargoid wake data, g4, unknownwakedata", "Name_Localised":"Thargoid Wake Data
    #TODO protoheatradiator, g5, protoheatradiators", "Name_Localised":"Proto Heat Radiators"
    #TODO bio-mechanical conduits, g3, tg_biomechanicalconduits", "Name_Localised":"Bio-Mechanical Conduits
    #TODO propulsion elements, g3, tg_propulsionelement", "Name_Localised":"Propulsion Elements
    #TODO thargoid carapace, g2, unknowncarapace", "Name_Localised":"Thargoid Carapace
    #TODO thargoid energy cell, g3, unknownenergycell", "Name_Localised":"Thargoid Energy Cell
    #TODO thargoid organic circuitry, g5, unknownorganiccircuitry", "Name_Localised":"Thargoid Organic Circuitry
    #TODO thargoid technological components, g4, unknowntechnologycomponents", "Name_Localised":"Thargoid Technological Components

    def __init__(self):
        self.encoded = {}
        self.raw = {}
        self.manufactured = {}

    def initialize(self, materials):
        for thing in materials["Encoded"]:
            cname = self.__c_name(thing["Name"])
            self.encoded[cname] = thing["Count"]

        for thing in materials["Raw"]:
            cname = self.__c_name(thing["Name"])
            self.raw[cname] = thing["Count"]

        for thing in materials["Raw"]:
            cname = self.__c_name(thing["Name"])
            self.manufactured[cname] = thing["Count"]

    def collected(self, info):
        self.add(info["Category"], info["Name"], info["Count"])

    def discarded(self, info):
        self.substract(info["Category"], info["Name"], info["Count"])

    def count(self, name):
        category = self.category(name)
        cname = self.__c_name(name)
        if category == "encoded":
            return self.encoded.get(cname)
        elif category == "raw":
            return self.raw.get(cname)
        elif category == "encoded":
            return self.manufactured.get(cname)

    def oneliner(self, name):
        category = self.category(name)
        cname = self.__c_name(name)
        entry = self.MATERIALS_LUT.get(cname, None)
        if not category or not entry:
            return "{} (?!)"
        count = self.count(cname)
        #grades = [u"?", u"❶", u"❷", u"❸", u"❹", u"❺"]
        grades = [u"?", u"Ⅰ", u"Ⅱ", u"Ⅲ", u"Ⅳ", u"Ⅴ"]
        slots = [u"?", u"300", u"250", u"200", u"150", u"100"]
        return u"{} (Grade: {}; {}/{})".format(entry["localized"], grades[entry["grade"]], count, slots[entry["slots"]])

    def donated_engineer(self, info):
        if info["Type"] != "Material":
            return
        category = self.category(info["Name"])
        if category:
            self.substract(category, info["Name"], info["Quantity"])

    def donated_science(self, info):
        self.substract(info["Category"], info["Name"], info["Count"])

    def consumed(self, ingredients):
        for ingredient in ingredients:
            category = ingredient.get("Category", self.category(ingredient["Name"]))
            if category:
                self.substract(category, ingredient["Name"], ingredient["Count"])

    def traded(self, info):
        paid = info["Paid"]
        self.substract(paid["Category"], paid["Name"], paid["Quantity"])
        received = info["Received"]
        self.substract(received["Category"], received["Name"], received["Quantity"])

    def rewarded(self, info):
        # TODO Does Search And Rescue give material rewards??
        if "MaterialsReward" not in info:
            return
        for reward in info["MaterialsReward"]:
            self.add(reward["Category"], reward["Name"], reward["Count"])

    def add(self, category, name, count):
        ccategory = self.__c_cat(category)
        cname = self.__c_name(name)
        if ccategory == "encoded":
            self.encoded[cname] += count
        elif ccategory == "raw":
            self.raw[cname] += count
        elif ccategory == "manufactured":
            self.manufactured[cname] += count

    def substract(self, category, name, count):
        ccategory = self.__c_cat(category)
        cname = self.__c_name(name)
        if ccategory == "encoded":
            self.encoded[cname] -= count
        elif ccategory == "raw":
            self.raw[cname] -= count
        elif ccategory == "manufactured":
            self.manufactured[cname] -= count

    def category(self, name):
        cname = self.__c_name(name)
        entry = self.MATERIALS_LUT.get(cname, None)
        return entry["category"] if entry else None

    def __c_cat(self, category):
        ccat = category.lower()
        if ccat.endswith(u";"):
            ccat = ccat[:-1]
        if ccat.startswith(u"$MICRORESOURCE_CATEGORY_"):
            useless_prefix_length = len(u"$MICRORESOURCE_CATEGORY_")
            ccat = ccat[useless_prefix_length:]
        return ccat

    def __c_name(self, name):
        return name.lower()