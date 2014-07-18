# -*- mode: ruby -*-
# vi: set ft=ruby :


CENTOS = {
  box: "opscode-centos-6.5",
  virtualbox_url: "http://opscode-vm-bento.s3.amazonaws.com/vagrant/virtualbox/opscode_centos-6.5_chef-provisionerless.box",
  vmware_fusion_url: "http://opscode-vm-bento.s3.amazonaws.com/vagrant/vmware/opscode_centos-6.5_chef-provisionerless.box"
}
UBUNTU = {
  box: "opscode-ubuntu-12.04",
  virtualbox_url: "http://opscode-vm-bento.s3.amazonaws.com/vagrant/virtualbox/opscode_ubuntu-12.04_chef-provisionerless.box",
  vmware_fusion_url: "http://opscode-vm-bento.s3.amazonaws.com/vagrant/vmware/opscode_ubuntu-12.04_chef-provisionerless.box"
}

VAGRANTFILE_API_VERSION = "2"
OS = ENV["VAGRANT_OS"].nil? ? CENTOS : Kernel.const_get(ENV["VAGRANT_OS"])
NODES = ENV["TRAINING_NODES"].nil? ? 3 : ENV["TRAINING_NODES"].to_i

Vagrant.configure(VAGRANTFILE_API_VERSION) do |cluster|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.

cluster.vm.define "node-1" do |config|
  config.vm.box = CENTOS[:box]
  config.vm.provider :virtualbox do |vb, override|
    vb.customize ["modifyvm", :id, "--memory", "128"]
    vb.customize ["modifyvm", :id, "--cpus", "1"]
  end

  config.vm.provider :vmware_fusion do |vm, override|
    vm.vmx["memsize"] = "128"
    vm.vmx["numvcpus"] = "1"
  end

  config.vm.hostname = "node-1"
  config.vm.network :private_network, ip: "10.42.0.6"
end

cluster.vm.define "node-2" do |config|
  config.vm.box = CENTOS[:box]
  config.vm.provider :virtualbox do |vb, override|
    vb.customize ["modifyvm", :id, "--memory", "128"]
    vb.customize ["modifyvm", :id, "--cpus", "1"]
  end

  config.vm.provider :vmware_fusion do |vm, override|
    vm.vmx["memsize"] = "128"
    vm.vmx["numvcpus"] = "1"
  end

  config.vm.hostname = "node-2"
  config.vm.network :private_network, ip: "10.42.0.7"
end

cluster.vm.define "node-3" do |config|
  config.vm.box = UBUNTU[:box]
  config.vm.provider :virtualbox do |vb, override|
    vb.customize ["modifyvm", :id, "--memory", "128"]
    vb.customize ["modifyvm", :id, "--cpus", "1"]
  end

  config.vm.provider :vmware_fusion do |vm, override|
    vm.vmx["memsize"] = "128"
    vm.vmx["numvcpus"] = "1"
  end

  config.vm.hostname = "node-3"
  config.vm.network :private_network, ip: "10.42.0.8"
end


cluster.vm.define "haproxy" do |config|
  config.vm.box = "opscode-centos-6.5"
  config.vm.provider :virtualbox do |vb, override|
    vb.customize ["modifyvm", :id, "--memory", "128"]
    vb.customize ["modifyvm", :id, "--cpus", "1"]
  end

  config.vm.provider :vmware_fusion do |vm, override|
    vm.vmx["memsize"] = "1024"
    vm.vmx["numvcpus"] = "1"
  end

  config.vm.hostname = "haproxy"
  config.vm.network :private_network, ip: "10.42.0.100"
end


cluster.vm.define "tower" do |config|
  config.vm.box = "opscode-centos-6.5"
  config.vm.provider :virtualbox do |vb, override|
    vb.customize ["modifyvm", :id, "--memory", "1024"]
    vb.customize ["modifyvm", :id, "--cpus", "1"]
  end

  config.vm.provider :vmware_fusion do |vm, override|
    vm.vmx["memsize"] = "1024"
    vm.vmx["numvcpus"] = "1"
  end

  config.vm.hostname = "tower"
  config.vm.network :private_network, ip: "10.42.0.200"
end
end
