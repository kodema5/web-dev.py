import fire
from cmd.build import build
from cmd.start import start
from cmd.stop import stop
from cmd.test import test
from cmd.watch import watch

if __name__ == '__main__':
    fire.Fire({
        'build': build,
        'start': start,
        'stop': stop,
        'test': test,
        'watch': watch,
    })

