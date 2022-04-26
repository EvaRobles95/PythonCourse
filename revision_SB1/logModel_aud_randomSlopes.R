# Random slope models vs. no random slope models

# import lme4 module for mixed models
library(lme4)
library(emmeans)
library(MuMIn)
library(optimx)
library(car)

# read data - auditory
data_aud <- read.csv("C://Users//annae//Desktop//ChoiceHistory_Psych//Data//Exp1_auditory//exp1_model1_auditory.csv")

# 1. MODEL WITHOUT RANDOM SLOPES
patsy_noRS <- 'response ~ (1|sbj_id) + (1|block:sbj_id) + target_z + stimulus_z + stim_1_z + cue_z * PPS_z * block_type + resp_1_z * PPS_z * block_type_z'


model_aud_noRS <- glmer(patsy_noRS, data=data_aud, 
                    family=binomial('logit'), 
                    control=glmerControl(optimizer='optimx', optCtrl=list(method='nlminb')))


# 2. MODEL WITH ALL RANDOM SLOPES (CUE, STIMULUS AND CHOICE HISTORY)
patsy_RS <- 'response ~ (1|sbj_id) + (1|block:sbj_id) + (1+cue_z|sbj_id) + (1+resp_1_z|sbj_id) + (1+stim_1_z|sbj_id) + target_z + stimulus_z + stim_1_z + cue_z * PPS_z * block_type_z + resp_1_z * PPS_z * block_type_z'

model_RS <- glmer(patsy_RS, data=data_aud,
                  family=binomial('logit'),
                  control=glmerControl(optimizer='optimx', optCtrl=list(method='nlminb')))


# 3. MODEL WITH RANDOM SLOPE FOR CUE
patsy_RScue <- 'response ~ (1|sbj_id) + (1|block:sbj_id) + (1+cue_z|sbj_id) + target_z + stimulus_z + stim_1_z + cue_z * PPS_z * block_type_z + resp_1_z * PPS_z * block_type_z'

model_aud_RScue <- glmer(patsy_RScue, data=data_aud,
                         family=binomial('logit'),
                         control=glmerControl(optimizer='optimx', optCtrl=list(method='nlminb')))


# 4. MODEL WITH RANDOM SLOPE FOR CHOICE HISTORY
patsy_RS_rt1 <- 'response ~ (1|sbj_id) + (1|block:sbj_id) + (1+resp_1_z|sbj_id) + target_z + stimulus_z + stim_1_z + cue_z * PPS_z * block_type_z + resp_1_z * PPS_z * block_type_z'

model_aud_RS_rt1 <- glmer(patsy_RS_rt1, data=data_aud,
                          family=binomial('logit'),
                          control=glmerControl(optimizer='optimx', optCtrl=list(method='nlminb')))

# 5. MODEL WITH RANDOM SLOPE FOR STIMULUS HISTORY
patsy_RS_st1 <- 'response ~ (1|sbj_id) + (1|block:sbj_id) + (1+stim_1_z|sbj_id) + target_z + stimulus_z + stim_1_z + cue_z * PPS_z * block_type_z + resp_1_z * PPS_z * block_type_z'

model_aud_RS_st1 <- glmer(patsy_RS_st1, data=data_aud,
                          family=binomial('logit'),
                          control=glmerControl(optimizer='optimx', optCtrl=list(method='nlminb')))

