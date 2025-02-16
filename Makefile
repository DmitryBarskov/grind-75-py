sh:
	docker compose run -it --rm py sh

lint:
	docker compose run -it --rm py python -m pylint src/

build: .env
	docker compose build
	docker compose run -it --rm py pip install -r ./requirements.txt -t .packages

.env:
	echo "USER_ID=$$(id -u)\nGROUP_ID=$$(id -g)" > .env
