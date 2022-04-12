import sys
import os
import docker

def start (
    name = "web-dev",
    user = "web",
    password = "rei",
    database = "web",
    port = 5432
):
    """starts docker image"""
    print(f"starting {name} container")

    cwd = os.getcwd()
    d = docker.from_env()
    try:
        d.containers.run(
            name,
            ' '.join([
                "-c shared_preload_libraries=pg_cron",
                f"-c cron.database={database}"
            ]),
            name = name,
            auto_remove = True,
            detach = True,
            ports = {
                '5432/tcp': port
            },
            environment = [
                f"POSTGRES_USER={user}",
                f"POSTGRES_PASSWORD={password}",
                f"POSTGRES_DB={database}",
            ],
            volumes = [
                f"{cwd}/.data/{name}:/var/lib/postgresql/data",
                f"{cwd}:/work"
            ]
        )
    except docker.errors.APIError as e:
        print(f"Error: {str(e)}")

