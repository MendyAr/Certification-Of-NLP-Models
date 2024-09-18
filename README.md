# Certifications-Of-NLP-Models
https://nlp-cetrification.cs.bgu.ac.il/  

This web application is a platform that allows users to certificate NLP models,
working with HuggingFace models and questionnaire to evaluate models' biases.

For information about building and developing the app see app installation.txt

For information about how to install the app on a linux machine and manage the production servers see Readme Servers.txt.
 
# Important notes for developers
## Evaluation score meaning
Error score shown when the evaluation module couldn't complete the evaluation.  
"Evaluation failed" - possible causes:   
evaluation module failed to evaluate due to exception in the evaluation module.  
model took too long to be evaluated, more than "evaluation_timed_out" [value](.env.env), which is used to avoid the following error.   
model is too large to be evaluated on this machine (out of memory error).

"Model is incompatible for evaluation" - possible causes:  
evaluation module failed to evaluate due to exception in the evaluation module and also the model configuration doesn't have the "label2id" key with "entailment" != -1   



## Configuring [.env](.env.env) file:
#### RESET_DB - set True to reset the db on application execution (then set back to false to avoid additional reset)
#### HF_MODEL_NAME_FILTER - the Agent returns models that has one of these keywords in their names, for automatic evaluation
#### EVALUATION_TIMED_OUT - after this timeout, evaluation will stop and consider the model as "Failed to evaluate" (is used to solved out of memory bug in model evaluation)
