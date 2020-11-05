resource "google_storage_bucket" "data-load-build" {

    name = "gcp-data-load-build",
    location = "US",
    force_destroy = true
    storage_class = "REGIONAL"

    lifecycle_rule {
        condition {
            age = 90
        }
        action {
            type = "Delete"
        }
    }

}

resource "google_storage_bucket" "data-load-lake" {

    name = "gcp-data-load-lake",
    location = "US",
    force_destroy = true
    storage_class = "REGIONAL"

    lifecycle_rule {
        condition {
            age = 90
        }
        action {
            type = "Delete"
        }
    }

}

