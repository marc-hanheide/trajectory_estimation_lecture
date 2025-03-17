# Lecture Materials for "Trajectory Estimation" Module

<a target="_blank" href="https://colab.research.google.com/github/marc-hanheide/trajectory_estimation_lecture">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## Repository Overview

This repository contains lecture materials for the "Trajectory Estimation" module, including:

- Jupyter notebooks with interactive examples and exercises
- Code implementations
- Practical examples and case studies
- Supporting data files for exercises

The materials can be accessed and run interactively through Google Colab by clicking the badge above, allowing students to experiment with the code without requiring local installation.

The repository is structured to follow the module's curriculum, covering fundamental concepts to advanced topics in trajectory estimation techniques.

It also offers a ROS2 development environment (devContainer) for students to practice with real-world data and scenarios.


## Local Python Installation

1. create a virtual environment: `python3 -m venv .venv`
2. activate the virtual environment: `source .venv/bin/activate`
3. install the required packages: `pip install -r requirements.txt`

## Run local Jupyter notebook server

1. start the Jupyter notebook server: `jupyter lab --config ./jupyter_lab_config.py`

## Generate slides

`jupyter nbconvert --config mycfg.py`