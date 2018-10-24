# Configure gcloud
gcloud config set project ace-shine-212419
gcloud config set compute/zone us-central1-a

# Set environment variables
export PROJECT_ID="$(gcloud config get-value project -q)"

# Build and push container
docker build -t gcr.io/${PROJECT_ID}/upmoji:gke .
docker push gcr.io/${PROJECT_ID}/upmoji:gke
