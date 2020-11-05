#Steps

1. First you need configure google cloud gsutil into your environment

2. And then You need run terraform file into devops folder to provide infrastructure objects on GCP

3. Run scripts/deploy.sh

4. Run that command to create workflow from file: gcloud dataproc workflow-templates instantiate-from-file --file=your-template.yaml --region=region

5. Execute the created workflow template
