from flask_script import Manager, Shell

from app import create_app
from app.models.database import recreate
from app.models import User, Article

from generate_data import GenerateData

app = create_app('development')
manager = Manager(app)



def make_shell_context():
    return dict(recreate=recreate,
                userv=User(),
                aserv=Article(),
                gus = GenerateData().generate_users,
                gas = GenerateData().generate_articles,
                gcs = GenerateData().generate_comments)

manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
