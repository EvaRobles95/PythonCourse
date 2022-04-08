# import lme4 module for mixed models
library(lme4)
library(emmeans)
library(MuMIn)
library(optimx)

# read data - auditory
data_aud <- read.csv("C://Users//annae//Desktop//ChoiceHistory_Psych//Data//Exp1_auditory//exp1_prevMotor_prevDiff.csv")

# read data - visual
data_vis <- read.csv("C://Users//annae//Desktop//ChoiceHistory_Psych//Data//Exp2_visual//exp2_prevMotor_prevDiff.csv")

# set up model on auditory data...
# patsy auditory
patsy_aud <- 'response ~ (1|sbj_id) + target_z + stimulus_z + (1|block:sbj_id) + cue_z * PPS_z * block_type + stim_1_z + resp_1_z * PPS_z * block_type_z + cue_z*resp_1_z*PPS_z + prev_mot_z * PPS_z * resp_1_z'

# patsy for auditory neutral blocks only
#patsy_aud <- 'response_z ~ (1|sbj_id) + target_z + stimulus_z + cue_z * PPS_z + stim_1_z + resp_1_z * PPS_z'

model1_aud <- glmer(patsy_aud, data=data_aud, 
                    family=binomial('logit'), 
                    control=glmerControl(optimizer='optimx', optCtrl=list(method='nlminb')))

# save model in summary text file for later manip. in python
sink('exp1_model_prevMotor.txt')
print(summary(model1_aud))
sink()

# set up model on visual data... 
# patsy visual
patsy_vis <- 'response ~ (1|sbj_id) + target_z + coherence_z + (1|Block:sbj_id) + cue_z * PPS_z * block_type + stim_1_z + resp_1_z * PPS_z * block_type_z + cue_z*resp_1_z*PPS_z + prev_mot_z * PPS_z * resp_1_z'

# patsy visual, neutral blocks only
#patsy_vis <- 'response ~ (1|sbj_id) + target + coherence + cue * PPS_z + stim_1 + resp_1 * PPS_z'

model1_vis <- glmer(patsy_vis, data=data_vis,
                    family=binomial('logit'),
                    control=glmerControl(optimizer='optimx', optCtrl = list(method='nlminb')))


# save model summary in text file
sink('exp2_model_prevMotor.txt')
print(summary(model1_vis))
sink()

r.squaredGLMM(model1_aud)
r.squaredGLMM(model1_vis)
