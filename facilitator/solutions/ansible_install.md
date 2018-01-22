# Workshop: Installing Ansible

This brief exercise demonstrates how easy it can be to install and configure Ansible and begin automating.

NOTE: If and how you conduct this workshop depends on how you configured the provisioner to run. To save time, you can have lab control machines setup with Ansible. If so, you can skip with workshop.

We use pip because it's OS independent and always has the absolute latest stable release of Ansible. Other package repos such as EPEL can sometime lag behind for days or even weeks. For this reason, Ansible by Red Hat recommends using PIP.

## Solution

Each student will need to SSH into their "control" machine using the host IP, user and password provided to them in their lab environment inventory file.

From that control machine:

```bash
sudo pip install ansible
sudo yum install -y ansible

ansible --verison

ansible --help

mkdir -p ~/.ansible/retry-files
vi ~/.ansible.cfg
# add forks and retry_files_save_path


```

## NOTE

Depending how the lab provisioner was run, students may already have Ansible on their control machines. You can still have them run Ansible with `--version` and `--help` options to check they can ssh into their control box and prove Ansible is indeed present.

Whatever the case, you should make sure each student has the core Ansible software before proceeding.

