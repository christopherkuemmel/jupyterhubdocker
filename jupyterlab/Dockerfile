FROM anibali/pytorch:cuda-10.0

# install jupyterhub/lab/notebook dependecies
RUN conda install --quiet --yes \
    'notebook=5.7.8' \
    'jupyterhub=0.9.6' \
    'jupyterlab=0.35.5' 

# define workdir for notebook
RUN mkdir /home/user/workdir
WORKDIR /home/user/workdir

CMD ["jupyterhub-singleuser --ip=0.0.0.0"]