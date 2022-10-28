#!/bin/bash

# shellcheck disable=SC2164
cd /opt/yeabook

while ! nc -z "$ASTERISK_HOST" "$ASTERISK_SSH_PORT"; do
      sleep 0.1
done

python3.11 main.py
