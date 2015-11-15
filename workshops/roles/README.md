# Workshop: Roles

### Topics Covered

This workshop builds on your assignment from the prior basic playbook workshop. This workshop challenges you to make your work more reusable by refactoring what you've done in to a role. In this workshop will exercise the following concepts:

* roles structure and behavior
* using roles in playbooks
* parameterizing roles
* defaults values
* creating a configuration file with a template

### The Assignment

Refactor your basic collectd playbook in to a role with the following added features:

* Generates a configuration file
* The configuration can be modified thru parameters passed in to the role.
* Has default values if a configuration (role) parameter is not passed in.

Create a simple playbook that uses the role and passes one parameter to the role.

The file collectd.conf.example has been provided to help get you started.

### Requirements

You will need to have the EPEL repo enabled on your remote nodes.