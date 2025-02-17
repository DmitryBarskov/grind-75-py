sh:
	docker compose run -it --rm py sh

lint:
	docker compose run -it --rm py python -m pylint src/

test:
	docker compose run -it --rm py sh -c 'find src -name "*.py" | xargs python -m doctest'

build: .env
	docker compose build
	docker compose run -it --rm py pip install -r ./requirements.txt -t .packages

.env:
	echo "USER_ID=$$(id -u)\nGROUP_ID=$$(id -g)" > .env

src/%: FORCE
	docker compose run -it --rm py python -m doctest -v $@

FORCE: ;
