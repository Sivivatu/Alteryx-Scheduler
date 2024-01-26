from typing import Optional

# One line of FastAPI imports here later 👈
from sqlmodel import Field, SQLModel, Session, create_engine, select


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


sqlite_file_name = "database/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Code above omitted 👆

def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    
    print("Before interacting with the database")
    print("Hero 1:", hero_1)
    print("Hero 2:", hero_2)
    print("Hero 3:", hero_3)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)

        session.commit()

def select_heroes():
    with Session(engine) as session:
        statement = select(Hero)
        heros = session.exec(statement).all()
        print(heros)

def main():
    create_db_and_tables()
    create_heroes()
    select_heroes()

# More code here later 👇

if __name__ == "__main__":
    main()