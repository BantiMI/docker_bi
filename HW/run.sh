#!/bin/bash

case "$1" in
    build_generator)
        echo "Сборка образа"
        docker build -t generator .
        ;;
    run_generator)
        echo "Запуск контейнера"
        mkdir -p data
        docker run --rm -v /d/docker_bi/HW/data:/data generator
        echo "Файл создан в data/data.csv"
        ;;
    create_local_data)
        echo "Создание данных"
        mkdir -p local_data
        python3 generate.py local_data
        echo "Файл создан в local_data/data.csv"
        ;;
    *)
        echo "Использование: $0 {build_generator|run_generator|create_local_data}"
        exit 1
        ;;
esac