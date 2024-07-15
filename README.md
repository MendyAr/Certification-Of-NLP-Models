# Certifications-Of-NLP-Models

This web application is a platform that allows users to certificate NLP models,
working with HuggingFace models and questionnaire to evaluate models' biases.

For information about building and developing the app see app installation.txt

For information about how to install the app on a linux machine and manage the production servers see Readme Servers.txt.
 

## Scores in the csv file
Error score shown when the evaluation module couldn't complete the evaluation.  
Evaluation failed - Possible causes:  
model is too large to be evaluated on this machine (out of memory error).
evaluation module failed to evaluate (exception occurred in the evaluating module).

Model is incompatible for evaluation - Possible causes:  
evaluation module failed to evaluate (exception occurred in the evaluating module) and also a model configuration doesn't have the "label2id" key with "entailment" != -1   



## Configuring .env.env file:
#### RESET_DB - set True to reset the db on application execution (then set back to false to avoid additional reset)
#### HF_MODEL_NAME_FILTER - the Agent returns models that has one of these keywords in its name, for automatic evaluation
#### EVALUATION_TIMED_OUT - after this timeout, evaluation will stop and consider the model as "Failed to evaluate" (is used to solved out of memory bug in model evaluation)