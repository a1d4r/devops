terraform {
  required_providers {
    vagrant = {
      source  = "bmatcuk/vagrant"
      version = "~> 4.0.0"
    }
  }
}

provider "vagrant" {
  # no config
}

resource "vagrant_vm" "my_vagrant_vm" {
  vagrantfile_dir = "vagrant"
}