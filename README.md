# Ultrasound Probes (UP) team

# Background

Our project was organized as part of the [hackathon for United Nations World Innovation days by Hackmakers](https://hackmakers.com/). the team's topic within Global Sustainable Development Goal of Health and Wellbeing.

Our teams main objective is to show how allowing development of lower cost Ultrasound medical imaging solutions for better guidance to medical teams, we will demonstrate this by develop a tool to doagnose and help with Covid-19 follow-up using ultrasound imaging.  

# Goals of this repo

Develop an AI-enhanced tool to help medical teams Covid-19 lung scarring severity diagnosis using ultrasound imaging. 
The data used to develop the models will come from [OpenSource ultrasound lung imaging for Covid-19 detections](https://github.com/jannisborn/covid19_ultrasound)

Demonstrate the benefit of using a platform to gather Ultrasound Imaging (UI) to enable AI-enhanced diagnosis making for doctors.

Show how collected UI can be put to use for globaly improved diagnosis making process to support medical teams on the field.

Make improvement iteration processes less manuel and more automated using Data Engineering and MLOps tools, e.g. Airflow, and MLFlow for faster experimentation/improvements/model deployment iterations 

# Benefits 

Equip teams with a tool to improve and accelerate decision making in diagnosis situation when using Ultrasound Imaging (UI)

# Non-goal

- reinvent the wheel
- do better than the litterature models

# Designe Overview

## Data Engineering :
### Airflow 
- data processing (cleaning labelling etc.)
- data Augmentation
- Splitting for later ML/DL Experimentation
## Machine Learning Engineering

### MLflow
- to leverage differents experimentations at the same on GPU compute nodes
- track model versions
- automate model deployment
### Python FastAPI
- Expose and serve models through API endpoints 

## Front End

- Develop an interface show Ultrasound image enhanced with models results and other type of information relevant to the medical user.

# Detailed Design

[backend pipeline](images/pipeline2.png)

# Performance Implications

_What should we know about performance?_

# Engineering Asks

_What does the rest of engineering have to do if this project is implemented?_