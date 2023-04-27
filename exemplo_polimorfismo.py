class Argentina:
    def capital(self):
        print("Buenos Aires e a capital da Argentina.")
    def kingua_oficial(self):
        print("O espanhol e a linha oficial da Argentina.")


class Brasil():
    def capital(self):
        print("Brasilia e a capital do Brasil.")

    def lingua_oficial(self):
        print("O portugues e a lingua oficial do Brasil")

obj_arg = Argentina()
obj_bra = Brasil
for pais in (obj_arg, obj_bra):
    pais.capital()
    pais.lingua_oficial()