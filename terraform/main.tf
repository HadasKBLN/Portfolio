provider "google" {
  region      = "${var.region}"
  zone         = "${var.region_zone}"
  project     = "${var.project_name}"
  credentials = "${file("${var.auth_file}")}"
}

resource "google_compute_instance" "docker" {
  count = 1

  name         = "tf-docker-${count.index}"
  machine_type = "g1-small"
  tags         = ["docker-node"]

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-1404-trusty-v20160602"
    }
  }

  network_interface {
    network = "default"
    access_config {
      nat_ip = google_compute_address.static.address
    }
  }




  provisioner "remote-exec" {
    connection {
      host        = google_compute_address.static.address
      type        = "ssh"
      user        = "root"
      private_key = "${file("${var.private_key_path}")}"
      agent       = false
    }

    inline = [
      "sudo curl -sSL https://get.docker.com/ | sh",
      "sudo usermod -aG docker `echo $USER`",
      "sudo docker network create jen",
      "sudo docker run -d -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --name jenkins --network jen -p 80:8080 hadask/jenkins_with_docker:1.0.0"
    ]
  }

  depends_on = [ google_compute_firewall.firewall, google_compute_firewall.webserverrule ]

  service_account {
    email = "devops-portfolio-763@devops-portfolio.iam.gserviceaccount.com"
    scopes = ["https://www.googleapis.com/auth/compute.readonly"]
  }
    metadata = {
    ssh-keys = "root:${file("${var.public_key_path}")}"
  }
}

# resource "google_compute_firewall" "default" {
#   name    = "tf-www-firewall"
#   network = "default"

#   allow {
#     protocol = "tcp"
#     ports    = ["80"]
#   }

#   source_ranges = ["0.0.0.0/0"]
#   target_tags   = ["docker-node"]
# }

resource "google_compute_firewall" "firewall" {
  name    = "gritfy-firewall-externalssh"
  network = "default"
  allow {
    protocol = "tcp"
    ports    = ["22","8080"]
  }
  source_ranges = ["0.0.0.0/0"] # Not So Secure. Limit the Source Range
  target_tags   = ["externalssh"]
}

resource "google_compute_firewall" "webserverrule" {
  name    = "gritfy-webserver"
  network = "default"
  allow {
    protocol = "tcp"
    ports    = ["80","443","8080"]
  }
  source_ranges = ["0.0.0.0/0"] # Not So Secure. Limit the Source Range
  target_tags   = ["webserver"]
}

# We create a public IP address for our google compute instance to utilize
resource "google_compute_address" "static" {
  name = "vm-public-address"
  project = "${var.project_name}"
  region = "${var.region}"
  depends_on = [ google_compute_firewall.firewall ]
}
