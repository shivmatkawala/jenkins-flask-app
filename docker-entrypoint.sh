#!/bin/bash
# Give Jenkins user access to Docker socket
if [ -S /var/run/docker.sock ]; then
    chgrp docker /var/run/docker.sock
    chmod 660 /var/run/docker.sock
fi

# Execute original CMD
exec "$@"
