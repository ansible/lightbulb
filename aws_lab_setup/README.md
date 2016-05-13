Ansible AWS training provisioner
================================

This is an automated lab setup for ansible training. It creates 5 nodes per user in the `users` list.

* One control node from which ansible will be executed from
* Three web nodes that coincide with the three nodes in lightbulbs original design
* And one node where haproxy is installed (via lightbulb lesson)

Usage
-----

## AWS Setup
To set up the lab for Ansible training in EMEA, follow these steps. I've done this using the eu-west (Ireland) datacentre, so you will need to modify if you want to use eu-central (Frankfurt) - in particular the AMI IDs may be different.

1. Create an Amazon AWS account registered to your Red Hat email address and credit card if you do not have one already.

2. Create an ssh key pair called 'ansible' (Network & Security->Key Pairs->Create Key Pair). Download the private key to your .ssh directory, e.g. to .ssh/ansible.pem. Alternatively, you can upload your own public key into AWS

If using an AWS generated key add it to the ssh-agent:

ssh-add ~/.ssh/ansible.pem

3. Login to the EC2 dashboard at https://eu-west-1.console.aws.amazon.com/ec2/v2/home?region=eu-west-1# (this is for eu-west) and create a VPC with a single public subnet. Make note of both the VPC and Subnet IDs. 


4. Create a free sendgrid account if you don't have one at sendgrid.com, and
record your credentials.

5. Install the sendgrid python library:

`pip install sendgrid`

6. Clone the lightbulb repo:

```
git clone ssh://git@gitlab.consulting.redhat.com:2222/jammarti/lightbulb.git 
cd lightbulb/aws_lab_setup
```

7. Edit aws_lab_setup/infra-aws.yml to add your (instructor) email
address:

```
@@ -37,4 +37,4 @@
   roles:
     - role: training_infra
     -        email: yes
     -        -      instructor_email: jdavila@redhat.com
     -        +      instructor_email: nstrug@redhat.com
8. Edit aws_lab_setup/roles/training_infra/defaults/main.yml to use
AMIs available in eu-west:

@@ -20,19 +20,19 @@ instance_types:
     os_type: linux
     disk_space: 20
   rhel7:
-    ami_id: ami-12663b7a
-    +    ami_id: ami-8b8c57f8
-         size: t2.micro
-              os_type: linux
-                   disk_space: 10
-    ami_id: ami-12663b7a
-    +    ami_id: ami-8b8c57f8
-         size: t2.medium
-              os_type: linux
-                   disk_space: 10
```

9. Create a users.yml by copying sample-users.yml and adding all your
students:

e.g.:

```
users:
   - username: foo
     email: foo@redhat.com
   - username: bar
     email: bar@redhat.com
```

10. You should now be able to run the playbook:

$ ssh-add -l     # ensure that your ansible key is loaded into the agent
$ ansible-playbook infra-aws.yml -e "name_prefix=ansible_training aws_key_name=ansible \
        instructor_email=my_emal@redhat.com sendrid_user=my_sendgrid_user \
        sendgrid_pass=my_sendgrid_password"  -e @users.yml

11. Check on the EC2 console and you should see instances being created like:

ansibe_training-<student_username>-node1|2|3|haproxy|tower|control

If successful all your students will be emailed the details of their
hosts including addresses and credentials, and an instructor_inventory
file will be created listing all the student machines.

The playbook will start the instances, configure them for password auth, and dump an ansible inventory  file for each user with their IPs and credentials into the current directory, then it will email every user their respective inventory file. This will also generate an 'instructor' inventory file in the current directory which will let the instructor access the nodes of any student by simply targeting the the username as a host group.

Ensure you have boto installed and configured, and that your public key is installed in the target region. The lab will get created in us-west-1 by default.


