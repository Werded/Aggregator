#!/bin/bash

set -e

show_help() {
    echo """
Usage: docker run <imagename> COMMAND
Commands
dev     : Start a normal Django development server.
lint    : Run lints.
manage  : Start manage.py
prod    : Run wsgi server.
help    : Show this message
celery  : Run celery
"""
}

prepare() {
    until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do sleep 1; done;
}

# Run
case "$1" in
    prod)
        prepare
        uwsgi --ini uwsgi.ini
    ;;
esac
