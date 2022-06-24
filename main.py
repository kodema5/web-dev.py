import fire
from docker_build import build
from docker_start import start
from docker_stop import stop
from serve import serve
from test2 import test2
from start import start

if __name__ == '__main__':
    fire.Fire({
        'docker-build': build,
        'docker-start': start,
        'docker-stop': stop,
        'start': start,
        'serve': serve,
        'test': test2,
    })

