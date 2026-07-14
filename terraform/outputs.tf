output "development_namespace" {
  value = kubernetes_namespace_v1.school_dev.metadata[0].name
}

output "production_namespace" {
  value = kubernetes_namespace_v1.school_prod.metadata[0].name
}
