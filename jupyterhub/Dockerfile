# # Do not forget to pin down the version
FROM jupyterhub/jupyterhub:0.9.4

# Copy the JupyterHub configuration in the container
COPY jupyterhub_config.py .

# Install dependencies (for advanced authentication and spawning)
RUN pip install \
    dockerspawner==0.10.0 \
    oauthenticator==0.8.0