# adf-delta-lake-copy-demo


# Azure Resources Required
- Azure Blob Storage Account
- Azure Key Vault
- Azure Databricks Workspace
- Azure Data Factory

# Instructions
1. Create the Azure Resources above.  
2. Configure Azure Key Vault with access policy type of Azure role-based access control
3. Assign IAM role Key Vault Administrator to your Azure AD login in the Access Control settings for your Azure Key Vault.
4. Assign IAM role Key Vault Secrets User to your Azure Data Factory instance in the Access Control settings for your Azure Key Vault.
5. Create Azure Databricks PAT Token and save value to databricks-token secret in your Azure Key Vault
6. Get connection string for you Azure Blob Storage account and save value to storage-connstring secret in your Azure Key vault.
7. Create a secret scope in Azure Databricks workspace linked to Azure Key Vault
8. Setup Azure Databricks demo cluster with Spark configuration your Blob Storage account key using Azure Key Vault backed secret scope to the databricks-token secret: <br>
  fs.azure.account.key.yourblobstorageaccountname.blob.core.windows.net {{secrets/yoursecretscopename/databricks-token}} <br>
9. Create adfdemo container in Azure Blob Storage account
10. Run ADF Delta Lake Copy Demo Setup notebook in Datbricks using demo cluster to load your input file to Blob Storage and create the primary Delta Lake table.
11. Run Azure Data Factory adftaxidemo pipeline to copy data from Blob storage to Delta Lake table and back out to a folder in Blob Storage.


