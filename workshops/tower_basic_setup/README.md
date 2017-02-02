# Workshop: Ansible Tower Basic Setup

**THIS WORKSHOP IS CURRENTLY A WORK IN PROGRESS**

### Topics Covered

* Credentials
* Inventory
* Users
* Roles & Permissions
* Projects
* Job Templates
* Running a Job (Playbook)

### What You Will Learn

* Setting up a new instance of Tower with all the parts needed to run an existing Ansible playbook.

### Requirements

* A running instance of Ansible Tower with sufficient permissions to create credentials, inventory sources, projects etc.

### The Assignment

1. Create a machine credential called "Ansible Lab SSH" with the username and password for the hosts in your lab.
2. Create a cloud credential called "Ansible Lab AWS" with the XXXXXX for the hosts in your lab.
3. Create an inventory source called "AWS" and an inventory group named "Lab" that uses EC2 and the "Ansible Lab AWS" cloud credential.
4. Create a project called "Ansible Workshop" with:
    * URL:
    * BLAH:
    * BLAH:
5. In the "Ansible Workshop" project, create a job template called "Deploy Nginx Web Servers" with:
    * PARAM
    * PARAM
6. Run that Job Template and check that it runs without errors and the Nginx web servers are serving the home page.
7. Add an extra variable... test_message to "???" and execute the job template again. After running, load the 

### Extra Credit 

* Create a user... and give them permission to only execute the "Deploy Nginx..." job template... and build a survey to change the test message.
* scheduled refresh? 


### Results

At the end of this exercise, you should have successfully run the Telegraf example playbook.
