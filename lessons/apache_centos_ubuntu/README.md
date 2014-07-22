# apache-centos-ubuntu

If the nodes aren't already up, you'll need to run:

	vagrant up node-1 node-2 node-3

### Topics covered

* playbook
* inventory
* roles
* tagging
* include_vars
* conditionals
* seperate task files
* host_vars

### General Flow	

	
We're adding a new node this time, and it just so happens to be an Ubuntu node.  Now that's going to require some changes to our role.

We are also showing how to use host_vars to override the apache_test_message default.

No problem though, we still run the playbook in the same way.

### Commands

	ansible-playbook site.yml