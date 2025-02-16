sh:
	docker compose run -it --rm py sh

build: .env
	docker compose build

.env:
	echo "USER_ID=$$(id -u)\nGROUP_ID=$$(id -g)" > .env
