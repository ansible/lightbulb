# Workshop: Rolling Restart

### Topics Covered

This workshop begins your foray into developing your first Ansible playbook. In this workshop will exercise the following concepts:

* serial
* delegations
* pre_tasks
* post_tasks

### The Assignment

Your manager wants you to create a playbook to change the `telegraf_flush_retries` value to `3` on all of the servers, but not all at once.  One at a time.  This can be set in the extra_vars.yml file.

The playbook should also:

* Have a task-less play that only collects facts from the grafana server.

* echo to a log file ( /var/log/telegraf-maint.log ) on the grafana server with informational messages showing when the system is under maintenance and when it is over.


```timestamp - inventory_hostname - telegraf begin maintenance```



```timestamp - inventory_hostname - telegraf maintenance over```
