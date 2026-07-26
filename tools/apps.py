import subprocess


def open_app(app_name):
    try:
        subprocess.Popen([app_name])
        return f"Opening {app_name}..."
    except FileNotFoundError:
        return f"Couldn't find '{app_name}'. Is it installed?"
    except Exception as e:
        return f"Error: {e}"