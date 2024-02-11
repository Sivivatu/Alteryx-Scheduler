import asyncio
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.sql import text

load_dotenv()


# # Replace these variables with your connection details
# host = f"{os.getenv('DB_HOST')}"
# port = f"{os.getenv('DB_PORT')}"
# user = f"{os.getenv('DB_USER')}"
# password = f"{os.getenv('DB_PASSWORD')}"
# dbname = f"{os.getenv('DB_NAME')}"

# Access the database URL from the environment variable
database_url: str= f"postgresql+psycopg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
async_database_url: str= f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

print(database_url)
# Create an engine
engine = create_engine(database_url)

# # Connect to the database
# with engine.connect() as connection:
#     # Execute raw SQL command to get the list of databases
#     result = connection.execute(text("SELECT datname FROM pg_database WHERE datistemplate = false;"))

#     print(result.fetchall())

#     # # Print the list of databases
#     # print("Databases:")
#     # for row in result:
#     #     print(row['datname'])

# Create an asynchronous engine
async_engine = create_async_engine(async_database_url)

async def list_databases():
    async with async_engine.connect() as connection:
        # Execute raw SQL command to get the list of databases asynchronously
        result = await connection.execute(text("SELECT datname FROM pg_database WHERE datistemplate = false;"))
        databases = result.fetchall()

        print(databases)

        # # Print the list of databases
        # print("Databases:")
        # for db in databases:
        #     print(db['datname'])

# Run the async function
asyncio.run(list_databases())