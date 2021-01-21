"""run.py file """
from src import app
from src.models import Models

mod = Models()

mod.load_data()

if __name__ == '__main__':
    app.run(debug=True)
