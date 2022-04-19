import fire
from build import build
from serve import serve
from start import start
from stop import stop
from test import test
from watch import watch

if __name__ == '__main__':
    fire.Fire({
        'build': build,
        'serve': serve,
        'start': start,
        'stop': stop,
        'test': test,
        'watch': watch,
    })

