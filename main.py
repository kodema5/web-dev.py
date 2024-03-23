import fire
import docker_build
import docker_start
import docker_stop
import serve
import sidecar
import test2
import start

if __name__ == '__main__':
    fire.Fire({
        'docker-build': docker_build.build,
        'docker-start': docker_start.start,
        'docker-stop': docker_stop.stop,
        'start': start.start,
        'sidecar': sidecar.sidecar,
        'serve': serve.serve,
        'test': test2.test2,
    })

# using pipenv (python3 -m pipenv)
# > pip install pipenv
# > git clone https://github.com/kodema5/web-dev.py
# > cd web-dev.py
# > pipenv install
# > source web-dev