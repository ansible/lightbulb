# apache-centos

If the nodes aren't already up, you'll need to run:

	vagrant up node-1 node-2


Well plain-old playbooks are not very re-usable.  So here we've taken the same concepts in the apache-paybook example and built an apache role.  

Features demonstrated:

* roles
* tagging

To run the playbook:

	ansible-playbook site.yml