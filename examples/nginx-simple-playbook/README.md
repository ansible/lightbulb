# nginx-simple-playbook

This example is designed to be used as a quick introduction to playbook structure that can easily fit on one slide deck that demonstrates how Ansible works.

This playbook assures the hosts in a group called "web" has the Nginx web server present and is started with a static custom home page. The hosts are presumed to be running a Red Hat family linux.

This example assumes that the EPEL repo has already be enabled on each host. This was intentionally left out to keep this example simple and focused.

The playbook is intended for demonstration and instructional purpose. In reality it's too simplistic to be really useful. See `examples/nginx-basic-playbook` for a more complete example using nginx.
