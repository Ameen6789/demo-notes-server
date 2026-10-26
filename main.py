# from fastmcp import FastMCP
# import sqlite3

# import os
# # DB_PATH=os.path.join(os.path.dirname(__file__),"notes.db")
# DB_PATH = os.environ.get("NOTES_DB_PATH", "/tmp/notes.db")
# connection=sqlite3.connect(DB_PATH,check_same_thread=False)



# mcp=FastMCP(name="notes server")
# def init_db():
#     connection.execute(
#         """CREATE TABLE IF NOT EXISTS notes (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT,
#             description TEXT
#         )"""
#     )
#     connection.commit()

# init_db()

# @mcp.tool()
# def add_notes(title:str,description:str):
#     """
#     add a new note with title and description
#     """

#     try:
#         query="INSERT INTO notes (title,description) VALUES (?,?)"
#         connection.execute(query,(title,description))
#         connection.commit()
#         return "note added successfully"
#     except Exception as e:
#         return f"Error adding note: {e}"
    

# @mcp.tool()
# def list_notes():
#     """
#     list all notes with title and description
#     """

#     try:
#         query="SELECT id, title, description FROM notes"
#         cursor=connection.execute(query)
#         notes=cursor.fetchall()
#         return notes
#     except Exception as e:
#         return f"Error listing notes: {e}"
    
# @mcp.tool()
# def DELETE_notes(id:str):
#     """
#     delete a note by id
#     """

#     try:
#         query="DELETE FROM notes WHERE id = ?"
#         connection.execute(query, (id,))
#         connection.commit()
#         return "note deleted successfully"
#     except Exception as e:
#         return f"Error deleting note: {e}"


# if __name__=="__main__":
#     mcp.run()




from fastmcp import FastMCP
import aiosqlite

import os
# DB_PATH=os.path.join(os.path.dirname(__file__),"notes.db")
DB_PATH = os.environ.get("NOTES_DB_PATH", "/tmp/notes.db")

connection = aiosqlite.connect(DB_PATH, check_same_thread=False)



mcp=FastMCP(name="notes server")
def init_db():
    connection.execute(
        """CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT
        )"""
    )
    connection.commit()

init_db()

@mcp.tool()
async def add_notes(title:str,description:str):
    """
    add a new note with title and description
    """

    try:
        query="INSERT INTO notes (title,description) VALUES (?,?)"
        await connection.execute(query,(title,description))
        await connection.commit()
        return "note added successfully"
    except Exception as e:
        return f"Error adding note: {e}"
    

@mcp.tool()
async def list_notes():
    """
    list all notes with title and description
    """

    try:
        query="SELECT id, title, description FROM notes"
        cursor=await connection.execute(query)
        notes=await cursor.fetchall()
        return notes
    except Exception as e:
        return f"Error listing notes: {e}"
    
@mcp.tool()
async def DELETE_notes(id:str):
    """
    delete a note by id
    """

    try:
        query="DELETE FROM notes WHERE id = ?"
        await connection.execute(query, (id,))
        await connection.commit()
        return "note deleted successfully"
    except Exception as e:
        return f"Error deleting note: {e}"


if __name__=="__main__":
    mcp.run()