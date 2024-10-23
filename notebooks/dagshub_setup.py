import mlflow

import dagshub

dagsHubUri = "https://dagshub.com/SHIVRAJSHINDE/miniProMlOps.mlflow"

mlflow.set_tracking_uri(dagsHubUri)
dagshub.init(repo_owner='SHIVRAJSHINDE', repo_name='miniProMlOps', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)