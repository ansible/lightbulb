# Workshop: Tower - Install 

yum install wget 
wget http://releases.ansible.com/ansible-tower/setup/ansible-tower-setup-latest.tar.gz 
tar xvzf ansible-tower-setup-latest.tar.gz
cd ansible-tower-setup-<tower-version>/
vi inventory
<add a password for admin_password, redis_password, pg_password>
./setup.sh

Tower should be up and running on the host.
