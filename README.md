# Recipe Data ETL

## Overview

### Python Scripts

This Python script downloads a JSON file containing recipes from a web URL, parses the data into a Pandas DataFrame, filters recipes based on ingredients containing specific keywords ('chilies', 'chiles', 'chili'), calculates the difficulty level of each recipe based on preparation and cooking times, and outputs the filtered recipes with difficulty levels to a CSV file.

#### Requirements

- Python 3.11.5 or higher
- Required Python modules specified in requirements.txt

#### Installation

1. Clone the repository using the following command:
```bash
git clone https://github.com/QzQz-2000/recipes-etl.git
cd recipes-etl
```

2. Install dependencies:

Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

### Run the python script

Execute the python script:

```bash
python recipes_etl.py
```

### Orchestrated ETL pipeline

Now we can undertake an interesting experiment. Earlier, we implemented an ETL process using Python. We can now attempt to build a well-orchestrated ETL pipeline and upload the final CSV file to a cloud platform. This aims to streamline data processing workflows, ensure data integrity, and enable efficient analytics and reporting.

#### Technologies used

- **Mage:**
  - Open-source data pipeline tool for transforming and integrating data.
- **Docker:**
  - Containerization platform for packaging applications and dependencies.
- **Terraform:**
  - Infrastructure as code (IaC) tool for provisioning and managing cloud resources.
- **Google Cloud Storage and BigQuery:**
  - Cloud storage and data warehousing solutions for storing and analyzing large datasets.

#### Prerequisites

Before you can start working with this project, ensure you have the following prerequisites installed and set up:

1. **Google Cloud Platform (GCP) Account**

You'll need a GCP account to use Google Cloud services such as Google Cloud Storage. If you don't have a GCP account, sign up for free [here](https://cloud.google.com/free).

2. **Terraform**

Terraform is used for provisioning and managing cloud infrastructure.

- Make sure you have installed Terraform, if not, follow the instructions [here](https://developer.hashicorp.com/terraform/install).
- Verify the installation by running `terraform --version` in your terminal.

3. **Docker**

- Install Docker Desktop for your operating system by following the instructions in the [official documentation](https://docs.docker.com/get-docker/).
- Verify Docker installation by running `docker --version` in your terminal.

4. **Mage**

- Install Mage by following the instructions in the [official documentation](https://docs.mage.ai/introduction/overview)

#### Running the pipeline

After installing the prerequisites, follow these steps.

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

   ```bash
   git clone
   ```

2. **Set Up GCP Authentication**: Configure authentication for Google Cloud Platform by following the instructions [here](https://cloud.google.com/docs/authentication/getting-started).

3. **Initialize Terraform**: Navigate to the `terraform` directory and initialize Terraform by running the following command:

   ```bash
   terraform init
   terraform plan
   terraform apply
   ```

4. **Start Mage**: Navigate to the `Mage` directory and start Mage by doing `docker-compose up`. The navigate to http://localhost:6789 in your browser to use Mage.

5. **Deploy the Data Pipeline**: Run the exporters, loaders and transofmers located inside the dags folder. This will ingest the data to the Google Cloud Storage, and from there to BigQuery. Make sure to run the pipeline as follows:

   ![f1](./images/f1.png)

6. Then in Google cloud Storage, navigate to your bucket. There you can see the uploaded CSV file. 

   ![gcs](./images/gcs.png)

   In BigQuery you can see the `recipe` table we created in Mage. There we can do some SQL analysis.

   ![bq](./images/bq.png)

   

## Files

**recipes_etl.py**: Main Python script that downloads, processes, and analyzes recipes data.

**requirements.txt**: Specifies Python packages required to run the script.

**README.md**: Providing instructions and information about the script.

**final_recipes.csv**: Final output CSV file containing filtered recipes with difficulty levels.
