# role_deps

If you haven't done so already:

	vagrant up node-1 node-2 node-3 haproxy

This brings up another node.  Other changes made:

* Adding new haproxy role
* Adding new code to the infra role for a ec2 haproxy instance
* Making the apache module depend on the common module


Once that is setup, just run:

    #ensure that ec2 cache is purged
    rm -rf ~/.ansible/tmp/ansible-ec2.*
    
	# provision the infrastructure
	ansible-playbook infra.yml 
	
	# provision the apps
	ansible-playbook site.yml -e @secrets.yml --ask-vault-pass