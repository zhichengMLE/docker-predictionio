docker-predictionio
===================

## Run [PredictionIO](http://prediction.io) inside Docker

1. Run ```build``` to build the image
2. Run ```shell``` to start the container
3. Once inside the container, run ```runsvdir-start&``` to start everything
4. The Dashboard is available on port 9000

## Run [quickstart](http://predictionio.incubator.apache.org/templates/recommendation/quickstart/)

1. Go to quickstartapp directory ```cd /quickstartapp```
2. Build and Train Engine ```./run.sh```
3. Deploy Engine ```cd MyRecommendation && pio deploy --ip 0.0.0.0&```
4. Your Engine will now listen on port 8000

## Run Univerisal Recommender

### Train and Deploy the Model
1. ```cd /other-engines/ur/```
2. ```./examples/integration-test```

### Query Data
3. ```./examples/multi-query-handmade.sh```
4. 
```
curl -H "Content-Type: application/json" -d '
{
    "user": "u1"
}' http://localhost:8000/queries.json
```
