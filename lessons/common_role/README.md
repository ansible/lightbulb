# common_role

If you haven't done so already:

	vagrant up node-1 node-2 node-3 haproxy

This brings up another node.  


### Topics Covered

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
* using host ranges
* using registered variables
* setting facts
* using group_by

### Requirements

You'll need your AWS credentials configured either in ```$HOME/.boto``` or set in environment variables.  You'll also need your AWS ssh key in your keychain (using ssh-add). 


### General flow

* Add a new haproxy role
* Add new code to the infra role for a ec2 haproxy instance
* update the playbook to use the common role

### Commands


	# provision the infrastructure
	ansible-playbook infra.yml -e "key_name=my_ec2_key" -i inventory/ec2.py
	
	# provision the apps
	ansible-playbook site.yml -e @secrets.yml --ask-vault-pass -i inventory/cloud
	ansible-playbook site.yml -e @secrets.yml --ask-vault-pass -i inventory/local