import pyodbc

DRIVER_NAME = 'SQL SERVER'
SERVER = input('Enter Server Name')
DATABASE = input('Enter Database Name')
USERNAME = input('Enter Username')
PASSWORD = input('Enter Password')

connectionString = f'DRIVER={DRIVER_NAME};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

try:
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    print(f'Connected, Server Name: {SERVER}, Database: {DATABASE}') 
except:
    print('Connection Failed!')
