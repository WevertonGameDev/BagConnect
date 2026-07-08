class AuthService:



    def login(
        self,
        email,
        password
    ):


        if email and password:

            return True


        return False



    def register(
        self,
        name,
        email,
        password
    ):


        """
        Futuramente:

        Firebase Authentication
        Firestore users collection

        """


        if name and email and password:

            return True


        return False