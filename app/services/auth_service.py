from models.user import User
from services.database import Database


class AuthService:


    def register(self, usuario, email, senha):
        db = Database()

        try:
            db.cursor.execute(
                """
                INSERT INTO usuarios
                (
                    usuario,
                    email,
                    senha
                )

                VALUES (?, ?, ?)

                """,
                (
                    usuario,
                    email,
                    senha
                )
            )

            db.connection.commit()
            return True


        except Exception as erro:
            print("Erro ao cadastrar:", erro)
            return False

        finally:
            db.fechar()


    def login(self, email, senha):
        db = Database()

        try:
            db.cursor.execute(
                """
                SELECT *
                FROM usuarios
                WHERE email = ?
                AND senha = ?
                """,
                (
                    email,
                    senha
                )
            )

            usuario = db.cursor.fetchone()

            if usuario:
                return User(
                            id=usuario[0],
                            usuario=usuario[1],
                            email=usuario[2],
                            senha=usuario[3],
                            cpf=usuario[4],
                            passageiro_id=usuario[5]
                        )

            return None

        except Exception as erro:
            print("Erro no login:", erro)
            return None

        finally:
            db.fechar()