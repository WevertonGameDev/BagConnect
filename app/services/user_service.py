from models.user import User
from services.database import Database


class UserService:

    def editar_usuario(
        self,
        id_usuario,
        usuario,
        email,
        cpf
    ):
        db = Database()

        try:

            # Verifica se o usuário já existe
            db.cursor.execute(
                """
                SELECT id
                FROM usuarios
                WHERE usuario = ?
                AND id <> ?
                """,
                (
                    usuario,
                    id_usuario
                )
            )

            if db.cursor.fetchone():
                return False, "usuario"

            # Verifica se o email já existe
            db.cursor.execute(
                """
                SELECT id
                FROM usuarios
                WHERE email = ?
                AND id <> ?
                """,
                (
                    email,
                    id_usuario
                )
            )

            if db.cursor.fetchone():
                return False, "email"

            # Verifica se o CPF já existe (caso tenha sido informado)
            if cpf.strip():

                db.cursor.execute(
                    """
                    SELECT id
                    FROM usuarios
                    WHERE cpf = ?
                    AND id <> ?
                    """,
                    (
                        cpf,
                        id_usuario
                    )
                )

                if db.cursor.fetchone():
                    return False, "cpf"

            # Atualiza os dados
            db.cursor.execute(
                """
                UPDATE usuarios

                SET
                    usuario = ?,
                    email = ?,
                    cpf = ?

                WHERE id = ?
                """,
                (
                    usuario,
                    email,
                    cpf if cpf.strip() else None,
                    id_usuario
                )
            )

            db.connection.commit()

            usuario_atual = db.cursor.execute(
                """
                SELECT *
                FROM usuarios
                WHERE id = ?
                """,
                (id_usuario,)
            ).fetchone()

            return True, User(
                id=usuario_atual[0],
                usuario=usuario_atual[1],
                email=usuario_atual[2],
                senha=usuario_atual[3],
                cpf=usuario_atual[4],
                passageiro_id=usuario_atual[5]
            )

        except Exception as erro:
            print("Erro ao editar usuário:", erro)
            return False, None

        finally:
            db.fechar()