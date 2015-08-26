Activity for Advanced Templating:
=================================

### Topics Covered

* Complex Variable Use
* Loops
* Decisioning
* Filters

The reference folder is provided to teach specific points about templating:

### General flow

All playbooks provided in this section run against localhost. If you are testing a template for vagrant hosts, you'll need to add the hosts to inventory/hosts and 
provide all vars needed to render the playbook in vars.yml

### Commands

Using the playbook:

```
ansible-playbook -i inventory/hosts templates.yml
```

Activity:

Create template for iptables config file that does the following:

* if, elif decisioning 
* nested inside this is a for loop to place rules for hostgroups
* in that for loop, we access specific host variables

### Reference:

http://jinja.pocoo.org/docs/dev/templates/

* For Decisioning:
http://jinja.pocoo.org/docs/dev/templates/#tests
http://jinja.pocoo.org/docs/dev/templates/#if
http://jinja.pocoo.org/docs/dev/templates/#list-of-builtin-tests

* For Looping:
http://jinja.pocoo.org/docs/dev/templates/#for
http://jinja.pocoo.org/docs/dev/templates/#macros
http://jinja.pocoo.org/docs/dev/templates/#call

* For Filters:
http://jinja.pocoo.org/docs/dev/templates/#id11
http://jinja.pocoo.org/docs/dev/templates/#builtin-filters
https://docs.ansible.com/ansible/playbooks_filters.html#other-useful-filters

* Complex Variable Use:
http://jinja.pocoo.org/docs/dev/templates/#variables
http://jinja.pocoo.org/docs/dev/templates/#assignments
http://jinja.pocoo.org/docs/dev/templates/#block-assignments
http://jinja.pocoo.org/docs/dev/templates/#filters
http://jinja.pocoo.org/docs/dev/templates/#list-of-global-functions

* Other:
http://jinja.pocoo.org/docs/dev/templates/#expressions
http://jinja.pocoo.org/docs/dev/templates/#whitespace-control (Note trim_blocks is called in the template module)