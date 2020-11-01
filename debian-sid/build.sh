#!/usr/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

authorized_keys=$(cat /home/kevin/.ssh/id_rsa.pub)

su - falk -c "podman build -t sft/openage:sid --build-arg authorized_keys=\"${authorized_keys}\" $DIR/."
