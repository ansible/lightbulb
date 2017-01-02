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

* targets your **entire** inventory
* creates a variable that is a list of `vim` and `https://dl.fedoraproject.org/pub/epel/epel-release-latest-{{ ansible_distribution_major_version }}.noarch.rpm`
* installs the above packages in a loop
* defines a variable named `telegraf_version` and is set to `0.2.4`
* defines a variable named `telegraf_flush_retries` and is set to `2` (integer)
* defines a variable named `influxdb_db_name` that is set to `telegraf`
* defines a variable named `influxdb_url` that is set to `http://localhost:8086`
* copies the yum repository `solution/influxdb.repo.j2` using the template module. (Hint: Repos are located at /etc/yum.repos.d/SOMENAME.repo)
* installs `telegraf-0.2.4` package using the `telegraf_version` variable
* copies `solution/telegraf.conf.j2` to `/etc/opt/telegraf/telegraf.conf` using the template module
* starts and enables the `telegraf` service
* uses a handler to restart the `telegraf` service when the `telegraf` package is installed or the `telegraf` configuration file has changed


Verify that telegraf is working properly by running:

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
