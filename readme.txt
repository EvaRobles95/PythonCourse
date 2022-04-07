All code and data to reproduce analyses and figures of Choice History in Psychosis Proneness article. 

Separate .csv files are necessary for fitting the logistic choice model and psychometric functions, 
because psychometric functions require signed stimulus intensity which would falsify regression results. 
All datafiles can be produced from the raw data using the respective pre-processing scripts. 

Anonymized, raw data can be found in the figshare repository: https://figshare.com/account/home#/projects/131861


Code and analyses: 
	- pmf_repProb folders contain code to reproduce figures 2 and 3, psychometric function fit and repetition probability. 
	- pre-processing scripts can be found in pre-processing folder. 
	- Logistic model code in R can be found in the Logistic_Model folder. 
	- Result figure 1 can be obtained from running r_results.ipynb from in Logistic_model, however, some polishing touches were made using a graphical editor (inkscape).
	- supplementary analysis S2 can be reproduced using the script "suppl_logistic_model_neutralOnly.R" in the Logistic_Model folder
