# apache_playbook

If the nodes aren't already up, you'll need to run:

	vagrant up node-1 node-2


### Topics covered

* Inventory
* Creating a playbook.
* Using vars
* Using with_items
* Using host ranges

### General flow

Configuring systems with ad-hoc tasks can be annoying -- and ad-hoc tasks don't really keep a good record of how a system ***should*** be configured.


In this example, we show how to use a simple playbook to setup Apache on 2 hosts.


	ansible-playbook site.yml