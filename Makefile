.PHONY: install
install:
	pip install -r requirements.in

.PHONY: shell
shell:
	python manage.py shell -v 2

.PHONY: migrate
migrate:
	python manage.py makemigrations && python manage.py migrate

.PHONY: static
static:
	cd ui && npm i && npm run build && cd .. && python manage.py collectstatic --no-input

.PHONY: up
up:
	python manage.py runserver

.PHONY: ui
ui:
	cd ui && npm i && npm run dev -- --host

.PHONY: docker-up
docker-up:
	cd tools && docker compose up

.PHONY: docker-down
docker-down:
	cd tools && docker compose down