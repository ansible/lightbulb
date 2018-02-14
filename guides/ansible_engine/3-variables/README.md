# Exercise 3 - Using Variables, Loops, and Handlers

Previous exercises showed you the basics of Ansible Engine.  In the next few exercises, we are going to teach some more advanced ansible skills that will add flexibility and power to your playbooks.

Ansible exists to make tasks simple and repeatable.  We also know that not all systems are exactly alike and often require some slight change to the way an Ansible playbook is run.  Enter variables.

Variables are how we deal with differences between your systems, allowing you to account for a change in port, IP address or directory.

Loops enable us to repeat the same task over and over again.  For example, lets say you want to install 10 packages. By using an ansible loop, you can do that in a single task.

Handlers are the way in which we restart services.  Did you just deploy a new config file, install a new package? If so, you may need to restart a service for those changes to take effect.  We do that with a handler.

For a full understanding of variables, loops, and handlers; check out our Ansible documentation on these subjects.

* [Ansible Variables](http://docs.ansible.com/ansible/latest/playbooks_variables.html)
* [Ansible Loops](http://docs.ansible.com/ansible/latest/playbooks_loops.html)
* [Ansible Handlers](http://docs.ansible.com/ansible/latest/playbooks_intro.html#handlers-running-operations-on-change)

## Section 1: Running the Playbook

To begin, we are going to create a new playbook, but it should look very familiar to the one you created in exercise [1.2](../2-playbook/README.md)

We are now going to run you're brand new playbook on your two web nodes.  To do this, you are going to use the `ansible-playbook` command.

### Step 1

Navigate to your home directory create a new project and playbook.

```bash
cd
mkdir apache-basic-playbook
cd apache-basic-playbook
vim site.yml
```

### Step 2

Add a play definition and some variables to your playbook.  These include addtional packages your playbook will install on your web servers, plus some web server specific configurations.

```yml
---
- name: Ensure apache is installed and started
  hosts: web
  become: yes
  vars:
    httpd_packages:
      - httpd
      - mod_wsgi
    apache_test_message: This is a test message
    apache_max_keep_alive_requests: 115
```

### Step 3

Add a new task called *httpd packages are present*:

```yml
{% raw %}
  tasks:
    - name: Ensure httpd packages are present
      yum:
        name: "{{ item }}"
        state: present
      with_items: "{{ httpd_packages }}"
      notify: restart-apache-service
{% endraw %}
```

---
**NOTE**
> Let's see what is happening here.

* `vars:` You've told Ansible the next thing it sees will be a variable name
* `httpd_packages` You are defining a list-type variable called `httpd_packages**.  What follows is a list of those packages
* {% raw %}`{{ item }}`{% endraw %} You are telling Ansible that this will expand into a list item like `httpd` and `mod_wsgi`.
* {% raw %}`with_items: "{{ httpd_packages }}`{% endraw %} This is your loop which is instructing Ansible to perform this task on every `item` in `httpd_packages`
* `notify: restart-apache-service` This statement is a `handler`, so we'll come back to it in Section 3.

---

## Section 2: Deploying Files and Starting a Service

When you need to do something with files or directories on a system, use one of the [Ansible Files](http://docs.ansible.com/ansible/latest/list_of_files_modules.html) modules.  In this case, we'll leverage the `file` and `template` modules.

### Step 1

Create a `templates` directory in your project directory and download two files.

```bash
mkdir templates
cd templates
curl -O https://raw.githubusercontent.com/ansible/lightbulb/master/examples/apache-basic-playbook/templates/httpd.conf.j2
curl -O https://raw.githubusercontent.com/ansible/lightbulb/master/examples/apache-basic-playbook/templates/index.html.j2
```

### Step 2

Add some file tasks and a service task to your playbook.

```yml
- name: Ensure site-enabled directory is present
  file:
    name: /etc/httpd/conf/sites-enabled
    state: directory

- name: Ensure latest httpd.conf is present
  template:
    src: templates/httpd.conf.j2
    dest: /etc/httpd/conf/httpd.conf
  notify: restart-apache-service

- name: Ensure latest index.html is present
  template:
    src: templates/index.html.j2
    dest: /var/www/html/index.html

- name: Ensure httpd is started and enabled
  service:
    name: httpd
    state: started
    enabled: yes
```

---
**NOTE:** Recap of used modules

> What did we just write?

* `file:` This module is used to create, modify, delete files, directories, and symlinks.
* `template:` This module specifies that a [jinja2](http://docs.ansible.com/ansible/latest/playbooks_templating.html) template is being used and deployed. `template` is part of the `Files`
  module family and we encourage you to check out all of the other [file-management modules here](http://docs.ansible.com/ansible/latest/list_of_files_modules.html).
* `service` - The Service module starts/stops/restarts services.

---

## Section 3: Defining and Using Handlers

There are any number of reasons we often need to restart a service/process including the deployment of a configuration file, installing a new package, etc.  There are really two parts to this Section; adding a handler to the playbook and calling the handler after the a task.  We will start with the former.

### Step 1

Define a handler.

```yml
handlers:
  - name: restart-apache-service
    service:
      name: httpd
      state: restarted
```

---
**NOTE:** Handlers

> A handler is only executed when it is triggered by a task.

* `handler:` This is telling the *play* that the `tasks:` are over, and now we are defining `handlers:`. Everything below that looks the same as any other task, i.e. you give it a name, a module, and the options for that module.  This is the definition of a handler.
* `notify: restart-apache-service` This triggers the handler as mentioned above. The `nofify` statement is the invocation of a handler by name. In the above created playbook, a `notify` statement was already added to the `latest httpd.conf is present` task.

---

## Section 4: Review

Your new, improved playbook is done! Let's take a second look to make sure everything looks the way you intended.  If not, now is the time for us to fix it up. The figure below shows line counts and spacing.

```yml
{% raw %}
---
- name: Ensure apache is installed and started
  hosts: web
  become: yes
  vars:
    httpd_packages:
      - httpd
      - mod_wsgi
    apache_test_message: This is a test message
    apache_max_keep_alive_requests: 115

  tasks:
    - name: Ensure httpd packages are present
      yum:
        name: "{{ item }}"
        state: present
      with_items: "{{ httpd_packages }}"
      notify: restart-apache-service

    - name: Ensure site-enabled directory is present
      file:
        name: /etc/httpd/conf/sites-enabled
        state: directory

    - name: Ensure latest httpd.conf is present
      template:
        src: templates/httpd.conf.j2
        dest: /etc/httpd/conf/httpd.conf
      notify: restart-apache-service

    - name: Ensure latest index.html is present
      template:
        src: templates/index.html.j2
        dest: /var/www/html/index.html

    - name: Ensure httpd is started and enabled
      service:
        name: httpd
        state: started
        enabled: yes

  handlers:
    - name: restart-apache-service
      service:
        name: httpd
        state: restarted
{% endraw %}
```

## Section 5: Running your new apache playbook

Congratulations!  You just wrote a playbook that incorporates some key Ansible concepts that you use in most if not all of your future playbooks.  Before you get too excited though, we should probably make sure it actually runs.

So, lets do that now.

### Step 1

Make sure you are in the right directory and create a host file.

```bash
cd ~/apache-basic-playbook
```

### Step 2

Run your playbook

```bash
ansible-playbook -i ./inventory.ini site.yml
```

## Section 2: Review

If successful, you should see standard output that looks very similar to the following.  If not, just let us know.  We'll help get things fixed up.

![Stdout](stdout_2.png)

---

[Click Here to return to the Ansible Lightbulb - Ansible Engine Workshop](../README.md)
