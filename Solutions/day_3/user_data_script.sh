#!/bin/bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y python3
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install -y ansible
sudo apt install -y git
cd /etc/ansible
sudo bash -c 'echo -e "[webservers]\nlocalhost" >> /etc/ansible/hosts'
cd /home/ubuntu/.ssh
ssh-keygen -t rsa -N '' -f ~/.ssh/id_rsa <<< y
touch /home/ubuntu/.ssh/authorized_keys
sudo chmod 0700 /home/ubuntu/.ssh
sudo chmod 0645 /home/ubuntu/.ssh/authorized_keys
sudo cat /home/ubuntu/.ssh/id_rsa.pub >> /home/ubuntu/.ssh/authorized_keys
cd /home/ubuntu
git clone https://github.com/prajulchauhan/AWS.git
cd /home/ubuntu/AWS
sudo chown -R $USER: .
git checkout -b develop
git pull origin develop
cd /home/ubuntu/AWS/Solutions/day_3/
ansible-playbook webserver.yml
