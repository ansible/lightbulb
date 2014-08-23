# apache-centos

If the nodes aren't already up, you'll need to run:

	vagrant up node-1 node-2

### Topics covered

* playbook
* inventory
* initializing a role
* roles
* tagging
* templates


### General flow

Plain-old playbooks are not very re-usable.  So here we've taken the same concepts in the apache-paybook example and built an apache role.  


### Commands

	ansible-playbook site.yml
