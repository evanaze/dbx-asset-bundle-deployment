set -exo pipefail

# Get the pipeline id
PIPELINE_ID=$(databricks pipelines list-pipelines -t stage -p stage | jq -r '.[] | select(.name == "events_raw") | .pipeline_id')

# Get the pipeline status
STATUS=$(databricks pipelines get -t stage -p stage $PIPELINE_ID | jq -r '.state')
echo "Current state: $STATUS"

if [[ "$STATUS" == "RUNNING" || "$STATUS" == "IDLE" ]]; then
  sleep 1
fi
sleep 10

