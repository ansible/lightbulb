#! /bin/sh

yum -y install yum-utils creatrepo epel-release
yum -y install s3cmd
#need to update $HOME/.s3cfg with s3 credentials

cat <<EOF>/etc/yum.repos.d/influxdb.repo
[influxdb]
name = InfluxDB Repository - CentOS \$releasever
baseurl = https://repos.influxdata.com/centos/\$releasever/\$basearch/stable
enabled = 1
gpgcheck = 1
gpgkey = https://repos.influxdata.com/influxdb.key
EOF

reposync --repoid=influxdb --download_path=/vagrant/resources
wget https://repos.influxdata.com/influxdb.key -P /vagrant/resources/influxdb/
createrepo /vagrant/resources/influxdb

mkdir /vagrant/resources/grafana
wget https://grafanarel.s3.amazonaws.com/builds/grafana-2.6.0-1.x86_64.rpm -P /vagrant/resources/grafana

s3cmd sync /vagrant/resources/* s3://ansible-training-resources
