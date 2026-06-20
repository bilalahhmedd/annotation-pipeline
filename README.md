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
        * create annotation tasks (folder containing json files). \n 
        * create labeling tasks json files and place those in multiple subfolders as per number of annotators and repetition of each image
   * consume annotated data
        * create folders for each annotator project to land annotated data saparately, coming from label-studio app
   * Images 
        * images reside in one main folder called Images
        * Images folder reside in server-folder of label-studio app
        

****************************************************************************************

*   Label-studio App setup
    
    * launch annotation labeling app
    * label studio labeling configs

****************************************************************************************


    