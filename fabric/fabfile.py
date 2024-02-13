from fabric.api import *


#@hosts('ubuntu@16.171.63.3')

def do():
    sudo("systemctl status mcc")
    sudo("systemctl status basecamp")
