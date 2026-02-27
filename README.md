# Business Central Integration (Tendersure)

This module handles the Service-to-Service (S2S) authentication and data retrieval from Microsoft Dynamics 365 Business Central using a Multi-tenant Azure App Registration.

---

## 🛠️ Setup Requirements

### 1. Environment Variables
Create a .env file in the root directory. Replace the placeholders with your specific Azure and Business Central credentials:

| Variable | Value |
| :--- | :--- |
| AZURE_CLIENT_ID | your_azure_app_client_id |
| AZURE_CLIENT_SECRET | your_azure_app_client_secret |
| AZURE_TENANT_ID | your_work_tenant_id |
| BC_ENVIRONMENT | Sandbox or Production |
| BC_COMPANY_ID | your_target_company_guid |

Example .env:
AZURE_CLIENT_ID=
AZURE_CLIENT_SECRET=
AZURE_TENANT_ID=
BC_ENVIRONMENT=Sandbox
BC_COMPANY_ID=

### 2. Install Requirements
Ensure you have your virtual environment active, then install the necessary dependencies:

pip install -r requirements.txt

---

## Usage Example

The BusinessCentralService class manages token acquisition and API requests automatically.

from businesscentralservice import BusinessCentralService

# Initialize the service
bcs = BusinessCentralService()

# Retrieve purchase orders
data = bcs.get_purchase_orders()
print(data)

---

## Security
Do not commit your .env file to your repository. Ensure it is listed in your .gitignore to prevent leaking sensitive Azure credentials.