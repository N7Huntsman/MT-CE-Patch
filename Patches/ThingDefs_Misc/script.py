import xml.etree.ElementTree as ET

files = ['MedTimes_Weapons_Melee.xml',
		'MedTimes_Weapons_Melee_Rare.xml',
		'MedTimes_Weapons_Melee_Nan.xml']

apBaseValue = {	"Stab": 0.075,
				"Bite": 0.06,
				"Slash": 0.05,
				"Cut": 0.04,
				"Blunt": 0.04,
				"Poke": 0.03,
				"Scratch": 0.03}

apPerDmg = {	"Stab": 0.015,
				"Bite": 0.012,
				"Slash": 0.01,
				"Cut": 0.008,
				"Blunt": 0.008,
				"Poke": 0.006,
				"Scratch": 0.006}

apDimFactor = {	"Stab": 0.5,
				"Bite": 0.5,
				"Slash": 0.5,
				"Cut": 0.5,
				"Blunt": 0.2,
				"Poke": 0.5,
				"Scratch": 1}


def calculateAP(power, dmgType):
	return str(round(((apBaseValue[dmgType] + power * apPerDmg[dmgType]) / (1 + apDimFactor[dmgType] * power / 100)), 3))


for path in files:

	source = ET.parse(path)
	root = source.getroot()

	for tool in root.findall(".//tools/li"):
		power = float(tool.find('./power').text)
		dmgType = tool.find('./capacities/li').text
		AP = tool.find('./armorPenetration')
		AP.text = calculateAP(power, dmgType)

	source.write(path)

