from services.database import Database


class BagService:

    @staticmethod
    def buscar_bagagem(cpf: str, codigo: str):

        db = Database()

        try:

            db.cursor.execute("""
                SELECT
                    b.codigo,
                    b.status
                FROM bagagens b
                INNER JOIN passageiros p
                    ON p.id = b.passageiro_id
                WHERE
                    p.cpf = ?
                AND
                    b.codigo = ?
            """, (cpf, codigo))

            resultado = db.cursor.fetchone()

            if resultado is None:
                return None

            return {
                "codigo": resultado[0],
                "status": resultado[1]
            }

        finally:
            db.fechar()