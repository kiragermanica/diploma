# Используем последнюю версию Ubuntu
FROM ubuntu:latest

# Обновляем пакеты
RUN apt-get update && apt-get upgrade -y

# Устанавливаем необходимые утилиты
RUN apt-get install -y \
    curl \
    git \
    vim \
    nano \
    net-tools \
    tree \
    python3 \
    python3-pip \
    php \
    php-cli \
    # Дополнительные утилиты
    jq \
    htop \
    tmux \
    wget \
    zsh \
    # Инструменты для разработки
    build-essential \
    cmake \
    clang \
    lldb \
    gdb \
    # Средства безопасности
    ufw \
    fail2ban \
    # Средства мониторинга
    prometheus-node-exporter \
    grafana

# Настраиваем sudo без пароля
RUN echo "max ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Добавляем случайные capabilities
RUN setcap cap_net_bind_service=+ep /usr/bin/php

# Устанавливаем suid на vim
RUN chmod u+s /usr/bin/vim

# Копируем файлы приложения в контейнер
COPY . /app

# Запускаем PHP-сервер
CMD ["php", "-S", "0.0.0.0:8000", "-t", "/app"]

# Запускаем Python-приложение
CMD ["python3", "/app/app/app.py"]

# Создаем пользователя "max"
RUN useradd -m max

# Устанавливаем Python-библиотеки
RUN pip3 install requests flask sqlite3 \
    # Дополнительные библиотеки
    pandas \
    numpy \
    matplotlib \
    scikit-learn \
    tensorflow \
    pytorch

# Настраиваем зону часового пояса
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Конфигурируем Prometheus Node Exporter
RUN mkdir /etc/prometheus
COPY prometheus-node-exporter.yml /etc/prometheus/
CMD ["prometheus-node-exporter", "--config.file=/etc/prometheus/prometheus-node-exporter.yml"]

# Конфигурируем Grafana
RUN mkdir /etc/grafana
COPY grafana.ini /etc/grafana/
CMD ["grafana-server", "--config=/etc/grafana/grafana.ini"]
