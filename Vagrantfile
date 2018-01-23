# -*- mode: ruby -*-
# vi: set ft=ruby :

$NODES=4
$NODEMEM=256
# Overwrite host locale in ssh session
ENV["LC_ALL"] = "en_US.UTF-8"

# All Vagrant configuration is done here.
Vagrant.configure("2") do |cluster|
  # The most common configuration options are documented and commented below.
  # For more refer to https://www.vagrantup.com/docs/vagrantfile/

  # Every Vagrant virtual environment requires a box to build off of.

  # The ordering of these 2 lines expresses a preference for a hypervisor
  cluster.vm.provider "virtualbox"
  cluster.vm.provider "libvirt"
  cluster.vm.provider "vmware_fusion"

  # Avoid using the Virtualbox guest additions
  cluster.vm.synced_folder ".", "/vagrant", disabled: true
  if Vagrant.has_plugin?("vagrant-vbguest")
    cluster.vbguest.auto_update = false
  end

  # For convenience, testing and instruction, all you need is 'vagrant up'
  # Every vagrant box comes with a user 'vagrant' with password 'vagrant'
  # Every vagrant box has the root password 'vagrant'

  # This vagrant box is downloaded from https://vagrantcloud.com/centos/7
  # Other variants https://app.vagrantup.com/boxes/search
  cluster.vm.box = "centos/7"
  cluster.ssh.insert_key = false
  # Don't install your own key (you might not have it)
  # Use this: $HOME/.vagrant.d/insecure_private_key

  # host to run ansible and tower
  cluster.vm.define "ansible", primary: true do |config|
    config.vm.hostname = "ansible"
    config.vm.network :private_network, ip: "10.42.0.2"
    config.ssh.forward_agent = true
    config.vm.provider :virtualbox do |vb, override|
      vb.customize [
        "modifyvm", :id,
        "--name", "ansible",
        "--memory", "2048",
        "--cpus", 1
      ]
    end
  end

  # hosts to run ansible-core
  (1..$NODES).each do |i|
    cluster.vm.define "node-#{i}" do |node|
      node.vm.hostname = "node-#{i}"
      node.vm.box = "centos/7"
      node.vm.network :private_network, ip: "10.42.0.#{i+5}"
      node.vm.provider :virtualbox do |vb, override|
      vb.customize [
        "modifyvm", :id,
        "--name", "node-#{i}",
        "--memory", "#$NODEMEM",
        "--cpus", 1
      ]
      end
    end
  end
end
