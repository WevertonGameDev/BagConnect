class DatabaseService:


    def login(
        self,
        email,
        password
    ):

        """
        Futuramente:
        Firebase Authentication
        """

        if email and password:

            return {

                "success": True,
                "message": "Login realizado"

            }


        return {

            "success": False,
            "message": "Dados inválidos"

        }