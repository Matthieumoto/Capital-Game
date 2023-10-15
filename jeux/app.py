from flask import Flask, render_template
from settings import *

class App:

    """Classe qui permet d'ouvrir un serveur web en local pour afficher les scores"""

    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route('/')
        def index():
            return render_template('index.html')

    def run(self):
        if __name__ == '__main__':
            self.app.run()

if __name__ == '__main__':
    mon_application = App()
    mon_application.run()
