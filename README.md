# Yottaa Data Analytics

## Repo Structure

├── README.md - you're reading this
├── archive - old code that will be integrated into /src/. This will go away
│   └── scratch.py
├── databricks.yml - The primary Databricks Asset Bundle configuration.
├── devenv.lock - A lock file for devenv
├── devenv.nix - The Nix configuration for devenv
├── devenv.yaml - The Yaml configuration for devenv
├── pytest.ini - A configuration file for Pytest
├── requirements-dev.txt - Requirements for developing on this project. This is not used yet
├── requirements-tst.txt - Requirements for testing this project. Used in `prd_cicd.yml`
├── resources - A repo for resources managed by Databricks Asset Bundles
│   └── events_raw.pipeline.yml - The events_raw ingestion pipeline
├── src - All Python code and notebooks lives here
│   └── events_raw.py
└── tests - All testing code lives here
├── integration
│   └── test_events_raw.py
└── unit
└── test_dummy.py

## Asset Bundles

This repo uses Databricks Asset Bundles to deploy and manage resources within Databricks.
For documentation on the Databricks asset bundles format used for this project, and for CI/CD configuration, see:

- **High-level overview**: https://docs.databricks.com/dev-tools/bundles/index.html.
- **Configuration reference**: https://docs.databricks.com/en/dev-tools/bundles/reference.html

## Local Development

1. Install the Databricks CLI from https://docs.databricks.com/dev-tools/cli/databricks-cli.html

2. Authenticate to your Databricks workspace, if you have not done so already:

```
$ databricks configure
```

Here are a couple of the commands you may want to use if manually dealing with asset bundles.
Note: none of this is necessary because the Github Actions pipeline deploys your bundle
on every commit to a branch other than main.

- To deploy a development copy of this project, type:

  ```
  $ databricks bundle deploy --target dev
  ```

  (Note that "dev" is the default target, so the `--target` parameter
  is optional here.)

  This deploys everything that's defined for this project.
  For example, the default template would deploy a job called
  `[dev yourname] yottaa_job` to your workspace.
  You can find that job by opening your workpace and clicking on **Workflows**.

- Similarly, to deploy a production copy, type:

  ```
  $ databricks bundle deploy --target prod
  ```

  Note that the default job from the template has a schedule that runs every day
  (defined in resources/yottaa.job.yml). The schedule
  is paused when deploying in development mode (see
  https://docs.databricks.com/dev-tools/bundles/deployment-modes.html).

- To run a job or pipeline, use the "run" command:

  ```
  $ databricks bundle run
  ```

- Optionally, install developer tools such as the Databricks extension for Visual Studio Code from
  https://docs.databricks.com/dev-tools/vscode-ext.html. Or read the "getting started" documentation for
  **Databricks Connect** for instructions on running the included Python code from a different IDE.
