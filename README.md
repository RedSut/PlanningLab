# Planning-Lab

Code for the Planning lab of *Planning and Automated Reasoning* course, MSc degree in Artificial Intelligence 2023/2024, University of Verona

## Setup 

1. Download [Anaconda](https://www.anaconda.com/distribution/#download-section) for your System.

2. Install Anaconda and Git:
   - On **Linux/Mac**: 
     - `sh Anaconda{version}.sh` to install the Anaconda version chosen.
     - Could be necessary to update your *.bashrc* file writing this line: *export PATH=~/anaconda3/bin:$PATH* then save and close the *.bashrc* file.
     -  Open a terminal and digit: `source ~/.bashrc`
     - Install Git: `sudo apt-get install git` 

   - On **Windows**:
     - Double click the installer to launch.
     - *NB: during the installation, ensure to install "Anaconda Prompt" and use it for the other steps.*
     - Install Git: download [here](https://gitforwindows.org/)

3. Setup Conda environment:
   - `git clone https://github.com/vrncst/PlanningLab`
   - `conda env create -f tools/planning-lab-env.yml`

   

## Using the Jupyter Notebook

To start the environment and work on your assignments, navigate to the downloaded folder root *(Planning-Lab)* and run:

```
conda activate planning-lab
jupyter notebook
```

The last command will open your browser for you to start working. To open the tutorial navigate with your browser to the current lesson notebook (*Lesson_\*/lesson_\*_problem.ipynb*).



## Authors

*  **Celeste Veronese** - celeste.veronese@univr.it
*  **Alessandro Farinelli** - alessandro.farinelli@univr.it



## Acknowledgments

Environments are based on OpenAI Gym: https://github.com/openai/gym
Material based on the previous version of the course, provided by Luca Marzari - luca.marzari@univr.it
