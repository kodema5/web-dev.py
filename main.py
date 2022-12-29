import fire
import docker_build
import docker_start
import docker_stop
import serve
import test2
import start

if __name__ == '__main__':
    fire.Fire({
        'docker-build': docker_build.build,
        'docker-start': docker_start.start,
        'docker-stop': docker_stop.stop,
        'start': start.start,
        'serve': serve.serve,
        'test': test2.test2,
    })

# using pipenv
# > pip install pipenv
# > cat web-dev
# #!/bin/sh
#
# # change ?? below to folder
# (cd /??/web-dev.py && pipenv run python main.py $*)
