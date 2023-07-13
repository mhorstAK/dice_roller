# dice_roller
This is a Dice Rolling Simulation

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

##### Method 2 starting APP

docker-compose down
docker-compose build
docker-compose up

#### Starting the containers
Navigate to the directory containing your docker-compose.yml file.

Run the following command to start the containers:

Copy code
`docker-compose up -d`

The -d flag runs the containers in detached mode, which means they'll run in the background without occupying your terminal. Docker Compose will automatically start the containers based on the configuration in the docker-compose.yml file.

#### Stopping the containers
Navigate to the directory containing your docker-compose.yml file.

Run the following command to stop the containers:

Copy code
`docker-compose down`

This command will stop and remove the containers defined in your docker-compose.yml file. Note that volumes defined in the file will not be removed by default. 

Restarting the containers
If you want to restart the containers without removing them, you can use the following command:

#### Copy code
docker-compose restart
This command will restart the containers defined in your docker-compose.yml file, preserving the existing volumes.

By using these commands, you can easily start, stop, and restart your containers while ensuring that the necessary dependencies and relationships between containers are maintained.

