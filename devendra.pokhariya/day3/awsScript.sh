#!/bin/bash
function installPrequisiteApplication(){
sudo apt install -y python # Pyhton interprator
sudo apt install software-properties-common 
sudo apt-add-repository -y ppa:ansible/ansible
sudo apt update
sudo apt install -y ansible # Ansible to run role
sudo apt install -y git # git for clonning 
sudo apt install -y nginx # and nginx server to serve page

runRoleFromGit
    

}

function runRoleFromGit (){
    git clone https://gitlab.com/devendra.pokhariya/my-own-repo.git
    cd my-own-repo
    ansible-playbook -i inventory nginxIndexPage.yml --extra-vars "yourname=Devendra Pokhariya"
}

installPrequisiteApplication
