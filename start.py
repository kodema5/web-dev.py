
from sidecar import sidecar
from serve import serve
from test2 import test2
import os
import sys
import multiprocessing as mp

def start(
    file,
    pattern = None,   # pattern of test-names, ex: "first"
    docker_name = "web-dev",
    user = "web",
    database = "web",
    local = "t",
    cwd = os.getcwd(),
    watch = True,

    # serve
    #
    port=8000,   # port listens to
    debug=True, # displays the pg-calls
    reload=False, # force reload deno code cache
    pgfunc="web.{schema}_{func}", # pg function signature

    # sidecar
    #
    sidelib=None # library to be loaded
):
    """start test with --watch and serve --debug"""

    mp.set_start_method('spawn')
    q = mp.Queue()
    p1 = mp.Process(
        target = test2,
        args = (file, pattern, docker_name, user, database, local, cwd, watch)
    )

    p2 = mp.Process(
        target=serve,
        args=(port, debug, reload, pgfunc,),
    )

    p3 = mp.Process(
        target=sidecar,
        args=(sidelib, debug, reload),
    )

    try:
        p1.start()
        p2.start()
        p3.start()
        q.get()
    except KeyboardInterrupt:
        p1.terminate()
        p2.terminate()
        p3.terminate()
        print("\nterminated.")

