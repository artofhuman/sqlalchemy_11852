RUN := run --rm
DB := development
DOCKER_COMPOSE := docker-compose
DOCKER_COMPOSE_RUN := ${DOCKER_COMPOSE} $(RUN)

compose-bash:
	${DOCKER_COMPOSE_RUN} app bash
