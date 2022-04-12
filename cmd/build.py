# builds docker image from dockerfile

import os
import docker

def build (
    name = "web-dev"
):
    """builds docker image"""
    src = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(src, 'dockerfile','.')
    print(f"building '{name}' docker-image from {path}")
    print("this may take a minute")

    d = docker.from_env()
    try:
        d.images.build(
            path = path,
            quiet  = False,
            tag = self._image
        )
    except:
        print("fail.")
    else:
        print("done.")
