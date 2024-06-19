variable "project" {
  description = "Project"
  default     = "my-dbt-project-426120"
}

variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my-dbt-project-426120-050c4ec7248d.json"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "bq_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "my-dbt-project-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}