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

* use ansible-galaxy to install a influxdb role created by Ross McDonald, and a grafana role created by James Martin.

#### Playbook to role

Using the telegraf playbook in the previous workshop, refactor it into a role.  It should have the following features.

* Generates a configuration file that points to the influxdb server.
* The configuration can be modified thru parameters passed in to the role.
* Has default values if a configuration (role) parameter is not passed in.


#### Playbook Creation

The playbook should be composed of 2 plays.  The first play will target the grafana and influxdb roles against your influxdb server.  Before those roles are executed, use a pre_task to setup the epel-release package.


* Generates a configuration file that points to the influxdb
* The configuration can be modified thru parameters passed in to the role.
* Has default values if a configuration (role) parameter is not passed in.

#### Freebies

You will need to pass the `vars.yml` file as extra vars to your ansible-playbook command.  `training-dashboard.json` is used to populate a dashboard in grafana. When referencing make sure the path to `training-dashboard.json` in vars.yml is relative to the playbook path.

The default username and password for grafana is  **admin** / **password**.