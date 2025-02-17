"""Integration tests for the events_raw pipeilne"""

import pytest
from databricks.sdk import WorkspaceClient


@pytest.fixture
def fx_dbx_workspace() -> WorkspaceClient:
    wsclient = WorkspaceClient()
    return wsclient


def test_continuous(
    fx_dbx_workspace: WorkspaceClient, pipeline_name: str = "events_raw"
):
    """Verify that the ingestion table is running continuously."""
    for pipeline in fx_dbx_workspace.pipelines.list_pipelines():
        if pipeline_name in pipeline.name:
            assert str(pipeline.state).split(".")[-1] == "RUNNING"
