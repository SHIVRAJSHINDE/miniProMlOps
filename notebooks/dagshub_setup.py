import mlflow

import dagshub

mlflow.set_tracking_uri('https://dagshub.com/SHIVRAJSHINDE/miniProMlOps.mlflow')
dagshub.init(repo_owner='SHIVRAJSHINDE', repo_name='miniProMlOps', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)