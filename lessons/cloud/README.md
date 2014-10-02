# cloud

If you haven't done so already:

	vagrant up node-1 node-2 node-3

### Topics covered

This is our foray into dynamic inventories and provisioning cloud instances.  This example shows the following concepts:

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


### Requirements

You'll need your AWS credentials configured either in ```$HOME/.boto``` or set in environment variables.  You'll also need your AWS ssh key in your keychain (using ssh-add).  

### General flow

Show how ec2.py creates the groups.  Show some of the settings for ec2.ini.

Show the different inventory directories, and the aliases/child groups made in inventory/cloud.  This allows use to use the same playbook in both environments, but only having to change the inventory file.  

We also wanto to show how to use extra vars, so there is a ansible-vaulted file named secrets.yml, with the password of: ```password```.  Changing this will override the test message on the web pages.

You'll also have to override my key_name parameter for the infra role to something that you actually have -- you could that with extra vars or by sending the parameter to the role.


### Commands


	# provision the infrastructure
	ansible-playbook infra.yml -e "key_name=my_ec2_key" -i inventory/ec2.py
	
	# provision the apps
	ansible-playbook site.yml -e @secrets.yml --ask-vault-pass -i inventory/cloud
	ansible-playbook site.yml -e @secrets.yml --ask-vault-pass -i inventory/local