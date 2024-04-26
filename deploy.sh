#!/bin/bash

# Set the GCP project ID
PROJECT_ID='serenaid-421315'
APP_NAME='serenaid-backend'
IMAGE_NAME="gcr.io/$PROJECT_ID/$APP_NAME"
REGION='us-central1-a'
CLUSTER_NAME='serenaid-cluster'
NAMESPACE='default'

# Set the project ID
echo "Setting project ID..."
gcloud config set project $PROJECT_ID

# Build the Docker image
echo "Building Docker image..."
gcloud builds submit --tag $IMAGE_NAME

# Get credentials for the cluster
echo "Getting credentials for cluster..."
gcloud container clusters get-credentials $CLUSTER_NAME --region $REGION --project $PROJECT_ID

# Deploy to GKE
echo "Deploying to Google Kubernetes Engine..."
kubectl apply -f k8s/

# Update the image in the deployment to ensure the latest is used
echo "Updating deployment with new image..."
kubectl set image deployment/$APP_NAME $APP_NAME=$IMAGE_NAME --namespace $NAMESPACE

echo "Deployment complete."
