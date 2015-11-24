# Workshop: Rolling Restart

### Topics Covered

This workshop begins your foray into developing your first Ansible playbook. In this workshop will exercise the following concepts:

* serial
* delegations
* pre_tasks
* post_tasks

### The Assignment

Create a basic playbook that On no more than one server at a time

* echos to a log file ( /var/log/telegraf-maint.log ) on the grafana server with informational messages showing when the system is under maintenance and when it is over.


```timestamp - inventory_hostname - telegraf begin maintenance```
    
    
    
```timestamp - inventory_hostname - telegraf maintenance over```
     
	
	
*  Updates the telegraf configuration file on each system.  You can invoke this with an extra_var 
