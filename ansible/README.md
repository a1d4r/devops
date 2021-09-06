### Install roles from Ansible Galaxy
```
ansible-galaxy role install geerlingguy.docker geerlingguy.pip weareinteractive.apt
```

### Run playbooks
#### Install docker
```
ansible-playbook playbooks/install_docker.yml
```