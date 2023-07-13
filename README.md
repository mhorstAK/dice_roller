# DICE ROLLER SIM
This is a Dice Rolling Simulation

Below are some examples of simulations you can run.

Here is a simple histogram of a single roll type (10d20+10 with disadvantage) ran for 5000 simulations:
![Alt text](/read_me_pics/simulated_roll_distrobution.jpg "Distrobution of Simulated Dice Rolls")

Here is a histogram of an advantage roll type (1d20 with advantage) ran for 5000 simulations:
![Alt text](/read_me_pics/simulated_advantage_distrobution.jpg "Distrobution of Advantage Rolls")

Here is a normal distribution built curve from a roll type (3d20+5 with advantage) for 5000 simulation and showing an limit (Dnd AC) of 50. This gives the Win & Lose rate of the simulation as seen in the bottom of the sidebar.
![Alt text](/read_me_pics/simulated_win_lose.jpg "Simulated Win & Lose Ratios")

# Outline
Maintained by Morgan and Michael

1. [Overview](#overview)
1. [Developement Environment Setup](#developement_environment_setup)

## Overview
Repository for...


## Developement Environment Setup
This repository is setup up to run locally inside a docker container. This isolates and environmental variables when developing in this repo from your local machine. Everyone developing in this manor will be developing in the same environment. Below are the steps to help get set up.


#### Things you will need:
1. Visual Studio (VS Code)
2. Docker Desktop or Colima
3. Clone this repository locally


#### Steps:
1. If you are using docker desktop or colima just have it `Running` in the background.
2. Open this project (repo) in VS Code IDE.
3. Download the `Remote Developement` extension (by Microsoft) through the extension button on the left hand toolbar. This should add a green button on the bottom left hand corner of your IDE that has `><` symbols in it.
4. Back to the project folder right click the DockerFile and select `build image`. Press enter if prompted for a image name.
5. Once image is built (can view the build proccess in the IDE terminal) select the green button in the bottom left hand corner of your IDE. Select `reopen in container`. Then select `From 'DockerFile'`. Then select `OK` if prompted again. Your IDE is building a container from the image you just built and is opening up the IDE inside that container.
6. (optional) Add additional extensions for working with jupyter notebooks and python if needed.


#### Environmental Python Packages:

Python package definitions for this environment are located in the `requirements.txt` file. These get loaded when the the environment get built above. If you are needing to add a new python package for developement update the requirments.txt file accordingly. Then delete any previously build container for this repo in either docker desktop or colima. And then repeat the proccess given above starting at step 5 build image.


#### Method 2 starting APP
Close app if app is running.
`docker-compose down`

Builds the image
`docker-compose build`

Start up
`docker-compose up`


#### Starting the containers
Navigate to the directory containing your docker-compose.yml file.

Run the following command to start the containers:

`docker-compose up -d`

The -d flag runs the containers in detached mode, which means they'll run in the background without occupying your terminal. Docker Compose will automatically start the containers based on the configuration in the docker-compose.yml file.


#### Stopping the containers
Navigate to the directory containing your docker-compose.yml file.

Run the following command to stop the containers:

`docker-compose down`

This command will stop and remove the containers defined in your docker-compose.yml file.


`docker-compose restart`

This command will restart the containers defined in your docker-compose.yml file, preserving the existing volumes.

By using these commands, you can easily start, stop, and restart your containers while ensuring that the necessary dependencies and relationships between containers are maintained.


## Running Streamlit Application

Once you build the app you can go to any browser on the system that is hosting the app and typ in `http://localhost:8501/` into the URL.

The app should appear and be interacting. If you select `always rerun` the app will update as soon as the code files are saved making the developement loop very quick.
