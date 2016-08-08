# Workshop: Ad-Hoc Commands

### Topics Covered

* ansible installation
* ansible.cfg
* modules
* command-line options: ```-i -u -m -a```

### The Assignment

Perform the following operations using ad-hoc commands:

1. Test Ansible is setup correctly to communicate with your web nodes using the ping module.
1. Install the latest `epel-release` on the web nodes using the yum module. (Use `https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm` on RHEL).
1. Install `nginx` using the yum module on the web nodes.
1. Start `nginx` on the web nodes using the service module.

