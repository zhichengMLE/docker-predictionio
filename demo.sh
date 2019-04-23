#!/bin/zsh

echo "------------------------Clean up Container-------------------------"
docker kill $(docker ps -q)

echo "------------------------Start Container-------------------------"
imageId="$(docker run -d -p 9000:9000 -p 8000:8000 -p 7070:7070 predictionio_with_universal_recommender )"
echo "$imageId"

docker exec "$imageId" bash -c "touch test; touch test2; touch test3"
echo "------------------------Run Services-------------------------"
docker exec "$imageId" runsvdir-start&
sleep 10s
docker exec "$imageId" pio status

echo "------------------------Build and Deploy-------------------------"
docker exec "$imageId" bash -c "cd ./other-engines/ur/ ; ./examples/nlt-test ; pio deploy --ip 0.0.0.0"