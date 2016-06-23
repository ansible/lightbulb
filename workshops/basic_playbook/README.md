# Workshop: Basic Playbook

### Topics Covered

This workshop begins your foray into developing your first Ansible playbook. In this workshop will exercise the following concepts:

* playbook struture 
* tasks
* handlers
* loops
* variables

### The Assignment

Create a basic playbook that 

* creates a list as a variable that includes vim & epel-release
* installs the above packages in a loop
* defines a variable named `telegraf_install_version` and is set to `0.2.4`
* defines a variable named `telegraf_flush_retries` and is set to `2` (integer)
* defines a variable named `influxdb_db_name` that is set to `telegraf`
* defines a variable named `influxdb_url` that is set to `http://localhost:8086`
* it should also create the influx yum repository using this template [template](solution/influxdb.repo.j2)
* installs the telegraf package
* configures the telegraf package with a [template](solution/telegraf.conf.j2)
* starts and enables the telegraf client
* uses a handler to notify the restart of the telegraf service when the telegraf package is installed or the telegraf configuration file has changed

The playbook should also (re)start the service up only if necesseary.


You should be able to verify that telegraf is working properly by running:

	[user@node-1]# /opt/telegraf/telegraf -test -config /etc/opt/telegraf/telegraf.conf
	* Plugin: cpu, Collection 1
	> cpu_time_user,cpu=cpu0 value=25.99 1448378995373412842
	> cpu_time_system,cpu=cpu0 value=18.56 1448378995373448280
	> cpu_time_idle,cpu=cpu0 value=3605.88 1448378995373456059
	> cpu_time_nice,cpu=cpu0 value=0 1448378995373463851
	> cpu_time_iowait,cpu=cpu0 value=5.81 1448378995373470204
	> cpu_time_irq,cpu=cpu0 value=0.01 1448378995373477438
	> cpu_time_softirq,cpu=cpu0 value=2.69 1448378995373487361
	> cpu_time_steal,cpu=cpu0 value=0 1448378995373494417
	> cpu_time_guest,cpu=cpu0 value=0 1448378995373500291
	> cpu_time_guest_nice,cpu=cpu0 value=0 1448378995373506909
