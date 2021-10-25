FROM ubuntu:latest

RUN apt update && apt install  openssh-server sudo -y

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 test 

RUN echo 'test:test' | chpasswd

RUN service ssh start


#add docker cli 
RUN apt-get update && apt-get -y install \
            apt-transport-https \
            ca-certificates \
            curl \
            software-properties-common \
            gnupg

RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

#architecture => dpkg --print-architecture
#Distributor => lsb_release -is
#Codename => lsb_release -cs
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian  buster  stable" 
RUN apt-get update && apt-get -y install docker-ce-cli

RUN groupadd docker
RUN usermod -aG docker test

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]
