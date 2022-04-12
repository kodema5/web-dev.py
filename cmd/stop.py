# manage docker image/containers

import os
import docker

def stop (
    name = "web-dev",
):
    """stops docker image"""
    print(f"stopping {name} container")
    d = docker.from_env()
    try:
        c = d.containers.get(name)
        c.stop()

    except docker.errors.APIError as e:
        print(f"Error: {str(e)}")
