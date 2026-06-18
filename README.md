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

* Data Service Layer
   * create labeling task
        * create folders for annotation
        * divide images dataset into muliple subfolders
    * images

****************************************************************************************

*   Label-studio App setup
    
    * launch annotation labeling app
    * label studio labeling configs

****************************************************************************************


    