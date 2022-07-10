import sqlite3

connection = sqlite3.connect('cmdb.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Servers
             (Servername TEXT, Ipaddr TEXT, Uptime TEXT)''')
cursor.execute('''INSERT INTO SERVERS(Servername, Ipaddr, Uptime) VALUES ("atlas","192.168.1.185","30 days")''')
connection.commit()
connection.close() 
