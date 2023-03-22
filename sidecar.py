import subprocess

def sidecar (
    sidelib=None, # side-libraries
    debug=False, # to-do
    reload=False # force reload deno code cache
):
    """launches pg_sidecar.js pg-listener"""

    cmd = [
        'deno', 'run',
        '--allow-net', '--allow-read', '--allow-env', '--unstable', '--allow-sys',
        '--reload' if reload else '',
        # '../pg_sidecar.js/mod.js',
        'https://raw.githubusercontent.com/kodema5/pg_sidecar.js/main/mod.js',
        '--debug=true' if debug else '',
        '-l' if sidelib is not None else '',
        f"{sidelib}" if sidelib is not None else '',
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

