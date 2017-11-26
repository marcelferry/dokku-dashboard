import subprocess
import os

from dokku_dashboard.dokku_cmds import Dokku


def get_list_apps_command():
    apps = Dokku().apps
    apps.parent_cmd.quiet()
    return str(apps)


def filter_apps(app):
    app_name = os.environ.get('APP_NAME', 'dokku-dashboard')
    return app and app != app_name


def format_stdout(stdout):
    decoded = stdout.decode('utf-8')
    apps = map(str.strip, decoded.split('\n'))
    return list(filter(filter_apps, apps))


def list_apps():
    cmd = get_list_apps_command()
    result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    return format_stdout(result.stdout)
