FROM python:latest

# Update system and install Vim
RUN apt-get update \ 
&& apt-get install -y \
    vim \
    curl \
    bash \
    sudo \
    docker.io \
    jq

# Install horusec
RUN curl -fsSL https://raw.githubusercontent.com/ZupIT/horusec/main/deployments/scripts/install.sh | bash -s latest

# Install Django and Pillow
RUN pip install django \
&& pip install Pillow \
&& pip install debugpy \
&& pip install psycopg \
&& pip install daphne \
&& pip install channels \
&& pip install gitpython \
&& pip install validators \
&& pip install semgrep

#Create entrypoint command
ENTRYPOINT python -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:5678 /opt/CodeAnalizer/manage.py runserver 0.0.0.0:8000
