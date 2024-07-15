# Certifications-Of-NLP-Models

This web application is a platform that allows users to certificate NLP models,
working with HuggingFace models and questionnaire to evaluate models' biases.

For information about building and developing the app see app installation.txt

For information about how to install the app on a linux machine and manage the production servers see Readme Servers.txt.
 


## configuring .env.env file:
#### RESET_DB - set True to reset the db on application execution (then set back to false to avoid additional reset)
#### HF_MODEL_NAME_FILTER - the Agent returns models that has one of these keywords in its name, for automatic evaluation
#### EVALUATION_TIMED_OUT - after this timeout, evaluation will stop and consider the model as "Failed to evaluate" (is used to solved out of memory bug in model evaluation)