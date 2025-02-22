# Databricks Asset Bundle Deployment

See the associated blog post to this repo here: https://evanazevedo.com/blog/databricks-deployment

## Deployment

### Asset Bundles

This repo uses Databricks Asset Bundles to deploy and manage resources within Databricks.
For documentation on the Databricks asset bundles format used for this project, see:

- **High-level overview**: https://docs.databricks.com/dev-tools/bundles/index.html.
- **Configuration reference**: https://docs.databricks.com/en/dev-tools/bundles/reference.html

### Service Principals

There are 2 service principals: one each for staging and production.
They each have an OAuth token that was created in the Databricks portal that are used to authenticate the Github Action Runner to Databricks.
The OAuth token consists of a Secret, and it is stored in the assocated Github Environment as a secret.
The Service Principal's ID is also stored in the Github Environment as variable.
Here is a screenshot of the production environment setup in Github:

![Github Environments](docs/images/github_environment.png)

The OAuth key for the Databricks service principal prd_sp stored as environment variables DBX_SP_ID and DBX_SP_SECRET, respectively.
This holds across all three environments, and the names are as follows:

| Github Environment Name | Databricks Service Principal Name |
| ----------------------- | --------------------------------- |
| stage                   | stage_sp                          |
| prod                    | prod_sp                           |

You can find the service principal by

1. Start at the homepage of the Databricks environment
2. Click on your user icon in the top right and select Settings.
3. You’ll find the service principal under Settings > Identity and access > Service Principals
