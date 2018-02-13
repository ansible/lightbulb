# Exercise 2 - Writing Your First playbook

Now that you've gotten a sense of how ansible works, we are going to write our first ansible *playbook*. Playbooks are Ansible’s configuration, deployment, and orchestration language. They are written in YAML and are used to invoke Ansible modules to perform tasks that are executed sequentially i.e top to bottom. They can describe a policy you want your remote systems to enforce, or a set of steps in a general IT workflow. Playbooks are like an instruction manual and describe the state of environment.

A playbook can have multiple plays and a play can have one or multiple tasks.  The goal of a *play* is to map a group of hosts.  The goal of a *task* is to implement modules against those hosts.

For our first playbook, we are only going to write one play and two tasks.

## Section 1: Creating a Directory Structure and Files for your Playbook

There is a [best practices](http://docs.ansible.com/ansible/playbooks_best_practices.html) on the preferred directory structures for playbooks.  We strongly encourage you to read and understand these practices as you develop your Ansible skills.

Instead, we are going to create a very simple directory structure for our playbook, and add just a couple of files to it.

### Step 1: Create a directory called `apache_basic` in your home directory and change directories into it

```bash
mkdir ~/apache-simple-playbook
cd ~/apache-simple-playbook
```

### Step 2: Use `vi` or `vim` to open a file called `site.yml`

## Section 2: Defining Your Play

Now that you are editing `site.yml`, let's begin by defining the play and then understanding what each line accomplishes

```yml
---
- name: Ensure apache is installed and started
  hosts: web
  become: yes
```

* `---` Defines the beginning of YAML
* `hosts: web` Defines the host group in your inventory on which this play will run against
* `name: install and start apache` This describes our play
* `become: yes` Enables user privilege escalation.  The default is sudo, but su, pbrun, and [several others](http://docs.ansible.com/ansible/become.html) are also supported.

## Section 3: Adding Tasks to Your Play

Now that we've defined your play, let's add some tasks to get some things done.  Align (vertically) the *t* in `task` with the *b* `become`. Yes, it does actually matter.  In fact, you should make sure all of your playbook statements are aligned in the way shown here. If you want to see the entire playbook for reference, skip to the bottom of this exercise.

```yml
  tasks:
  - name: Ensure httpd package is present
    yum:
      name: httpd
      state: present

  - name: Ensure latest httpd.conf file is present
    copy:
      src: files/index.html
      dest: /var/www/html/

  - name: Ensure httpd is started
    service:
      name: httpd
      state: started
```

* `tasks:` This denotes that one or more tasks are about to be defined
* `- name:` Each task requires a name which will print to standard output when you run your playbook. It's considered best practice to give all your plays and tasks concise and human-meaningful descriptions.

```yml
- name: Ensure httpd package is present
  yum:
    name: httpd
    state: present
```

* These four lines are calling the Ansible module *yum* to install httpd. [Click here](http://docs.ansible.com/ansible/yum_module.html) to see all options for the yum module.

```yml
- name: Ensure latest httpd.conf file is present
  copy:
    src: files/index.html
    dest: /var/www/html/
```

* These four lines ensure that the `httpd.conf` file is copied over to the target node. [Click here](http://docs.ansible.com/ansible/copy_module.html) to see all options for the copy module.

```yml
- name: Ensure httpd is started
  service:
    name: httpd
    state: started
```

* The next few lines are using the ansible module `service` to start the httpd service right now. The service module is the preferred way of controlling services on remote hosts. [Click here](http://docs.ansible.com/ansible/service_module.html) to learn more about the `service` module.

## Section 4: Saving your Playbook

Now that you've completed writing your playbook, it would be a shame not to keep it.

Use the `write/quit` method in `vi` or `vim` to save your playbook, i.e. `Esc :wq!`

Also, you have to create the above mentioned `index.html` file. For this, first create the proper directory:

```bash
mkdir ~/apache-simple-playbook/files
cd ~/apache-simple-playbook/files
```

Next, create the file and add content: Use `vi` or `vim` to open a file called `index.html` and add the following content:

```html
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Ansible: Automation for Everyone</title>
  <link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
  <style>
body {
    font-family: 'Open Sans', sans-serif;
    text-align: center;
}
.container {
    position: absolute;
    top: 50%;
    left: 50%;
    -moz-transform: translateX(-50%) translateY(-50%);
    -webkit-transform: translateX(-50%) translateY(-50%);
    transform: translateX(-50%) translateY(-50%);
    font-size: 200%;
}
footer {
    width: 100%;
    bottom: 0;
    position: fixed;
    font-size: 75%;
}
img {
    margin: 0 auto;
}
  </style>
</head>
<body>
<div class="container">
    <img src="https://www.ansible.com/hubfs/2017_Images/BrandPage/Brand-Assets/Ansible_RH_AnsibleAutomation_RGB_RedBlack.png" width="75%"/>
</div>
<footer>Red Hat Ansible</footer>
</body>
</html>
```

Use the `write/quit` method in `vi` or `vim` to save your playbook, i.e. `Esc :wq!`

And that should do it.  You should now have a fully written playbook called `site.yml`. You are ready to automate!

---
**NOTE**
Ansible playbooks are essential YAML and YAML is a bit particular about formatting especially regards to whitespace. If you are unfamiliar with this, we recommend reading up on [YAML Syntax](http://docs.ansible.com/ansible/YAMLSyntax.html) in the Ansible docs.

In the meantime, your completed playbook should look like this example below. (Take note of the spacing and alignment.)

---

```yml
---
- name: Ensure apache is installed and started
  hosts: web
  become: yes

  tasks:
  - name: Ensure httpd package is present
    yum:
      name: httpd
      state: present

  - name: Ensure latest httpd.conf file is present
    copy:
      src: files/index.html
      dest: /var/www/html/

  - name: Ensure httpd is started
    service:
      name: httpd
      state: started
```

---

[Click Here to return to the Ansible Lightbulb - Ansible Engine Workshop](../README.md)
