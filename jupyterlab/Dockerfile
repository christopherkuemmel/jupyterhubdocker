FROM pytorch/pytorch:1.1.0-cuda10.0-cudnn7.5-devel

# install jupyterhub/lab/notebook dependecies
RUN conda install --quiet --yes \
    'notebook=5.7.8' \
    'jupyterhub=0.9.6' \
    'jupyterlab=0.35.5' \
    && conda clean -ya

RUN conda install --quiet --yes \ 
    matplotlib \
    scipy \
    scikit-learn \
    numpy \
    pandas \
    pandas-profiling \
    && conda clean -ya

RUN pip install \
    nibabel \
    tensorflow-gpu \
    opencv-python

# create new user without sudo
RUN groupadd -r user && useradd -ms /bin/bash --no-log-init -r -g user user
USER user

# define workdir for notebook
RUN mkdir /home/user/workdir
WORKDIR /home/user/workdir

CMD ["jupyterhub-singleuser", "--ip=0.0.0.0"]