import subprocess

def serve (
    port=8000,   # port listens to
    debug=False, # displays the pg-calls
    reload=False # force reload
):
    """launches web-dev.js http-server"""

    cmd = [
        'deno', 'run',
        '--allow-net', '--allow-read', '--allow-env', '--unstable',
        '--reload' if reload else '',
        'https://raw.githubusercontent.com/kodema5/web-dev.js/main/mod.js',
        f"--port={port}",
        '--debug=true' if debug else ''
    ]
    cmd = [a for a in cmd if a != '']

    try:
        p = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        for l in iter(p.stdout.readline, ""):
            print(l, end='')
        p.stdout.close()
    except:
        pass

