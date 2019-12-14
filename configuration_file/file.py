from configparser import ConfigParser

c = ConfigParser()
c["settings"] = {'debug':"true",
                 'secret_key':"9797",
                 'log_path':"C:\\Users\\Saloni\\PycharmProjects"}

c["DB"] = {'db_name':"sql",
           'db_type':"rdbms",
           'db_port':"8888"}

with open("C:\\Users\\Saloni\\PycharmProjects\\Sample.ini","w") as f:
    c.write(f)
    f.close()
    