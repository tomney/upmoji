### Deployment
 Get GCloud to point to your project. If you have access to the upmoji project, this can be done by running
 ```
 gcloud config set project ace-shine-212419
 ```

 You can also specify the zone via:
 ```
 gcloud config set compute/zone us-central1-a
 ```

 Now we will want to specify an environment variable to get the project id.
 ```
 export PROJECT_ID="$(gcloud config get-value project -q)"
 ```

If `docker` is not already configured on your computer, you must download it and set it up. You should be able to find a working version [here]{https://docs.docker.com/install/overview/}.

Once `docker` is running on your machine, you can build the image by running the following command in the same directory as the Dockerfile:
```
docker build -t gcr.io/${PROJECT_ID}/upmoji:gke .
```
Note the period to indicate the directory. The `upmoji` part is the tag for this project. Feel free to use different tags for custom versions.

Check to see that the image can be run locally via"
```
docker run --rm -p 8080:80 gcr.io/${PROJECT_ID}/upmoji:gke
```
If it is ever necessary to edit the port allocations it is helpful to note that `-p` is used to specify port allocations where the first port is the port you will access locally and the second port is the exposed port on the docker container.

Once the docker image is built you should be able to see it in your list of local docker images by running:
```
docker image ls
```

The image can then be pushed to the Google Cloud Container Registry via
```
docker push gcr.io/${PROJECT_ID}/upmoji:gke
```

Ensure that you are logged in to your docker account, or the push request will fail.

A deployment can be created from the image through the container registry in Google Cloud Platform.

If you experience a lot of trouble it is likely that your firewall setting are not configured properly. You can edit firewall rules in the VPC Networks option in GCP. Also, note that the default GCE web addresses are not HTTPS.
