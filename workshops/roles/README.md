# Workshop: Roles

### Topics Covered

This workshop builds on your assignment from the prior basic playbook workshop. This workshop challenges you to make your work more reusable by refactoring what you've done in to a role. In this workshop will exercise the following concepts:

* roles structure and behavior
* using roles in playbooks
* parameterizing roles
* defaults values
* creating a configuration file with a template
* using ansible galaxy

### The Assignment

#### Using ansible-galaxy

* Use `ansible-galaxy` to find and install a `influxdb` and a `grafana` role created by James Martin (`jsmartin`). Extra points if you use `requirements.yml`.

#### Refactor your basic playbook to role

Start from the basic playbook you developed in the previous workshop, where you installed and setup `telegraf` on each web node, and refactor into a role. It should have the following features:

* Creates a configuration file that points to the `influxdb` server.
* The configuration can be modified through parameters passed in to the role.
* Has default values if a configuration (role) parameter is not passed in.

#### Playbook Creation

The playbook should be composed of two plays. The first play will target the `grafana` and `influxdb` roles against the `grafana` server in your inventory. Before those roles are executed, use a `pre_task` to setup the `epel-release` package (Use `https://dl.fedoraproject.org/pub/epel/epel-release-latest-{{ ansible_distribution_major_version }}.noarch.rpm` as the package name on RHEL). The second play will target your newly created `telegraf` role against the web nodes in your inventory.

#### Freebies

You will need to pass the `extra_vars.yml` file as extra vars to your ansible-playbook command.

The file `training-dashboard.json` is used to populate a dashboard in `grafana`. When referencing make sure the path to `training-dashboard.json` in vars.yml is relative to the playbook path.

Go to http://your_grafana_ip_here:3000 to login to your grafana server.

The default username and password for grafana is **admin** / **password**.
