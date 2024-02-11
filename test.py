# test a file

import os
#import docker
import subprocess

def test (
    file,
    pattern = None,   # pattern of test-names, ex: "first"
    docker_name = "web-dev",
    user = "web",
    database = "web",
    drop = "f",
    dev = "f",
):
    """run test.sql over .sql file"""
    print(f"testing {file} in {docker_name}")
    subprocess.run([
        'docker', 'exec', 'web-dev',
        'psql',
        '-U', user, '-d', database,
        '-f', '/test.sql',
        '-v', f"test_file=/work/{file}",
        '-v', f"drop={drop}",
        '-v', f"dev={dev}",
        '--quiet',
        '--tuples-only',
        f'-v' if pattern is not None else '',
        f"test_pattern={pattern}" if pattern is not None else '',

    ])

    # 9/26 failed after docker-desktop upgrade
    # d = docker.from_env()
    # try:
    #     c = d.containers.get(docker_name)
    #     a = c.exec_run(cmd=' '.join([
    #         'psql',
    #         f" -U {user}",
    #         f" -d {database}",
    #         '-f /test.sql',
    #         f"-v test_file=/work/{file}",
    #         f" -v drop={drop}",
    #         ' --quiet ',
    #         ' --tuples-only ',
    #         f"-v test_pattern={pattern}" if pattern is not None else ''
    #     ])
    #     )
    #     print(a.output.decode("utf-8"))

    # except docker.errors.APIError as e:
    #     print(f"Error: {str(e)}")
