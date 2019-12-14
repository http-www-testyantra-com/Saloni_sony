from configparser import ConfigParser,ExtendedInterpolation

c = ConfigParser(interpolation=ExtendedInterpolation())

c.read("C:\\Users\\Saloni\\PycharmProjects\\Sample.ini")
print(c.sections())
print(c.get("settings","secret_key"))
print(c.options("settings"))
print("DB" in c)
print(c.get("DB","db_port"))
print(c.getint("DB","db_port",fallback=8080))
print(c.getboolean("settings","debug"))