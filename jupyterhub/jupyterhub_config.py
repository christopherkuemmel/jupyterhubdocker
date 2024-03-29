from oauthenticator.gitlab import GitLabOAuthenticator
import os

# general dockerspawner & jupyterhub setup
cuda_installed = os.environ['CUDA_INSTALLED']
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# add admins
c.Authenticator.admin_users = {'ckuemmel', 'khildebrand'}

# whitelist users
c.Authenticator.whitelist = {'ckuemmel', 'khildebrand'}

# nvidia-docker setup
if 'yes' in cuda_installed:
    c.DockerSpawner.extra_create_kwargs = {'runtime': 'nvidia'}
    c.DockerSpawner.extra_host_config = {'runtime': 'nvidia'}

# overwrite dockerspawner cmd
c.DockerSpawner.extra_create_kwargs.update({
	'command': 'jupyterhub-singleuser --ip=0.0.0.0'

    ## Other commands, for dev purposes
	# 'command': 'bash /usr/local/bin/start-singleuser.sh'
	# 'command': 'jupyter lab --ip=0.0.0.0 --port=8888'
})

c.Spawner.default_url = '/lab'

## Configure authentication (delagated to GitLab)
c.JupyterHub.authenticator_class = GitLabOAuthenticator

# user data persistence
notebook_dir = '/home/user/workdir'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }