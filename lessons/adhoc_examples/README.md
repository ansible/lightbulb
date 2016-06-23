# ad-hoc examples

### Topics Covered

* ansible installation methods
* ad-hoc ansible
* command-line options: ```-i -u -m -a```
* using ansible.cfg


### Commands

Install ansible with yum, but explain other methods (brew, pip, apt, etc)

	yum install ansible

Run the following commands and experiment:

	ansible web -i inventory/hosts -m setup

	ansible web -i inventory/hosts -m yum -a "name=httpd state=present" -s

Specifying the inventory is annoying, so open up ansible.cfg and uncomment the entries for hostfile.

	ansible web -m service -a "name=httpd state=started" -s

	ansible web -m service -a "name=httpd state=stopped" -s

	ansible web -m yum -a "name=httpd state=absent" -s


Imagine the calories saved by less typing.
