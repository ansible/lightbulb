# nginx-roles

This example demonstrates how roles are structured and used in a playbook. In communicating these concepts, this example is simply a refactoring of the `nginx-basic-playbook` and `nginx-remove-playbook` examples into a role.

This example requires Ansible v2.2 or later. It uses the `include_role` module that introduced in that version.

This also example assumes that the EPEL repo has already be enabled on each host. This was intentionally left out to keep this example focused.

This example is also the solution to the primary assignment and extra credit assignments in `workshop/roles`.
