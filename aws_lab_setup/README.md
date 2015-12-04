Ansible AWS training provisioner
================================

This is an automated lab setup for ansible training. It creates 5 nodes per user in the `users` list.

* One control node from which ansible will be executed from
* Three web nodes that coincide with the three nodes in lightbulbs original design
* And one node where haproxy is installed (via lightbulb lesson)

Usage
-----

Ensure you have boto installed and configured, and that your public key is installed in the target region. The lab will get created in us-west-1 by default.

Add users and their emails to the users list in defaults/main.yml
```yml
users:
  - username: jdavila
    email: jdavila@ansible.com
  - username: jdoe
    email: jdoe@example.com
```

Inside of group_vars/localhost/ specify your SendGrid credentials

```yml
sendgrid_user: example
sendgrid_pass: password
```


Then to setup the lab:

```
ansible-playbook -i hosts infra-aws.yml -e "name_prefix=(yourname)-training aws_key_name=your-pubkey-name instructor_email=youremail@example.com"
```

The playbook will start the instances, configure them for password auth, and dump an ansible inventory  file for each user with their IPs and credentials into the current directory, then it will email every user their respective inventory file. This will also generate an 'instructor' inventory file in the current directory which will let the instructor access the nodes of any student by simply targeting the the username as a host group.

