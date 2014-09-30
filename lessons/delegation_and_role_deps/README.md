# common_role

If you haven't done so already:

	vagrant up node-1 node-2 node-3 haproxy

This brings up another node.  


### Topics Covered
* custom filters
* pre and post tasks
* serial
* delegation
* custom modules (haproxy)
* role dependencies (parameterized)
* looping with array of dictionaries for user information
* using a common role
* ansible-vault
* inventory groups and child groups
* roles
* tagging
* include_vars
* conditionals
* seperate task files
* using mixed static/dynamic inventories
* using group_vars to set the remote user
* provisioning instances and using wait_for
* including playbooks within playbooks
* using extra vars
* using ignore_errors
* using host ranges
* using registered variables
* setting facts
* using group_by
* role dependencies
* custom library

### General flow


Adds a new lameapp role that depends on apache role.  Show that lameapp role has passed a parameter to the apache role.  Show the custom filters.  Show how the rolling restart and delegation works and the custom modules.

### Commands


	# provision the infrastructure
	ansible-playbook infra.yml -e "key_name=my_ec2_key" -i inventory/ec2.py
	
	# provision the apps
	ansible-playbook site.yml -e @secrets.yml --ask-vault-pass -i inventory/ec2.py
	ansible-playbook site.yml -e @secrets.yml --ask-vault-pass -i inventory/hosts