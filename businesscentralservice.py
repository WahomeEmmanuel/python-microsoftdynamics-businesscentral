import os
from dotenv import load_dotenv
import msal
import requests

# Load variables from .env
load_dotenv()

class BusinessCentralService:
    def __init__(self):
        # Retrieve from environment variables
        self.client_id = os.getenv("AZURE_CLIENT_ID")
        self.client_secret = os.getenv("AZURE_CLIENT_SECRET")
        self.tenant_id = os.getenv("AZURE_TENANT_ID")
        self.environment = os.getenv("BC_ENVIRONMENT", "Sandbox")

        if not all([self.client_id, self.client_secret, self.tenant_id]):
            raise ValueError("Missing critical Azure credentials in .env file")
        
        self.authority = f"https://login.microsoftonline.com/{self.tenant_id}"
        self.scope = ["https://api.businesscentral.dynamics.com/.default"]
        self.base_url = f"https://api.businesscentral.dynamics.com/v2.0/{self.tenant_id}/{self.environment}/api/v2.0"

    def get_token(self):
        app = msal.ConfidentialClientApplication(
            self.client_id,
            authority=self.authority,
            client_credential=self.client_secret,
        )
        result = app.acquire_token_for_client(scopes=self.scope)
        return result.get("access_token")

    def get_purchase_orders(self):
        token = self.get_token()
        company_id = os.getenv("BC_COMPANY_ID")
        
        # Corrected syntax for v2.0
        url = f"{self.base_url}/companies({company_id})/purchaseOrders?$expand=purchaseOrderLines"
        
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        return response.json()