# coding=UTF-8
# This Python file uses the following encoding: utf-8

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from main import app
from models import *
from views import *

# 設定你的 app
manager = Manager(app)
# 設定 python manage.py db 來管理 models
manager.add_command('db', MigrateCommand)
# 設定 python manage.py runserver 為啟動 server 指令
manager.add_command('runserver', Server())


if __name__ == '__main__':
    manager.run()
