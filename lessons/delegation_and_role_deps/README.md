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


Adds a new lameapp role that depends on apache role.  lameapp is a very simple python script. Show that lameapp role has passed a parameter to the apache role.  Show the custom filters.  Show how the rolling restart and delegation works and the custom modules.

The app is hosted at: http://10.42.0.100/lame

The vault password is 'password'.

### Rolling restart flow

The ```lameapp_version``` is found in the ```group_vars/all``` file.

1. Default deployment is version 1.1
2. upgrade to version 1.2, using rolling_update playbook
3. try to upgrade to version 1.3 using rolling update playbook
4. note failure, revert back to version 1.2

Command to revert to previous version:
	
	ansible-playbook rolling_update.yml -v --limit 10.42.0.6,haproxy -i inventory/local



### Commands


	# provision the infrastructure
	ansible-playbook infra.yml -e "key_name=my_ec2_key" -i inventory/cloud
	
	# provision the apps
	ansible-playbook site.yml -e @secrets.yml --ask-vault-pass -i inventory/cloud
	ansible-playbook site.yml -e @secrets.yml --ask-vault-pass -i inventory/local
