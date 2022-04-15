# adf-delta-lake-copy-demo


# Azure Resources Required
- Azure Blob Storage Account
- Azure Databricks Workspace
- Azure Data Factory

# Instructions
1. Create the Azure Resources above.
2. Assign IAM role Contributor to your Azure Data Factory instance in the Access Control settings for your Azure Databricks Workspace.
3. Assign IAM role Storage Blob Data Contributor to your Azure Data Factory instance in the Access Control settings for your Azure Blob Storage account.
4. Add Azure Key Vault Access Policy for your user Azure AD login with the Secret Management template.
5. Add secret named storagekey to your Azure Key Vault secrets using access key from your Azure Blob Storage Account. 
6. Create a secret scope named adfdemo in Azure Databricks workspace linked to Azure Key Vault <br> https://docs.microsoft.com/en-us/azure/databricks/security/secrets/secret-scopes#create-an-azure-key-vault-backed-secret-scope-using-the-ui
7. Create Azure Databricks cluster with Spark configuration for your Blob Storage account using Azure Key Vault backed secret scope to the databricks-token secret https://docs.microsoft.com/en-us/azure/databricks/clusters/configure#--spark-configuration: <br>
  fs.azure.account.key.yourblobstorageaccountname.blob.core.windows.net {{secrets/adfdemo/storagekey}} <br>
8. Create adfdemo container in Azure Blob Storage account
9. Import ADF Delta Lake Copy Demo Setup.py notebook into Databricks workspace.
10. Run notebook in Datbricks using demo cluster to load your input file to Blob Storage and create the primary Delta Lake table.
11. Import all Azure Data Factory artifacts from this repo and configure the linked services for the correct Azure Key Vault, Azure Blob Storage, and Azure Databricks Delta Lake settings.
12. Run Azure Data Factory adftaxidemo pipeline to copy data from Blob storage to Delta Lake table and back out to a folder in Blob Storage.
