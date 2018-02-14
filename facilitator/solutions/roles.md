# Workshop: Roles

Here students are tasked with refactoring their previous work from the Basic Playbook workshop into a role and modifying their playbook accordingly. We intentionally avoid introducing any new tasks or functionality otherwise. The objective here is to focus students specifically on how roles are structured and develop.

You should emphasize the value of roles in better organizing playbooks as they grow in sophistication and making Ansible automation more portable and reusable than a basic playbook.

## Defaults vs. Vars

A common question that is asked "when do I put a variable in defaults instead of a vars?" It depends on the usage of a variable in the context of a role. It all comes down to variable precedence.

If a variable holds a data that someone using the role may want to override anyway numbers of ways, then it's best stored under `defaults/`. If a variable holds data that is internal to the function of the role and rarely (or in practice should never) be modified, then it's best stored under `vars/` where its much hard to be overridden by other variables sources.

Applying these guidelines to this assignment, `nginx_packages` would go in `vars/` while `nginx_test_message` and `nginx_webserver_port` would go in `defaults/`.

## NOTE

The extra credit assignment should use the `include_role` module that was introduced in version 2.2. Students working with older versions of Ansible will have trouble completing the assignment.

## Solution

The solution to this workshop is `nginx-role` under `examples/`. This example also includes the solution to the extra credit assignment. See `remove.yml` and `roles/nginx-basic/tasks/remove.yml`.
