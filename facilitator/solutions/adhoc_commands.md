# Workshop: Ad-Hoc Commands

This brief exercise demonstrates Ansible in-action at it's most basic and simple level. Thru ad-hoc commands, students are exposed to Ansible modules and usage and will apply to their understanding of tasks and playbooks. This exercise also begins to expose students to the concepts of Ansible facts and inventory.

This workshop is also a good way to verify their lab environments are properly configured before going forward.

## Solution

The following commands are the solution for the workshop and extra credit assignments.

```bash
ansible all -m ping

ansible all -m setup

ansible web -b -m yum -a "name=epel-release state=present"
ansible web -b -m yum -a "name=https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm state=present"

---

ansible all -m setup -a "gather_subset=virtual"

ansible all -m setup -a "filter=ansible_fqdn*"

ansible all -m command -a "uptime"

ansible all -m ping --limit '!control'
```

### NOTE

You will need to make sure each student successfully installed the EPEL repo here. Later workshop assignments ask students to install Nginx. Without EPEL enabled on each web host `yum` will not be able to locate the package.
