import LoadLocationData
import Badge
import RandomizeItems
import RandomizerRom
import PokemonRandomizer
import yaml
from collections import defaultdict

res = LoadLocationData.LoadDataFromFolder(".")
trashItems = res[1]
LocationList = LoadLocationData.FlattenLocationTree(res[0])
yamlfile = open("TrainerData/Trainers.yaml")
yamltext = yamlfile.read()
trainerData = yaml.load(yamltext)
RandomizerRom.ResetRomForLabelling()
RandomizerRom.LabelAllLocations(LocationList)
RandomizerRom.LabelTrainerData(trainerData)
RandomizerRom.LabelWild()