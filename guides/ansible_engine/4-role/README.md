# Exercise 1.4 - Roles: Making your playbooks reusable

While it is possible to write a Playbook in one very large file, eventually you’ll want to reuse files and start to organize things. At a basic level, including task files allows you to break up bits of configuration policy into smaller files. Task includes pull in tasks from other files. Since handlers are tasks too, you can also include handler files.

When you start to think about it – tasks, handlers, variables, and so on – begin to form larger concepts. You start to think about modeling what something is,

* It’s no longer "apply THIS to these hosts"
* You say "these hosts are are webservers".

Roles build on the idea of include files and provide Ansible with a way to load tasks, handlers, and variables from external files. The files that define a role have specific names and are organized in a rigid directory structure.

Use of Ansible roles has the following benefits:

* Roles group content, allowing easy sharing of code with others
* Roles can be written that define the essential elements of a system type: web server, database server...
* Roles make larger projects more manageable
* Roles can be developed in parallel by different administrators

For this exercise, you are going to take the playbook you just wrote and refactor it into a role. In addition, you'll learn to use `ansible-galaxy` to jumpstart development of a role.

Let's begin with seeing how the new playbook structure `apache-role`, which we are going to create in this exercise,  will break down into a role.

```bash
apache-role/
├── roles
│   └── apache-simple
│       ├── defaults
│       │   └── main.yml
│       ├── files
│       ├── handlers
│       │   └── main.yml
│       ├── meta
│       │   └── main.yml
│       ├── README.md
│       ├── tasks
│       │   └── main.yml
│       ├── templates
│       ├── tests
│       │   ├── inventory
│       │   └── test.yml
│       └── vars
│           └── main.yml
├── inventory.ini
└── site.yml
```

Fortunately, you don't have to create all of these directories and files by hand.  That's where `ansible-galaxy` comes in.

## Section 1: Using ansible-galaxy to initialize a new role

Ansible Galaxy is a free site for finding, downloading, and sharing roles. Ansible includes the tool `ansible-galaxy` which can interact with the site and the roles hosted there.  It's also pretty handy for creating them locally which is what we are about to do here.

### Step 1

Create a new directory, `apache-role`.

```bash
cd
mkdir apache-role
cd ~/apache-role
```

### Step 2

Create a directory called `roles` and `cd` into it.

```bash
mkdir roles
cd roles
```

### Step 3

Use the `ansible-galaxy` command to initialize a new role called `apache-simple`.

```bash
ansible-galaxy init apache-simple
```

Take a look around the structure you just created.  It should look a lot like Figure 1 above.  However, we need to complete one more step before moving onto section 2.  It is Ansible best practice to clean out role directories and files you won't be using.  For this role, we won't be using anything from `files`, `tests`.

### Step 4

Remove the `files` and `tests` directories

```bash
cd ~/apache-role/roles/apache-simple/
rm -rf files tests
```

## Section 2: Breaking Your `site.yml` Playbook into the Newly Created `apache-simple` Role

In this section, we will separate out the major parts of your playbook including `vars:`, `tasks:`, `template:`, and `handlers:`.

### Step 1

Copy the `inventory.ini` file:

```bash
cd ~/apache-role
cp ~/apache-basic-playbook/inventory.ini inventory.ini
```

Make a copy of `site.yml` which was written in the last exercise to the current directory.

```bash
cd ~/apache-role
cp ~/apache-basic-playbook/site.yml site.yml
vim site.yml
```

### Step 2

Add the play definition and the invocation of a single role.

```yml
---
- name: Ensure apache is installed and started via role
  hosts: web
  become: yes

  roles:
    - apache-simple
```

### Step 3

Add some default variables to your role in `roles/apache-simple/defaults/main.yml`.

```yml
---
# defaults file for apache-simple
apache_test_message: This is a test message
apache_max_keep_alive_requests: 115
```

### Step 4

Add some role-specific variables to your role in `roles/apache-simple/vars/main.yml`.

```yml
---
# vars file for apache-simple
httpd_packages:
  - httpd
  - mod_wsgi
```

---
**NOTE**
####
As can be seen above, we added variables at another place than the previously directly in the playbook. Variables can be defined in a variety of places and have a clear [precedence](http://docs.ansible.com/ansible/latest/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable). Here are some examples where variables can be placed:

* vars directory
* defaults directory
* group_vars directory
* In the playbook under the `vars:` section
* In any file which can be specified on the command line using the `--extra_vars` option

In this exercise, we are using role defaults to define a couple of variables and these are the most malleable.  After that, we defined some variables in `/vars` which have a higher precedence than defaults and can't be overridden as a default variable.

---

### Step 5

Create your role handler in `roles/apache-simple/handlers/main.yml`.

```yml
---
# handlers file for apache-simple
- name: Ensure apache service is restarted
  service:
    name: httpd
    state: restarted
    enabled: yes
```

### Step 6

Add tasks to your role in `roles/apache-simple/tasks/main.yml`.

```yml
{% raw %}
---
# tasks file for apache-simple
- name: Ensure httpd packages are installed
  yum:
    name: "{{ item }}"
    state: present
  with_items: "{{ httpd_packages }}"
  notify: restart-apache-service

- name: Ensure site-enabled directory is created
  file:
    name: /etc/httpd/conf/sites-enabled
    state: directory

- name: Copy httpd.conf
  template:
    src: templates/httpd.conf.j2
    dest: /etc/httpd/conf/httpd.conf
  notify: restart-apache-service

- name: Copy index.html
  template:
    src: templates/index.html.j2
    dest: /var/www/html/index.html

- name: Ensure httpd is started
  service:
    name: httpd
    state: started
    enabled: yes
{% endraw %}
```

### Step 7

Download a couple of templates into `roles/apache-simple/templates/`.  And right after that, let's clean up from exercise 2.1 by removing the old templates directory.

```bash
mkdir -p ~/apache-role/roles/apache-simple/templates/
cd ~/apache-role/roles/apache-simple/templates/
curl -O https://raw.githubusercontent.com/ansible/lightbulb/master/examples/apache-role/roles/apache-simple/templates/httpd.conf.j2
curl -O https://raw.githubusercontent.com/ansible/lightbulb/master/examples/apache-role/roles/apache-simple/templates/index.html.j2
```

## Section 3: Running your new role-based playbook

Now that you've successfully separated your original playbook into a role, let's run it and see how it works.

### Step 1

Run the playbook.

```bash
ansible-playbook -i ./inventory.ini site.yml
```

If successful, your standard output should look similar to the figure below.

![Role based stdout](stdout_3.png)

## Section 4: Review

You should now have a completed playbook, `site.yml` with a single role called `apache-simple`.  The advantage of structuring your playbook into roles is that you can now add new roles to the playbook using Ansible Galaxy or simply writing your own.  In addition, roles simplify changes to variables, tasks, templates, etc.

---

[Click Here to return to the Ansible Lightbulb - Ansible Engine Workshop](../README.md)
