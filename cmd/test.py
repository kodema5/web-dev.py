# test a file

import os
import docker

def test (
    file,
    pattern = None,   # pattern of test-names, ex: "first"
    docker_name = "web-dev",
    user = "web",
    database = "web",
):
    """run test.sql over .sql file"""
    print(f"testing {file} in {docker_name}")
    d = docker.from_env()
    try:
        c = d.containers.get(docker_name)
        a = c.exec_run(cmd=' '.join([
            'psql',
            f" -U {user}",
            f" -d {database}",
            '-f /test.sql',
            f"-v test_file=/work/{file}",
            ' --set local=t',
            ' --quiet ',
            ' --tuples-only ',
            ' -v local=t ',
            f"-v test_pattern={pattern}" if pattern is not None else ''
        ])
        )
        print(a.output.decode("utf-8"))

    except docker.errors.APIError as e:
        print(f"Error: {str(e)}")
