build:
	docker-compose build
test:
	docker exec -it 2022-mai-backend-m-potenko_web_1 python3.8 manage.py test
migrate:
	docker exec -it 2022-mai-backend-m-potenko_web_1 python3.8 manage.py migrate
# up:	build
# 	docker-compose up -d
up:
	docker-compose up -d

down:
	docker-compose down --volumes
shell:
	docker exec -it 2022-mai-backend-m-potenko_web_1 python3.8 manage.py shell