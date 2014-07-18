# apache-centos-ubuntu

If the nodes aren't already up, you'll need to run:

	vagrant up node-1 node-2 node-3
	
	
We're adding a new node this time, and it just so happens to be an Ubuntu node.  Now that's going to require some changes to our role:

* Seperate task files or each OS, included conditionally based on OS, to account for yum and apt tasks.
* Seperate var files, included based on OS, to account for different in package and service names between OSes.


We are also showing how to use host_vars to override the apache_test_message default.

No problem though, we still run the playbook in the same way.


	ansible-playbook site.yml