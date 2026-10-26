from fastmcp import FastMCP
import sqlite3
import os
DB_PATH=os.path.join(os.path.dirname(__file__),"notes.db")
connection=sqlite3.connect(DB_PATH,check_same_thread=False)



mcp=FastMCP(name="notes server")
def init_db():
    try:
        connection.execute("CREATE TABLE notes (title TEXT, description TEXT)")
    except sqlite3.OperationalError:
        pass  # Table already exists

init_db()

@mcp.tool()
def add_notes(title:str,description:str):
    """
    add a new note with title and description
    """

    try:
        query="INSERT INTO notes (title,description) VALUES (?,?)"
        connection.execute(query,(title,description))
        connection.commit()
        return "note added successfully"
    except Exception as e:
        return f"Error adding note: {e}"
    

@mcp.tool()
def list_notes():
    """
    list all notes with title and description
    """

    try:
        query="SELECT id, title, description FROM notes"
        cursor=connection.execute(query)
        notes=cursor.fetchall()
        return notes
    except Exception as e:
        return f"Error listing notes: {e}"
    
@mcp.tool()
def DELETE_notes(id:str):
    """
    delete a note by id
    """

    try:
        query="DELETE FROM notes WHERE id = ?"
        connection.execute(query, (id,))
        connection.commit()
        return "note deleted successfully"
    except Exception as e:
        return f"Error deleting note: {e}"


if __name__=="__main__":
    init_db()
    mcp.run()