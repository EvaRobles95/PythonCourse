################################################################################
# Random slope models vs. no random slope models
# VISUAL

# set up model on visual data... 
# patsy visual

# read data - visual
data_vis <- read.csv("C://Users//annae//Desktop//ChoiceHistory_Psych//Data//Exp2_visual//exp2_model1_visual.csv")

patsy_vis <- 'response ~ (1|sbj_id)  + (1|Block:sbj_id) + target_z + coherence_z + cue_z  + stim_1_z + resp_1_z * PPS_z + PPS_z * stim_1_z '

model1_vis <- glmer(patsy_vis, data=data_vis,
                    family=binomial('logit'),
                    control=glmerControl(optimizer='optimx', optCtrl = list(method='nlminb')))