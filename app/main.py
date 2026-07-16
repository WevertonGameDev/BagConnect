from core.app import BagConnectApp
from services.database import Database

if __name__ == "__main__":

    db = Database()
    db.criar_tabelas()
    db.fechar()

    BagConnectApp().run()