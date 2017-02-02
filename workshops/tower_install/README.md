# Workshop: Installing Tower

### Topics Covered

* Installing Ansible Tower
* Importing a License File

### What You Will Learn

* The installation process for a standlone instance of Ansible Tower using the bundled installer.

### The Assignment

Install Ansible Tower on your controller machine using the [latest bundled installer](http://releases.ansible.com/ansible-tower/setup-bundle/ansible-tower-setup-bundle-latest.el7.tar.gz) and upload your license file. 

1. Follow the [quick installation instructions](http://docs.ansible.com/ansible-tower/latest/html/quickinstall/index.html) to configure and run the installation.
2. Load the Ansible Tower UI in a web browser using the controller machine IP address. 
3. Sign in as the admin user with the password created in the installation process. You will be prompted for a license.
4. Request a trial license if one hasn't been provided already. (Either trial license type will suffice.)
5. Import the license file.

### Extra Credit

* After importing the license file, access the ping API endpoint using a browser.

### Reference

* [Ansible Tower Quick Installation Guide](http://docs.ansible.com/ansible-tower/latest/html/quickinstall/index.html)
* [Import a License](http://docs.ansible.com/ansible-tower/latest/html/userguide/import_license.html)
* [Ansible Tower Ping API Endpoint](http://docs.ansible.com/ansible-tower/3.0.3/html/towerapi/ping.html)