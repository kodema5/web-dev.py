import test
import watch as watch_lib
import os

def test2 (
    file,
    pattern = None,   # pattern of test-names, ex: "first"
    docker_name = "web-dev",
    user = "web",
    database = "web",
    drop = "f",
    dev = "f",
    cwd = os.getcwd(),
    watch = False,
):
    if watch is True:
        watch_lib.watch(
            file,
            pattern,
            docker_name,
            user,
            database,
            drop,
            dev,
            cwd
        )
    else:
        test.test (
            file,
            pattern,
            docker_name,
            user,
            database,
            drop,
            dev
        )

