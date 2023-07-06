start:
	docker compose up -d

start-build:
	docker compose up -d --build

start-build-recreate:
	docker compose up -d --build --force-recreate

stop:
	docker compose down

log-app:
	docker compose logs -f app

log-proxy:
	docker compose logs -f nginx
