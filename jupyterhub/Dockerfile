# # Do not forget to pin down the version
FROM jupyterhub/jupyterhub:1.0.0

# Copy the JupyterHub configuration in the container
COPY jupyterhub_config.py .

# Install dependencies (for advanced authentication and spawning)
RUN pip install \
    dockerspawner==0.11.1 \
    oauthenticator==0.10.0