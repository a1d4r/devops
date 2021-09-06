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

resource "vagrant_vm" "web_vagrant" {
  vagrantfile_dir = "vagrant"
}