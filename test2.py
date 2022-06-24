import test
import watch as watch_lib
import os

def test2 (
    file,
    pattern = None,   # pattern of test-names, ex: "first"
    docker_name = "web-dev",
    user = "web",
    database = "web",
    local = "t",
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
            local,
            cwd
        )
    else:
        test.test (
            file,
            pattern,
            docker_name,
            user,
            database,
            local
        )

