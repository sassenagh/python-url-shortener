resource "google_container_cluster" "primary" {
  name     = var.cluster_name
  location = var.region
  # remove_default_node_pool = true
  initial_node_count       = 1

    node_config {
    machine_type = "e2-micro"
    disk_type    = "pd-ssd"
    disk_size_gb = 15
  }
}

# resource "google_container_node_pool" "primary_nodes" {
#   name       = "primary-node-pool"
#   cluster    = google_container_cluster.primary.name
#   location   = var.region

#   initial_node_count = 1

#   autoscaling {
#     min_node_count = 1
#     max_node_count = 2
#   }
# }