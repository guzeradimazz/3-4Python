
#BASE COMMANDS
run:
	python3 manage.py runserver

migration:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

#DOCKER
rundocker:
	${INFO} "Building image..."
	@docker-compose up --build
	${INFO} "Build complete"