# Workshop: Ad-Hoc Commands

### Topics Covered

* ansible installation
* ansible.cfg
* modules
* command-line options: ```-i -u -m -a```

### The Assignment

Install Ansible on your controller machine using pip and then perform the following operations using ad-hoc commands:

1. Test Ansible is setup correctly to communicate with your remote nodes with th ping module.
1. Install the latest ‘epel-release’ package using the yum on all your nodes.
1. Install ‘nginx’ using the yum module on all your nodes.
1. Start ‘nginx’ using the service module.
1. Extra Credit: Save yourself some typing and setup a configuration file.

### Requirements

You will need to have pip installed on your controller machine and the EPEL repo enabled on your remote nodes.
