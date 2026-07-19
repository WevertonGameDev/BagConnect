import platform
import subprocess
import locale


class System:

    @staticmethod
    def detectar_tema():
        """
        Retorna:
            "Dark"
            "Light"

        Caso não consiga detectar, retorna Light.
        """

        sistema = platform.system()

        try:
            # WINDOWS
            if sistema == "Windows":

                import winreg

                chave = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER,
                    r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize",
                )

                valor, _ = winreg.QueryValueEx(
                    chave,
                    "AppsUseLightTheme"
                )

                return "Light" if valor else "Dark"

            # macOS
            elif sistema == "Darwin":

                resultado = subprocess.check_output(
                    [
                        "defaults",
                        "read",
                        "-g",
                        "AppleInterfaceStyle",
                    ],
                    stderr=subprocess.DEVNULL,
                ).decode().strip()

                return "Dark" if resultado == "Dark" else "Light"

            # Linux
            elif sistema == "Linux":

                try:
                    resultado = subprocess.check_output(
                        [
                            "gsettings",
                            "get",
                            "org.gnome.desktop.interface",
                            "color-scheme",
                        ]
                    ).decode().lower()

                    if "dark" in resultado:
                        return "Dark"

                except Exception:
                    pass

                return "Light"

        except Exception:
            pass

        return "Light"

    @staticmethod
    def detectar_idioma():
        try:

            codigo = locale.getdefaultlocale()[0] or ""

            codigo = codigo.lower()

            if codigo.startswith("pt"):
                return "pt"

            if codigo.startswith("en"):
                return "en"

        except Exception:
            pass

        return "en"