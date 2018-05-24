# Ansible AWS training provisioner

This provisioner automatically sets up lab environments for Ansible training. It creates four nodes per student/user.

* One control node from which Ansible will be executed from and where Ansible Tower can be installed
* Three web nodes that coincide with the three nodes in Lightbulb's original design
* And one node where `haproxy` is installed (via Lightbulb lesson)

## AWS Setup

The setup of the environments is done via Ansible playbooks, the actual VMs are set up on AWS. The `provision_lab.yml` playbook creates instances, configures them for password authentication and creates an inventory file for each user with their IPs and credentials. An instructor inventory file is also created in the current directory which will let the instructor access the nodes of any student by simply targeting the username as a host group. The lab is created in `us-east-1` by default.  Currently the setup only works with `us-east-1`, `us-west-1`, `eu-west-1`, `ap-southeast-1`, `ap-southeast-2`, `ap-south-1` and `ap-northeast-1`.

## Email Options

This provisioner by default will send email to participants/students containing information about their lab environment including IPs and credentials. This configuration requires that each participant register for the workshop using their full name and email address.   Alternatively, you can use generic accounts for workshops.  This method offers the advantage of enabling the facilitator to handle "walk-ins" and is a simpler method overall in terms of collecting participant information.

Steps included in this guide will be tagged with __(email)__ to denote it as a step required if you want to use email and __(no email)__ for steps you should follow if you chose not to use email

**WARNING** Emails are sent _every_ time the playbook is run. To prevent emails from being sent on subsequent runs of the playbook, add `email: no` to `extra_vars.yml`.

## How To Set Up Lab Environments

### One-Time Preparations

To set up lab environments for Ansible training, follow these steps.

1. Create an Amazon AWS account.

1. In AWS, create an ssh key pair called 'ansible': In the AWS management console, click on "Services" on top of the page. In the menu that opens, click on "EC2". In the EC2 dashboard, on the left side, underneath "Network & Security" pick "Key Pairs". Download the private key to your `.ssh` directory, e.g. to `.ssh/ansible.pem`. Alternatively, you can upload your own public key into AWS.

      If using an AWS generated key add it to the ssh-agent:

        ssh-add ~/.ssh/ansible.pem

1. Create an Access Key ID and Secret Access Key. Save the ID and key for later. See [AWSHELP](aws-directions/AWSHELP.md) for a detailed howto.

1. Install `boto` and `boto3`.

        pip install boto boto3

1. Create a `boto` configuration file containing your AWS access key ID and secret access key.

      Use the quickstart directions provided here: [http://boto3.readthedocs.io/en/latest/guide/quickstart.html](http://boto3.readthedocs.io/en/latest/guide/quickstart.html)

1. __(email)__ Create a free [Sendgrid](http://sendgrid.com) account if you don't have one. Optionally, create an API key to use with this the playbook.

1. __(email)__ Install the `sendgrid` python library:

    **Note:** The `sendgrid` module does not work with `sendgrid >= 3`. Please install the latest `2.x` version.

        pip install sendgrid==2.2.1

1. Install the `passlib` library

        pip install passlib

1. Clone the lightbulb repo:

        git clone https://github.com/ansible/lightbulb.git
        cd lightbulb/tools/aws_lab_setup

### Steps To Provision the Lab Environments

1. Update your current installation of the lightbulb repo

1. Define the following variables, either in a file passed in using `-e @extra_vars.yml` or directly in a `vars` section in `aws_lab_setup\infra-aws.yml`:

      ```yaml
      ec2_key_name: username                # SSH key in AWS to put in all the instances
      ec2_region: us-west-1                 # region where the nodes will live
      ec2_az: us-east-1a                    # the availability zone
      ec2_name_prefix: TRAINING-LAB         # name prefix for all the VMs
      admin_password: changeme123           # Set this to something better if you'd like. Defaults to 'LearnAnsible[two digit month][two digit year]', e.g., LearnAnsible0416
      ## Optional Variables
      email: no                             # Set this if you wish to disable email
      sendgrid_user: username               # username for the Sendgrid module.  Not required if "email: no" is set
      sendgrid_pass: 'passwordgoeshere'     # sendgrid accound password.  Not required if "email: no" is set
      sendgrid_api_key: 'APIkey'            # Instead of username and password, you may use an API key. Don't define both. Not required if "email: no" is set
      instructor_email: 'Ansible Instructor <helloworld@acme.com>'  # address you want the emails to arrive from. Not required if "email: no" is set
      ```

1. Create a `users.yml` by copying `sample-users.yml` and adding all your students:

    __(email)__

    ```yaml
    users:
      - name: Bod Barker
        username: bbarker
        email: bbarker@acme.com

      - name: Jane Smith
        username: jsmith
        email: jsmith@acme.com
    ```

    __(no email)__

    ```yaml
    users:
      - name: Student01
        username: student01
        email: instructor@acme.com

      - name: Student02
        username: student02
        email: instructor@acme.com
    ```

    **(no email) NOTE:**  If using generic users, you can generate the corresponding
`users.yml` file from the command line by creating a 'STUDENTS' variable
containing the number of "environments" you want, and then populating the file.
For example:

        STUDENTS=30;
        echo "users:" > users.yml &&
        for NUM in $(seq -f "%02g" 1 $STUDENTS); do
          echo "  - name: Student${NUM}" >> users.yml
          echo "    username: student${NUM}" >> users.yml
          echo "    email: instructor@acme.com" >> users.yml
          echo >> users.yml
        done

1. Run the playbook:

        ansible-playbook provision_lab.yml -e @extra_vars.yml -e @users.yml

1. Check on the EC2 console and you should see instances being created like:

        TRAINING-LAB-<student_username>-node1|2|3|haproxy|tower|control

In your EC2 console you will also see that a VPC was automatically created with a corresponding subnet.

__(email)__ If successful all your students will be emailed the details of their hosts including addresses and credentials, and an `instructor_inventory.txt` file will be created listing all the student machines.

__(no email)__ If you disabled email in your `extra_vars.yml` file, you will need to upload the instructor's inventory to a public URL which you will hand out to participants.

1. Use [github gist](https://gist.github.com/) to upload `lightbulb/tools/aws_lab_setup/instructors_inventory`.
1. Use [http://goo.gl](http://goo.gl) to shorten the URL to make it more consumable

### Teardown The Lab Environments

The `teardown_lab.yml` playbook deletes all the training instances as well as local inventory files.

To destroy all the EC2 instances after training is complete:

1. Run the playbook:

        ansible-playbook teardown_lab.yml -e @extra_vars.yml -e @users.yml

## Accessing student documentation and slides

* A student guide and instructor slides are already hosted at [http://ansible-workshop.redhatgov.io](http://ansible-workshop.redhatgov.io) . (NOTE:  This guide is evolving and newer workshops can be previewed at [http://ansible.redhatgov.io](http://ansible.redhatgov.io) . This new version is currently being integrated with the Lightbulb project)
* Here you will find student instructions broken down into exercises as well as the presentation decks under the __Additional Resources__ drop down.
* During the workshop, it is recommended that you have a second device or printed copy of the student guide.  Previous workshops have demonstrated that unless you've memorized all of it, you'll likely need to refer to the guide, but your laptop will be projecting the slide decks.  Some students will fall behind and you'll need to refer back to other exercises/slides without having to change the projection for the entire class.


