from cobra.io import read_sbml_model
from cobra import Reaction, Metabolite

# Load the Aspergillus niger ATCC1015 model
model = read_sbml_model('../model/Aspergillus_ATCC1015.xml')

# Create all metabolites
Amorphadiene = Metabolite(id = 'amorpha', name = 'Amorphadiene', compartment = 'c')
Artemisinic_alcohol = Metabolite(id = 'artem_alcohol', name = 'Artemisinic alcohol', compartment = 'c')
Artemisinic_aldehyde = Metabolite(id = 'artem_aldehyde', name = 'Artemisinic aldehyde', compartment = 'c')
Artemisinic_acid_c = Metabolite(id = 'ARTA_c', name = 'Artemisinic acid_c', compartment = 'c')
Artemisinic_acid_e = Metabolite(id = 'ARTA_e', name = 'Artemisinic acid_e', compartment = 'e')

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
model.add_boundary(model.metabolites.get_by_id("ARTA_e"), type="exchange")

# Changing model media to YPD
YPD_media = model.medium
YPD_media['BOUNDARY_GLCe'] = 20
YPD_media['BOUNDARY_ALAe'] = 10
YPD_media['BOUNDARY_ARGe'] = 10
YPD_media['BOUNDARY_ASPe'] = 10
YPD_media['BOUNDARY_CYSe'] = 10
YPD_media['BOUNDARY_GLUe'] = 10
YPD_media['BOUNDARY_GLYe'] = 10
YPD_media['BOUNDARY_HISe'] = 10
YPD_media['BOUNDARY_ILEe'] = 10
YPD_media['BOUNDARY_LEUe'] = 10
YPD_media['BOUNDARY_LYSe'] = 10
YPD_media['BOUNDARY_METe'] = 10
YPD_media['BOUNDARY_PHEe'] = 10
YPD_media['BOUNDARY_PROe'] = 10
YPD_media['BOUNDARY_SERe'] = 10
YPD_media['BOUNDARY_THRe'] = 10
YPD_media['BOUNDARY_TRPe'] = 10
YPD_media['BOUNDARY_TYRe'] = 10
YPD_media['BOUNDARY_VALe'] = 10
YPD_media['BOUNDARY_ZNe'] = 10
YPD_media['BOUNDARY_FE2e'] = 10
YPD_media['BOUNDARY_HNO3e'] = 0
model.medium = YPD_media

# Setting bounds for exchange reactions
model.reactions.BOUNDARY_ALAe.bounds = -10, 0
model.reactions.BOUNDARY_ARGe.bounds = -10, 0
model.reactions.BOUNDARY_ASPe.bounds = -10, 0
model.reactions.BOUNDARY_CYSe.bounds = -10, 0
model.reactions.BOUNDARY_GLUe.bounds = -10, 0
model.reactions.BOUNDARY_GLYe.bounds = -10, 0
model.reactions.BOUNDARY_HISe.bounds = -10, 0
model.reactions.BOUNDARY_ILEe.bounds = -10, 0
model.reactions.BOUNDARY_LEUe.bounds = -10, 0
model.reactions.BOUNDARY_LYSe.bounds = -10, 0
model.reactions.BOUNDARY_METe.bounds = -10, 0
model.reactions.BOUNDARY_PHEe.bounds = -10, 0
model.reactions.BOUNDARY_PROe.bounds = -10, 0
model.reactions.BOUNDARY_SERe.bounds = -10, 0
model.reactions.BOUNDARY_THRe.bounds = -10, 0
model.reactions.BOUNDARY_TRPe.bounds = -10, 0
model.reactions.BOUNDARY_TYRe.bounds = -10, 0
model.reactions.BOUNDARY_VALe.bounds = -10, 0


# Implement biomass constraints (50% of theoretical max)
# Theorhetical max: 15.1154
constrained_growth = model.problem.Constraint(
    model.reactions.get_by_id('DRAIN_Biomass').flux_expression,
    lb=15.1154/2,
    ub=15.1154)
model.add_cons_vars(constrained_growth)

model
