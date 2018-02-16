# The Ansible Lightbulb Facilitator's Guide

The Ansible Lightbulb project is an effort to provide a reference and educational content for rapidly communicating and learning Ansible and Ansible Tower essentials. Lightbulb has been designed as a multi-purpose toolkit for effectively demonstrating Ansible's capabilities or providing informal workshop training in various forms -- instructor-led, hands-on or self-paced.

This guide covers different ways Ansible suggests they are assembled for various scenarios.

## Getting Started

If you haven't read it already, start with the [Ansible Lightbulb README](../README.md). There you will find what tools are in the toolkit and the requirements for using this content.

We also recommend reading about [the Lightbulb philosophy](../PHILOSOPHY.md) for effectively communicating and delivering informal training on Ansible in the same spirit that it has become known for and highly successful.

If you are already somewhat familiar with automating with Ansible, we recommend that you are also familiar with the best practices this content incorporates. See [this blog post](https://www.ansible.com/blog/ansible-best-practices-essentials) and [video presentation from AnsibleFest Brooklyn (October 2016)](https://www.ansible.com/ansible-best-practices).

The Lightbulb project provides a lab provisioner tool for creating an environment to present and work with Lightbulb content. Currently the provisioner only supports provisioning lab environments using Amazon Web Services. (A Vagrant option will be developed particularly for self-paced learning.) See the [Ansible AWS Lab Provisioner README](../tools/aws_lab_setup/README.md) for details on requirements, setup and configuration.

## Lightbulb Modules

Lightbulb modules are collections of this content that have been bundled to communicate and/or teach automating with Ansible based on objectives and scenarios. These modules are the "use cases" that all Lightbulb content was specifically developed. The project has endeavored to be as modular and flexible to make other uses possible.

### Live Demonstration

**Scenario**: Quickly demonstrating how Ansible or Ansible Tower works to an audience that has little to no knowledge on the topic.

**Run Time**: ~5-10 minutes to briefly explain and execute one example.

The content in `examples/` can be used to effectively demonstrate Ansible's features to supplement a presentation. These examples have been carefully curated to communicate how Ansible works in a simple and focused way and are easy to demonstrate live and in-action.

For a basic linux server automation demonstration we recommend `examples/apache-basic-playbook`. This example is a single playbook you can put up on a screen with limited scrolling and virtually no file system navigation. For a slightly more sophisticated linux server example, use the Nginx variant in `examples/nginx-basic-playbook`.

### Ansible Essentials Workshop

**Scenario**: Providing instruction on the core essentials to students that have little to no experience automating with Ansible on linux servers.

**Run Time**: 2 Hours

This module is designed to provide some valuable instruction with a limited amount of time and/or resources. It is also ideal for addressing large audiences where the overhead of provisioning and supporting the use of individual labs is not feasible. This module is also ideal for remote instruction like webinars.

#### Presentation Deck

For a basic linux server automation use `decks/ansible-essentials.html` and only navigate to the right. Going down will take you through the more in-depth content and workshops of the Ansible Essentials Hands-on Workshop.

#### Examples & Workshops

##### Examples

* apache-simple-playbook
* apache-basic-playbook
* apache-roles

Besides walking students through these examples, the facilitator of this module will also be asked to install Ansible using pip and demonstrate some ad-hoc commands use. Installing Ansible is optional though highly recommended as it shows how easy it is to get started.

An alternative option for delivering this module to a more sophisticated audience is to use the Nginx variants of the Apache examples instead:

* nginx-simple-playbook
* nginx-basic-playbook
* nginx-roles

##### Workshops

None.

#### Lab Environment

Only the facilitator of the workshop needs a lab environment making this module ideal for scenarios where time and facilities are limited. We recommend the instructor's lab environment be made up of a single "control" host in a group of the same name and 3 CentOS or RHEL linux hosts in a group called "web". The examples used by this module require very few system resources to run. Something akin to a "micro" instance is all that is needed for this particular module. You will need to consider the requirements of other modules if you are going to chain this one with others though.

### Ansible Essentials Hands-On Workshop

**Scenario**: Providing hands-on instruction on the core essentials to students with limited experience automating with Ansible on linux servers.

**Run Time**: 4 Hours

This module is designed to provide students with direct introductory instruction and guidance to beginning to automate with Ansible. It is the starting point for students intent on becoming more proficient with Ansible through other Lightbulb modules and their own usage.

It is ideal for addressing small to medium size audiences of students that are committed to learning how to automate with Ansible.

This module is the 2 hour workshop with a bit of extra depth and hands-on workshops. Delivering this module means providing each student with a lab environment and depending on the size and skill-level of the students in your audience, having one or more assistants to help students during the workshops.

#### Presentation Deck

For a basic linux server automation use `decks/ansible-essentials.html` navigating down when given the option.

#### Examples & Workshops

Unlike the 2 hour non-interactive Ansible Essentials Workshop, this module makes use of both the apache and nginx set of examples. The apache examples are used by the facilitator to demonstrate and walk-thru with the class. The nginx examples are the solutions to the workshops they will be assigned.

##### Examples

* apache-simple-playbook (optional)
* nginx-simple-playbook (optional)
* apache-basic-playbook
* nginx-basic-playbook
* apache-roles
* nginx-roles

##### Workshops

* ansible_install (optional though highly recommended)
* adhoc_commands
* simple_playbook (optional)
* basic_playbook
* roles

When pressed for time or dealing with a more technical audience you can opt to skip the "simple" examples and workshops. The "basic" ones cover the same topics and more.

When applicable, most workshops provide "extra credit" assignments for students that are more advanced or fast-learners.

Facilitators can opt to pre-install Ansible on each control machine for the students allowing you to skip that workshop. We recommend you don't do that though, to show how easy it is to get started using Ansible. It should take 10 minutes or less.

#### Lab Environment

This lab requires each student have their own lab environment in order to perform the workshop assignments. Use the Lightbulb provisioner tool to provision these student labs in advance.

We generally recommend **NOT** using Vagrant with groups. In our experience too much time gets spent helping students install, configure and troubleshoot Vagrant along with their lab environment that could be better spent on Ansible teaching.

Sharing a single lab environment amongst a group of students simply will not work.

We recommend the lab environments be made up of a single "control" host in a group of the same name and 3 CentOS or RHEL linux hosts in a group called "web". The examples used by this module require very few system resources to run. Something akin to a "micro" instance is all that is needed. You will need to consider the requirements of other modules if you are going to chain this one with others though.

### Introduction to Ansible Tower Workshop

**Scenario**: Providing basic instruction to students with limited experience using Ansible Tower on how it works and can be used to facilitate and manage Ansible automation in their organization.

**Run Time**: 1 Hour

**Prerequisites**: Ansible Essentials Workshop or Ansible Essentials Hands-On Workshop

This module is designed to provide some valuable instruction on using Ansible Tower with a limited amount of time and/or resources. It is also ideal for addressing large audiences where the overhead of provisioning and supporting the use of individual labs required to execute hands-on workshops is not feasible. This module is also ideal for remote instruction like webinars.

**NOTE**: The first rule of learning Ansible Tower is to learn Ansible core first. The second rule is to see the first rule. Don't start here.

#### Presentation Deck

For automating with Ansible Tower use DECK FILE HERE and only navigate to the right. Going down will take you through the more in-depth content and workshops of the Introduction to Ansible Tower Hands-On Workshop.

#### Examples & Workshops

##### Examples

The example(s) here are mostly at the facilitator's discretion. We recommend the apache-roles or nginx-roles example since those are the most sophisticated one students are exposed to in the Essentials workshops that should have preceded this module.

##### Workshops

None.

#### Lab Environment

Only the facilitator of the workshop needs a lab environment making this module ideal for scenarios where time and facilities are limited. We recommend the instructor's lab environment be made up of a single "control" host in a group of the same name and 3 CentOS or RHEL linux hosts in a group called "web". While the web hosts need only minimal resources, the control instance will take additional memory and storage requirements required by Ansible Tower system on it.

### Introduction to Ansible Tower Hands-On Workshop

**Scenario**: Providing hands-on instruction to students with limited experience with Ansible Tower on how it works and how it can be used to facilitate and manage Ansible automation in their organization.

**Run Time**: 2 Hours

**Prerequisites**: Ansible Essentials Workshop or Ansible Essentials Hands-On Workshop

This module is designed to provide some valuable instruction on using Ansible Tower with a limited amount of time and/or resources. It is also ideal for addressing large audiences where the overhead of provisioning and supporting the use of individual labs required to execute hands-on workshops is not feasible. This module is also ideal for remote instruction like webinars.

**NOTE**: The first rule of learning Ansible Tower is to learn Ansible core first. The second rule is to see the first rule. Don't start here.

#### Presentation Deck

For automating with Ansible Tower use DECK FILE HERE and only navigate to the right. Going down will take you thru the more in-depth content and workshops of the Introduction to Ansible Tower Hands-On Workshop.

#### Examples & Workshops

##### Examples

The example(s) here are mostly at the facilitator's discretion. We recommend the apache-roles or nginx-roles example since those are the most sophisticated one students are exposed to in the Essentials workshops that should have preceded this module.

##### Workshops

* tower_install (optional though highly recommended)
* tower_basic_setup

When applicable, most workshops provide "extra credit" assignments for students that are more advanced or fast-learners.

Facilitators can opt to pre-install Ansible Tower on each control machine for the students allowing you to skip that workshop.

#### Lab Environment

This lab requires each student to have their own lab environment in order to perform the workshop assignments. Use the Lightbulb provisioner tool to provision these student labs in advance.

We generally recommend **NOT** using Vagrant with groups. In our experience too much time gets spent helping students install, configure and troubleshoot Vagrant along with their lab environment that could be better spent on Ansible teaching.

Sharing a single lab environment amongst a group of students simply will not work.

We recommend the lab environments be made up of a single "control" host in a group of the same name and 3 CentOS or RHEL linux hosts in a group called "web". While the web hosts need only minimal resources, the control instance will take additional memory and storage requirements required by Ansible Tower system on it.

### Introduction to Ansible and Ansible Tower Workshop

**Scenario**: Providing an in-depth overview to an audience with limited Ansible and Ansible Tower experience on how they can be used to facilitate and manage Ansible automation in their organization.

**Run Time**: 3 Hours

This module is designed to provide basic instruction on using Ansible and Ansible Tower with a limited amount of time and/or resources.

This module is the combination of two modules:

* Ansible Essentials
* Introduction to Ansible Tower

Refer to the docs on those modules and run concurrently.

### Introduction to Ansible and Ansible Tower Hands-On Workshop

**Scenario**: Providing hands-on instruction on the core essentials and Ansible Tower to students with limited experience automating with Ansible on linux servers.

**Run Time**: 6 Hours

This module is designed to provide hands-on interactive instruction on using Ansible and Ansible Tower.

This module is the combination of two modules:

* Ansible Essentials Hands-On
* Introduction to Ansible Tower Hands-On

Refer to the docs on those modules and run concurrently.
