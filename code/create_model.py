from cobra.io import read_sbml_model
from cobra import Reaction, Metabolite

# Load the Aspergillus niger ATCC1015 model
model = read_sbml_model('../model/Aspergillus_ATCC1015.xml')

# Create all metabolites
Amorphadiene = Metabolite(id = 'amorpha', name = 'Amorphadiene', compartment = 'c')
Artemisinic_alcohol = Metabolite(id = 'artem_alcohol', name = 'Artemisinic alcohol', compartment = 'c')
Artemisinic_aldehyde = Metabolite(id = 'artem_aldehyde', name = 'Artemisinic aldehyde', compartment = 'c')
Artemisinic_acid_c = Metabolite(id = 'artem_acid_c', name = 'Artemisinic acid_c', compartment = 'c')
Artemisinic_acid_e = Metabolite(id = 'artem_acid_e', name = 'Artemisinic acid_e', compartment = 'e')

# Create all reactions
ADS = Reaction('ADS_reaction')
ADS.add_metabolites({
    model.metabolites.FPP: -1,
    Amorphadiene: 1
})

CYP1_CYB5 = Reaction('CYP1AV1CY/PCPR1/CYB5_reaction')
CYP1_CYB5.add_metabolites({
    Amorphadiene: -1,
    Artemisinic_alcohol: 1
})

ADH1 = Reaction('ADH1_reaction')
ADH1.add_metabolites({
    Artemisinic_alcohol: -1,
    Artemisinic_aldehyde: 1
})

ALDH1 = Reaction('ALDH1_reaction')
ALDH1.add_metabolites({
    Artemisinic_aldehyde: -1,
    Artemisinic_acid_c: 1
})

Artemisinic_acid_ex = Reaction('ARTA_ex')
Artemisinic_acid_ex.add_metabolites({
    Artemisinic_acid_c: -1,
    Artemisinic_acid_e: 1
})

new_reactions = [ADS, CYP1_CYB5, ADH1, ALDH1, Artemisinic_acid_ex]

model.add_reactions(new_reactions)
model.add_boundary(model.metabolites.get_by_id("artem_acid_e"), type="exchange")

model
