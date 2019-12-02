FROM pytorch/pytorch:1.3-cuda10.1-cudnn7-devel

# update package manager and install base deps
RUN apt-get update \
    && apt-get install -y libsm6 libxext6 libxrender-dev

# install jupyterhub/lab/notebook dependecies
RUN conda install --quiet --yes \
    'notebook=6.0.*' \
    'jupyterhub=1.0.*' \
    'jupyterlab=1.2.*' \
    && conda clean -ya

# install default datascience deps
RUN conda install --quiet --yes \ 
    matplotlib \
    scipy \
    scikit-learn \
    numpy \
    pandas \
    pandas-profiling \
    && conda install --quiet --yes -c conda-forge \
    nodejs \
    && conda clean -ya

RUN pip install \
    nibabel \
    tensorflow-gpu \
    opencv-python

# create new user without sudo
RUN groupadd -r user && useradd -ms /bin/bash --no-log-init -r -g user user
USER user

COPY jupyter_notebook_config.py /home/user/.jupyter/jupyter_notebook_config.py

# define workdir for notebook
RUN mkdir /home/user/workdir
WORKDIR /home/user/workdir

CMD ["jupyterhub-singleuser", "--ip=0.0.0.0"]