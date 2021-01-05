#!/bin/bash

set -e

show_help() {
  echo """
Usage: docker run <imagename> COMMAND
Commands
prod    : Run wsgi server.
celery  : Run celery
"""
}

prepare() {
  until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do sleep 1; done
}

# Run
case "$1" in
prod)
  prepare
  make migrate
  make fixture
  uwsgi --ini uwsgi.ini
  ;;
celery)
  celery -A exchange_rate_aggregator worker -B -l info
  ;;
esac
