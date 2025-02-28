sh:
	docker compose run -it --rm py sh

lint:
	docker compose run -it --rm py python -m pylint src/

types:
	docker compose run -it --rm py python -m mypy src/

test:
	docker compose run -it --rm py sh -c 'find src -name "*.py" | xargs python -m doctest'

build: .env
	docker compose build
	docker compose run -it --rm py pip install --upgrade pip -t .packages
	docker compose run -it --rm py pip install -r ./requirements.txt -t .packages

.env:
	echo "USER_ID=$$(id -u)\nGROUP_ID=$$(id -g)" > .env

src/%: FORCE
	docker compose run -it --rm py python -m doctest $@ | sed -r 's/\x1B\[(;?[0-9]{1,3})+[mGK]//g'

FORCE: ;
