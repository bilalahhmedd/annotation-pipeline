# annotation-pipeline
Annotation pipeline is critical to ensure good quality data for ai applications.
This is implementation of annotation pipeline containing multiple components.

# Overview

This project comprises following stages.

* setting up data layer
* setting up label-studio app
* orchestration 
* annotation application deployment

# Dependencies

* docker
* label-studio:1.3.0
* python: 3.8.0
* salenium

# Architecture

Create labeling tasks
        |
Images data
        |
Label studio app
        |
Label studion configs 
        |
Annotation App Launch 

Tech Stack: Python, Bash, Docker, Label-studio
Data Format: Json, CSV, Yml, JPG

****************************************************************************************

# System Components

1. Data Service Layer
   * feed data
        * create labeling tasks json files
        * place these task files in multiple subfolders, where each folder serves data to each annotator project in label-studio app
   * consume annotated data
        * create folders inside annotation_results folder to land annotated data coming from each annotator project of app saparately.
   * Images 
        * Single source folder to contain all images for app 
        * copy these images into Images folder residing in server-folder of label-studio app
        

****************************************************************************************

2. Label-studio App setup

    * Docker image "heartexlabs/label-studio:1.3.0"
    * Docker container "label_studio_annotator_container"
    * integrate data service layer into label-studio interface
    * launch annotation labeling app
    * label studio labeling configs

****************************************************************************************
3. Orchestration
   
   * launch_annotation_labeling_app.sh
        * app configuration
        * create annotation app folder
        * call python scripts to create data service layer
        * create server folder inside annotation app folder
        * docker run command to pull label-studio image, integrate data service layer into label-studio interface


    