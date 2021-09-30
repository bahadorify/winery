# winery
App for matching wine price from https://www.vinmonopolet.no with wine score from https://cellartracker.com 

### List of technologies/libraries proposed:
* DigitalOcean :white_check_mark:
* Python :white_check_mark:
* Flask :white_check_mark:
* Nginx
* MongoDB :white_check_mark:
* GitHub CI/CD

### Project deployment
1. Checkout the repo, set ```.env``` file in root directory with `MONGO_PASSWORD` and `MONGO_HOST` variables
2. Deploy the MongoDB and Flask with `docker-compose up -d --build`
3. Build scraper Docker image from `./ci/spider` directory or use one from a DO registry `registry.digitalocean.com/omega/vin:latest` 
4. Fill the DB using `docker run --rm -it --env-file .env --net=host vin --categories rødvin hvitvin`
5. Check the results with Flask: `http://127.0.0.1:8000`
