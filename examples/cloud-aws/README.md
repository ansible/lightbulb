# cloud-aws

This intermediate-level Ansible playbook example demonstrates the common tasks for provisioning EC2 server instances into an Amazon Web Services VPC. Once provisioned this example will use an existing role (apache-role) to deploy and setup an application service on the instances in the stack.

This example demonstrates a few other best practices and intermediate techniques:

* **Compound Playbook.** This example shows the use of a playbook, `site.yml`, combining other playbooks, `provision.yml` and `setup.yml`, using play level 'include' statements. Splitting provisioning and configuration plays into separate files is a recommended best practice. By doing so, users have more flexibility to what the run without needing tags and wrapping blocks of tasks with conditionals. This separation can be used to promote reuse, but enabling the mixing and matching of various playbooks.
* **Controlling Debug Message Display.** There is a debug task in `provison.yml` using the optional `verbosity` parameter. Avoiding the unnecessary display of debugging messages avoids confusion and is just good hygiene. In this implementation, the debug message won't be displayed unless the playbook is run in verbose mode level 1 or greater.

## Requirements

To use this example you will need to have an AWS account setup and properly configured on your control machine. You will also need the boto, boto3 and botocore modules installed. See the [Ansible AWS Guide](http://docs.ansible.com/ansible/guide_aws.html) for more details.

## Variables

Before running this playbook example, you should know about what variables it uses and how they effect the execution of the AWS provisioning process.

### Required

The following variables must be properly set for this example to run properly.

* `ec2_stack_name`: A unique name for your application stack. The stack name is used as a prefix for many other resources that will get created using this playbook.

* `ec2_region`: A valid AWS region name such as "us-east-2" or "ap-southeast-1" or "eu-west-2."

* `ec2_key_name`: An existing AWS keyname from your account to use when provisioning instances.

### Optional

There are a few other variables present whose value you can override if needed.

* `ec2_az`: The EC2 availability zone to use in the region. Default: a

* `ec2_vpcidr`: The VPC CIDR value. Default: 10.251.0.0/16

* `ec2_subnetcidr`: The VPC Subnet CIDR value. Default: 10.251.1.0/24

* `ec2_exact_count`: The number of EC2 instances that should be present. Using the `ec2` module, this playbook will create and terminate instances as needed. Default: 1

* `ec2_private_key_file`: The path to the private key associated with the `ec2_key_name` used to launch the instances if you need it. If undefined, it is omitted from dynamic inventory group "web".

## Usage

To execute this example, use the `site.yml` playbook and pass in all the required variables:

```
ansible-playbook site.yml -e "ec2_stack_name=lightbulb ec2_region=us-east-2 ec2_key_name=engima"
```

Using verbose mode of any type will emit a debugging message that displays information about the provisioned instances in the stack.

```
ansible-playbook site.yml -e "ec2_stack_name=lightbulb ec2_region=us-east-2 ec2_key_name=engima" -v
```

Remember you can put your variables in a YAML formatted file and feed it into the play with the @ operator.

```
ansible-playbook site.yml -e @extra_vars.yml
```

### One More Thing

Since we are reusing the apache-simple roles from `examples/apache-role`, we can override the default value of `apache_test_message` to change the message that gets inserted onto the generated home page by the role.

```
ansible-playbook site.yml -e "ec2_stack_name=lightbulb ec2_region=us-east-2 ec2_key_name=engima apache_test_message=Hello_World"
```
