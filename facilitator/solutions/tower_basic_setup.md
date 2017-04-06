# Workshop: Ansible Tower Basic Setup

**THIS WORKSHOP SOLUTION IS CURRENTLY A WORK IN PROGRESS**

Here students are tasked with installing and activating a new single integrated instance of Ansible Tower. The assignment will show students how they can setup an instance of Ansible Tower themselves to run an existing playbook for testing, demos and their own proof-of-concepts. 

#### Tips

This workshop can be presented in a classroom setting as a guided exercises to save a bit of time. The faciltator has the students follow along as they step thru each part of the correspending demo.

Stepping thru the solution provides an excellent opportunity to briefly mention other features in Tower such as schedule jobs not explored in this workshop assignment.

### Solution

The focus of this exercise is to familiarize students with how to use the Ansible Tower UI. The following screenshots approximate the steps required to complete the workshop.

#### 1
![creating inventory](../images/creating_inventory.png)

#### 1.a
![creating hosts](../images/creating_host.png)

#### 1.b
![final inventory](../images/finalized_inv.ong)

#### 2 
![creating machine credential](../images/LBcreatingcred.png)

#### 3
![cteaing a project](../images/project_creation.png)

#### 4 
![creating job template](../images/job_template.png)

#### 5
![launch job template](../images/running_job.png)

#### 5.a
![succesful job completion](../images/succes_job.png)

#### 6
![adding extra vars](../images/extra_variables.png)




NOTE: These screenshots where taken using Ansible Tower 3.1.1.

* Settings Icon and Credentials Card
* Create Machine Credential
* Create Group
* Create Hosts (under Group)
* Create Project
* Create Template
* Extra Variables 

#### Extras Credit

* Create Users
* Assign Execution Permission to User in Job Templates
* User Surveys
