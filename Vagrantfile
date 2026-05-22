# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.network "forwarded_port", guest: 3000, host: 3000
  
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y nodejs npm
    npm install -g juice-shop
    juice-shop &
  SHELL
end
