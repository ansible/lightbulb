# nginx-basic-playbook

This example represents a basic yet complete playbook approximating the typical tasks used to deploy and configure a single application service (Nginx) on a host running a Red Hat family linux.

This playbook assures the hosts in a group called "web" has the Nginx web server along with uwsgi and other build dependencies are present and nginx is started. The play also generates a basic configuration and custom home page using templates. If the configuration is changed, a handler task will execute to restart the nginx service.

This example assumes that the EPEL repo has already be enabled on each host. This was intentionally left out to keep this example focused.

The playbook is also the solution to the primary assignment and one of the extra credit assignments in `workshop/basic_playbook`.
