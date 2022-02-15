# import lme4 module for mixed models
library(lme4)
library(emmeans)
library(MuMIn)
library(optimx)

# read data - visual
data_vis <- read.csv("C://Users//annae//Desktop//ChoiceHistory_Psych//Data//Exp2_visual//exp2_inclOldDesignCol.csv")


# patsy visual
patsy_vis <- 'response ~ (1|sbj_id) + target_z + coherence_z + (1|Block:sbj_id) + cue_z * PPS_z * block_type + stim_1_z * PPS_z + resp_1_z * PPS_z * block_type_z + cue_z*resp_1_z*PPS_z + old_z'
# patsy visual, neutral blocks only
#patsy_vis <- 'response ~ (1|sbj_id) + target + coherence + cue * PPS_z + stim_1 + resp_1 * PPS_z'

model1_vis <- glmer(patsy_vis, data=data_vis,
                    family=binomial('logit'),
                    control=glmerControl(optimizer='optimx', optCtrl = list(method='nlminb')))


# save model summary in text file
sink('OldDesign_visual.txt')
print(summary(model1_vis))
sink()

r.squaredGLMM(model1_vis)