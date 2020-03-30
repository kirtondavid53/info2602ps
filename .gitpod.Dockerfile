FROM gitpod/workspace-full
                    
USER gitpod
RUN npm i -g npm newman mocha

USER root
RUN sudo apt-get update

RUN curl https://cli-assets.heroku.com/install-ubuntu.sh | sh

# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
# RUN sudo apt-get -q update && #     sudo apt-get install -yq bastet && #     sudo rm -rf /var/lib/apt/lists/*
#
# More information: https://www.gitpod.io/docs/config-docker/