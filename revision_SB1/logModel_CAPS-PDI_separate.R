# Looking at individual PPS measures
library(lme4)
library(emmeans)
library(MuMIn)
library(optimx)

# read data - auditory
data_aud <- read.csv("C://Users//annae//Desktop//ChoiceHistory_Psych//Data//Exp1_auditory//exp1_model1_auditory.csv")

# read data - visual
data_vis <- read.csv("C://Users//annae//Desktop//ChoiceHistory_Psych//Data//Exp2_visual//exp2_model1_visual.csv")

# set up model on auditory data...
# patsy auditory: PDI
patsy_aud_pdi <- 'response ~ (1|sbj_id) + target_z + stimulus_z + (1|block:sbj_id) + cue_z * pdi_z * block_type + stim_1_z + resp_1_z * pdi_z * block_type_z + cue_z*resp_1_z*pdi_z'

patsy_aud_caps <- 'response ~ (1|sbj_id) + target_z + stimulus_z + (1|block:sbj_id) + cue_z * caps_z * block_type + stim_1_z + resp_1_z*caps_z*block_type_z + cue_z*resp_1_z*caps_z'

# patsy for auditory neutral blocks only
#patsy_aud <- 'response_z ~ (1|sbj_id) + target_z + stimulus_z + cue_z * PPS_z + stim_1_z + resp_1_z * PPS_z'

model1_aud_pdi <- glmer(patsy_aud_pdi, data=data_aud, 
                    family=binomial('logit'), 
                    control=glmerControl(optimizer='optimx', optCtrl=list(method='nlminb')))

model1_aud_caps <- glmer(patsy_aud_caps, data=data_aud, 
                        family=binomial('logit'), 
                        control=glmerControl(optimizer='optimx', optCtrl=list(method='nlminb')))

# save model in summary text file for later manip. in python
sink('exp1_pdi.txt')
print(summary(model1_aud_pdi))
sink()

sink('exp1_caps.txt')
print(summary(model1_aud_caps))
sink()

# set up model on visual data... 
# patsy visual
patsy_vis_pdi <- 'response ~ (1|sbj_id) + target_z + coherence_z + (1|Block:sbj_id) + cue_z * pdi_zscore * block_type + stim_1_z + resp_1_z * pdi_zscore * block_type_z + cue_z*resp_1_z*pdi_zscore'

patsy_vis_caps <- 'response ~ (1|sbj_id) + target_z + coherence_z + (1|Block:sbj_id) + cue_z * caps_zscore * block_type + stim_1_z + resp_1_z * caps_zscore * block_type_z + cue_z*resp_1_z*caps_zscore'


model1_vis_pdi <- glmer(patsy_vis_pdi, data=data_vis,
                    family=binomial('logit'),
                    control=glmerControl(optimizer='optimx', optCtrl = list(method='nlminb')))

model1_vis_caps <- glmer(patsy_vis_caps, data=data_vis,
                        family=binomial('logit'),
                        control=glmerControl(optimizer='optimx', optCtrl = list(method='nlminb')))


# save model summary in text file
sink('exp2_pdi.txt')
print(summary(model1_vis_pdi))
sink()

sink('exp2_caps.txt')
print(summary(model1_vis_caps))
sink()
