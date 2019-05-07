# JupyterHub

This repository contains a JupyterHub setup for a *medium-scale* deployment, e.g., a single server with a docker installation and access to GPUs.
Accessing the JupyterHub with an OAuth GitLab authentication, the environment will spawn a new docker container for the user.

## TOC

- [JupyterHub](#jupyterhub)
  - [TOC](#toc)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Authentication & Security](#authentication--security)
  - [Usage](#usage)
  - [References](#references)
  - [License](#license)

## Installation

Since this project provides a docker setup, there is little installation processes to be made. 
However, there are some requirements and parameters to define.
The `jupyterhub/jupyterhub_config.py` file will define all JupyterHub related settings, while the `docker-compose.yml` will define all container relevant information.

### Requirements

1. Running docker and docker-compose instance
2. NVIDIA graphics card
3. NVIDIA-Driver version >= 410 
4. nvdia-docker v2

### Authentication & Security

1. In order to use **OAuth** you have to create an `.env` file in the root directory which contains two parameters:
   1. CLIENT_ID=<YOUR_ID>
   2. CLIENT_SECRET=<YOUR_SECRET>
2. Moreover you have to specifiy the GitLab specific URL and HOST in the `docker-compose.yml`:
   1. OAUTH_CALLBACK_URL
   2. GITLAB_HOST

## Usage

Starting the system:

* `docker-compose up`: will build and start the system
  * `-d`: will start the system in detached mode, so you can safely close the terminal session
* `docker-compose down`: will shutdown the hub, but not all other active notebook containers! If there are some running after you shutdown the system, you manually have to stop and remove them.


## References

1. https://opendreamkit.org/2018/10/17/jupyterhub-docker/ 
2. https://jupyter.org/hub
3. https://github.com/jupyterhub/dockerspawner

## License

Until now, JupyterHub is for internal use only.