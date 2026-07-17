terraform {
  required_version = ">= 1.5.0"

  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace_v1" "school_dev" {
  metadata {
    name = "school-dev"

    labels = {
      environment = "development"
      project     = "school-management-platform"
      managed-by  = "terraform"
    }
  }
}

resource "kubernetes_namespace_v1" "school_prod" {
  metadata {
    name = "school-prod"

    labels = {
      environment = "production"
      project     = "school-management-platform"
      managed-by  = "terraform"
    }
  }
}
