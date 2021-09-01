terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "web_app" {
  name         = "a1d4r/devops-python-app"
  keep_locally = false
}

resource "docker_container" "web_app" {
  image = docker_image.web_app.latest
  name  = "web-app"
  ports {
    internal = 8000
    external = 80
  }
}