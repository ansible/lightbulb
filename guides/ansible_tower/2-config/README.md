# Exercise 2 - Configuring Ansible Tower

In this exercise, we are going to configure Tower so that we can run a playbook.

## The Tower UI

There are a number of concepts in the Ansible Tower UI that enable multi-tenancy, notifications, scheduling, etc. However, we are only going to focus on a few of the key contructs that are required for this workshop today.

* Credentials
* Projects
* Inventory
* Job Template

## Logging into Tower and Installing the License Key

### Step 1

To log in, use the username `admin` and and the password `ansibleWS`.

![Ansible Tower Login Screen](ansible-lab-figure01-logon-screen.png)

As soon as you login, you will prompted to request a license or browse for an existing license file

![Uploading a License](at_lic_prompt.png)

### Step 2

In a seperate browser tab, browse to [https://www.ansible.com/workshop-license](https://www.ansible.com/workshop-license) to request a workshop license. These are special workshop licenses which are valid for only 5 nodes for 5 days.

### Step 3

Back in the Tower UI, choose BROWSE ![Browse button](at_browse.png) and upload the license file you received via e-mail.

### Step 4

Select "_I agree to the End User License Agreement_"

### Step 5

Click on SUBMIT ![Submit button](at_submit.png)

## Creating a Credential

Credentials are utilized by Tower for authentication when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system.

There are many [types of credentials](http://docs.ansible.com/ansible-tower/latest/html/userguide/credentials.html#credential-types) including machine, network, and various cloud providers.  In this workshop, we are using a *machine* credential.

### Step 1

Select the gear icon ![Gear button](at_gear.png)

### Step 2

Select CREDENTIALS

### Step 3

Click on ADD ![Add button](at_add.png)

### Step 4

Complete the form using the following entries.

|OPTION|VALUE
|------|-----
|NAME |Ansible Workshop Credential
|DESCRIPTION|Machine credential for run job templates during workshop
|ORGANIZATION|Default
|TYPE|Machine
|USERNAME|Your workshop username - Student(x)
|PASSWORD|Your workshop password
|PRIVILEGE ESCALATION|Sudo

![Adding a Credential](at_cred_detail.png)

### Step 5

Select SAVE ![Save button](at_save.png)

## Creating a Project

A Project is a logical collection of Ansible playbooks, represented in Tower. You can manage playbooks and playbook directories by either placing them manually under the Project Base Path on your Tower server, or by placing your playbooks into a source code management (SCM) system supported by Tower, including Git, Subversion, and Mercurial.

### Step 1

Click on PROJECTS

### Step 2

Select ADD ![Add button](at_add.png)

### Step 3

Complete the form using the following entries

|OPTION|VALUE
|------|-----
|NAME |Ansible Workshop Project
|DESCRIPTION|Workshop playbooks
|ORGANIZATION|Default
|SCM TYPE|Git
|SCM URL| [https://github.com/ansible/lightbulb](https://github.com/ansible/lightbulb)
|SCM BRANCH|
|SCM UPDATE OPTIONS|Mark _Clean_ and _Update on Launch_

![Defining a Project](at_project_detail.png)

### Step 4

Select SAVE ![Save button](at_save.png)

## Creating a Inventory

An inventory is a collection of hosts against which jobs may be launched. Inventories are divided into groups and these groups contain the actual hosts. Groups may be sourced manually, by entering host names into Tower, or from one of Ansible Tower’s supported cloud providers.

An Inventory can also be imported into Tower using the `tower-manage` command and this is how we are going to add an inventory for this workshop.

### Step 1

Click on INVENTORIES

### Step 2

Select ADD ![Add button](at_add,png)

### Step 3

Complete the form using the following entries

|OPTION|VALUE
|------|-----
|NAME |Ansible Workshop Inventory
|DESCRIPTION|Ansible Inventory
|ORGANIZATION|Default

![Create an Inventory](at_inv_create.png)

### Step 4

Select SAVE ![Save button](at_save.png)

### Step 5

Using ssh, login to your control node

```bash
ssh <username>@<IP_Address_of_your_control_node>
```

### Step 6

Use the `tower-manage` command to import an existing inventory.  (_Be sure to replace <username> with your actual username_)

```
sudo tower-manage inventory_import --source=/home/<username>/lightbulb/lessons/lab_inventory/<username>-instances.txt --inventory-name="Ansible Workshop Inventory"
```

You should see output similar to the following:

![Importing an inventory with tower-manage](at_tm_stdout.png)

Feel free to browse your inventory in Tower.  You should now notice that the inventory has been populated with Groups and that each of those groups contain hosts.

![Inventory with Groups](at_inv_group.png)

### End Result

At this point, we are doing with our basic configuration of Ansible Tower.  In exercise 2.2, we will be soley focused on creating and running a job template so you can see Tower in action.

---

[Click Here to return to the Ansible Lightbulb - Ansible Tower Workshop](../README.md)
