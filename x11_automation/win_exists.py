from ewmh import EWMH
import subprocess
import re


def win_exists(win_name):
    if get_win_by_name(win_name):
        return True


def get_win_by_name(win_name):
    ewmh = EWMH()

    # get every displayed windows
    wins = ewmh.getClientList()

    active = ewmh.getActiveWindow()
    print(f'{active}')

    for win in wins:
        name = win.get_wm_name()
        wm_id = win.id
        if not name:
            name = get_window_name(wm_id)

        if name == win_name:
            return {'name': name, 'win': win}
    return False


def get_window_name(win_id):
    p = subprocess.run(f'xprop -id {win_id}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = p.stdout.decode('utf-8')

    for line in out.splitlines():
        if match := re.match(r'WM_NAME\(.+\) = "(.+)"', line):
            return match.group(1)