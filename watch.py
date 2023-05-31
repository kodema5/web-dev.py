import os
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from test import test

class Handler(FileSystemEventHandler):
    last_ = ''

    def __init__(
            self,
            file,
            pattern,
            docker_name,
            user,
            database,
            drop,
    ):
        self._file = file
        self._pattern = pattern
        self._docker_name = docker_name
        self._user = user
        self._database = database
        self._drop = drop

    def on_any_event(self, event):
        if event.is_directory:
            return None

        _, ext = os.path.splitext(event.src_path)
        if ext != '.sql':
            return None

        ts = '-'
        if os.path.exists(event.src_path):
            ts = datetime.utcfromtimestamp(
                os.path.getmtime(event.src_path)
            ).strftime('%Y-%m-%d %H:%M:%S')

        s = f"\nfound {event.event_type} {event.src_path} ({ts})"
        if s == self.last_:
            return None

        self.last_ = s
        print(s)

        self.run_test()

    def run_test(self):
        test(
            file = self._file,
            pattern = self._pattern,
            docker_name = self._docker_name,
            user = self._user,
            database = self._database,
            drop = self._drop
        )

def watch (
    file,
    pattern = None,   # pattern of test-names, ex: "first"
    docker_name = "web-dev",
    user = "web",
    database = "web",
    drop = "f",
    cwd = os.getcwd(),
):
    """watching files for testing"""
    print(f"watching files in {cwd}"
        "\npress ^C to exit"
    )

    handler = Handler(
        file,
        pattern,
        docker_name,
        user,
        database,
        drop
    )
    handler.run_test() # run first test

    obsv = Observer()
    obsv.schedule(
        handler,
        cwd,
        recursive=True
    )
    obsv.start()

    try:
        while obsv.is_alive():
            obsv.join(1)
    except:
        obsv.stop()

