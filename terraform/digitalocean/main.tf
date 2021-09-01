terraform {
  required_version = "~> 1.0.0"

  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

provider "digitalocean" {}

resource "digitalocean_droplet" "web" {
  image     = "ubuntu-20-04-x64"
  name      = "web"
  region    = "fra1"
  size      = "s-1vcpu-1gb"
  user_data = file("conf.yaml")
}