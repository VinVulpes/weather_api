# weather_api
CRITICAL!
Check your Api weather token plan, forecast could not work.

Weather API site: https://www.weatherapi.com

Run in Docker container:
1. docker image build -t flask_docker .
2. docker run --name weather_server -p 5000:5000 -d flask_docker
3. curl localhost:5000

OR

1. docker-compose up -d --build

Example current: curl localhost:5000/current/city=Murmansk

or

Example forecast: curl localhost:5000/forecast/city=London&dt=2023-06-10
