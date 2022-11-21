import mysql.connector
from rich import print as printc
from rich.console import Console
console = Console()

# for Loading env variables
import os
from dotenv import load_dotenv
load_dotenv()

  
def dbconfig():
  try:
    db = mysql.connector.connect(
      host =os.getenv("HOST"),
      user =os.getenv("USER"),
      passwd =os.getenv("PASSWD")
    )
    # printc("[green][+][/green] Connected to db")  
  except Exception as e:
    print("[red][!] An error occurred while trying to connect to the database[/red]")
    console.print_exception(show_locals=True)

  return db


