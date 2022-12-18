run-dev:
	@docker-compose up --build -d app worker redis postgres flower

run-prod:
	@docker-compose up --build -d app worker redis flower

stop:
	@docker-compose -t 10 stop

destroy:
	@docker-compose down -v