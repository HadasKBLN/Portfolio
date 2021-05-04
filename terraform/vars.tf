# GCP authentication file
variable "auth_file" {
  type        = string
  default = "/home/hadas/.ssh/devops-portfolio-key.json"
}
# define GCP region
variable "region" {
  type        = string
  default = "us-central1"
}


variable "region_zone" {
  default = "us-central1-a"
}

# define GCP project name
variable "project_name" {
  type        = string
  default = "devops-portfolio"
}

variable "public_subnet_cidr_1" {
  type        = string
  default = "10.10.1.0/24"
}

variable "public_key_path" {
  description = "Path to file containing public key"
  default     = "/home/hadas/.ssh/id_ed25519.pub"
}

variable "private_key_path" {
  description = "Path to file containing private key"
  default     = "/home/hadas/.ssh/id_ed25519"
}
