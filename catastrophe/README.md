Using Your Swarm Cluster
========================

This directory contains all of the files the Docker CLI will need to
communicate with your Swarm Cluster. The included files are:

* ca.pem - Certificate Authority, used by clients to validate servers
* cert.pem - Client Certificate, used by clients to identify themselves to servers
* key.pem - Client Private Key, used by clients to encrypt their requests
* ca-key.pem - Certificate Authority Key, private file used to generate more client certificates.
* docker.env - Shell environment config file


Configuring Docker CLI
----------------------

The easiest way to configure the Docker CLI to communicate with the Swarm
Cluster is via environment variables. The provided 'docker.env' can be
sourced into your environment to set the required variables. When ever you
start a new shell session you will need to source the 'docker.env' file to
set the proper environment variables. You only need to do this once per
session though.

    $ source docker.env
    $ docker info
    Containers: 4
    Strategy: spread
    Filters: affinity, health, constraint, port, dependency
    Nodes: 2
     swarm-n1: 192.168.1.2:42376
      └ Containers: 2
      └ Reserved CPUs: 0 / 12
      └ Reserved Memory: 0 B / 2.1 GiB
     swarm-n2: 192.168.1.3:42376
      └ Containers: 2
      └ Reserved CPUs: 0 / 12
      └ Reserved Memory: 0 B / 2.1 GiB

When communicating with Swarm, the 'docker info' command will show global
details about the cluster and specific details about each node.


Running your first container
----------------------------

If you haven't sourced 'docker.env' you will need to do so before running
your first container. In this example, we will spawn a container running
an interactive shell.

First, make sure you've got the proper environment variables set by sourcing
'docker.env'. Next, we will actually run the container with 'docker run --rm
-it <image> <command>'. In our case, we will use the 'cirros' image, which is
a tiny demo image, and the '/bin/sh' command. It will take a short while for
Docker to run the container but when it is done, you will have an interactive
shell. To test out this container, we can run hostname, which will return the
short id of the container. The container also has network access, so you can
use ping to test networking. Lastly, to exit the container, simply issue an
'exit' command.

    $ source docker.env
    $ docker run --rm -it cirros /bin/sh
    / # hostname
    7bcfb8c82455
    / #  ping -c 4 8.8.8.8
    PING 8.8.8.8 (8.8.8.8): 56 data bytes
    64 bytes from 8.8.8.8: seq=0 ttl=42 time=9.457 ms
    64 bytes from 8.8.8.8: seq=1 ttl=42 time=9.633 ms
    64 bytes from 8.8.8.8: seq=2 ttl=42 time=9.527 ms
    64 bytes from 8.8.8.8: seq=3 ttl=42 time=9.654 ms

    --- 8.8.8.8 ping statistics ---
    4 packets transmitted, 4 packets received, 0% packet loss
    round-trip min/avg/max = 9.457/9.567/9.654 ms
    / #  exit

And, with that you've successfully used a Docker container! You can find more
details on available Docker CLI commands in their [documentation](https://docs.docker.com/reference/commandline/cli/ "Docker CLI Documentation").

