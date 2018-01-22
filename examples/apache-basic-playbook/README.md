# apache-basic-playbook

This example represents a basic yet complete playbook approximating the typical tasks used to deploy and configure a single application service (Apache) on a host running a Red Hat family linux.

This playbook assures the hosts in a group called "web" has the Apache web server (httpd) present and is started. The play also generates a basic configuration and custom home page using templates. If the configuration is changed, a handler task will execute to restart the apache httpd service.
