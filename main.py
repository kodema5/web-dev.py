import fire
from build import build
from serve import serve
from start import start
from stop import stop
from test2 import test2
from watch import watch

if __name__ == '__main__':
    fire.Fire({
        'docker-build': build,
        'docker-start': start,
        'docker-stop': stop,
        'serve': serve,
        'test': test2,
    })

