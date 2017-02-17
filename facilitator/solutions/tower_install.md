# Workshop: Installing Tower

Here students are tasked with installing and activating a new standalone instance of Ansible Tower. The assignment will show students how they can run an instance of Tower themselves for testing, demos and their own proof-of-concepts. 

#### Tips

If you are working in an environment that does not have access repos such as EPEL, you can opt to use the [Ansible Tower bundle installer](http://releases.ansible.com/ansible-tower/setup-bundle/ansible-tower-setup-bundle-latest.el7.tar.gz) instead. This bundle includes all of the RPMs from these repositories. It does not include **all** of the RPMs required.

Once downloaded, configured and the `setup.sh` is started, is will take a few minutes to install all of the Ansible Tower dependencies. Students can take a short break while that runs.

### Solution

1. Retreive the latest version of Tower from the Ansible Tower releases archive.
2. Unarchive the retreived Ansible Tower archive.
3. Change directories to the one created by the expanded Tower software archive.
4. Edit the `inventory` file with passwords for admin, message queue and the postgres database will use while setting up. These are represented by these inventory variables:
    * `admin_password` 
    * `mq_password`
    * `pg_password`
5. Run the `sudo setup.sh` script.
6. Verify Ansible has been successfully installed and started, load the Ansible Tower UI in a web browser using the control machine IP address. 
7. Sign in as the admin user with the password created in the installation process. You will be prompted for a license.
8. Request a trial license if one hasn't been provided already. (Either trial license type will suffice.)
9. Import the license file.
10. Extra Credit: Open the ping API end point in a web browser -- the URL will be something like like https://tower.host.ip/v1/api/ping.

These are the approximate BASH commands to do this:

```bash
$ wget http://releases.ansible.com/ansible-tower/setup/ansible-tower-setup-latest.tar.gz
$ tar -xzvf ansible-tower-setup-latest.tar.gz
$ cd ansible-tower-setup-x.x.x
$ vi inventory
# make edits to inventory variables
$ ./setup.sh
# Using your browser sign into the Ansible Tower UI 
# as admin and setup the instance with a license file.
```
