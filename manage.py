from  flask_script import Manager,Server,Shell
from app import create_app
from configs.default import DefaultConfig

from models import db
app=create_app(DefaultConfig) #利用这个配置创建app

manager=Manager(app)

def _make_context():
    from models.cinema import Cinema
    from models.hall import Hall
    locals().update(globals())  #局部变量添加全局变量
    return dict(**locals())



manager.add_command('runserver',Server('127.0.0.1',port=5000))
manager.add_command('shell',Shell(make_context=_make_context))


@manager.command
def createdb():
    from models.cinema import Cinema
    from models.hall import Hall
    db.create_all()

if __name__=='__main__':
    manager.run()