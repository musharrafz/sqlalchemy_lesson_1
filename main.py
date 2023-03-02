from sqlalchemy.orm import Session
import models
from config import engine, session


def main(db: Session):

    categories = db.query(models.Actor).limit(1)
    for i in categories:
        print(i)

    categories = db.query(models.Film).limit(1)
    for i in categories:
        print(i)

    categories = db.query(models.Category).limit(1)
    for i in categories:
        print(i)

    categories = db.query(models.FilmCategory).limit(1)
    for i in categories:
        print(i)

    categories = db.query(models.FilmActor).limit(1)
    for i in categories:
        print(i)

    categories = db.query(models.City).limit(1)
    for i in categories:
        print(i)

    categories = db.query(models.Country).limit(1)
    for i in categories:
        print(i)

    categories = db.query(models.Customer).limit(1)
    for i in categories:
        print(i)

    categories = db.query(models.Inventory).limit(1)
    for i in categories:
        print(i)

    categories = db.query(models.Language).limit(1)
    for i in categories:
        print(i)

    categories = db.query(models.Payment).limit(1)
    for i in categories:
        print(i)

    categories = db.query(models.Address).limit(1)
    for i in categories:
        print(i)

    categories = db.query(models.Rental).limit(1)
    for i in categories:
        print(i)

    categories = db.query(models.Staff).limit(1)
    for i in categories:
        print(i)

    categories = db.query(models.Store).limit(1)
    for i in categories:
        print(i)


if __name__ == "__main__":
    # models.Base.metadata.drop_all(engine)
    # models.Base.metadata.create_all(engine)
    main(session)
