# apache-basic-playbook

This example represents a basic yet complete playbook approximating the typical tasks used to deploy and configure a single application service. 

This playbook assures the hosts in a group called "web" has the Apache web server (httpd) is present and is started. The play also generates a basic configuration and custom home page using templates. If the configuration is changed, a handler task will execute to restart the apache httpd service.
