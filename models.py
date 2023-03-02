from sqlalchemy import Integer, String, Column, ForeignKey, TIMESTAMP, func, Text, Boolean, SmallInteger, DateTime, \
    Numeric, \
    Enum, true
from sqlalchemy.orm import relationship
from config import Base


class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    last_update = Column('last_update', DateTime(timezone=False), nullable=False, server_default=func.now())

    def __repr__(self):
        return f'{self.category_id} {self.name} {self.last_update}'


class FilmCategory(Base):
    __tablename__ = 'film_category'
    film_id = Column('film_id', SmallInteger, ForeignKey('film.film_id'), primary_key=True)
    category_id = Column('category_id', SmallInteger, ForeignKey('category.category_id'), primary_key=True)
    last_update = Column('last_update', DateTime(timezone=False), nullable=False, server_default=func.now())

    def __repr__(self):
        return f'{self.film_id} {self.category_id} {self.last_update}'


class Film(Base):
    __tablename__ = 'film'
    film_id = Column(Integer, primary_key=True)
    title = Column(String(25), nullable=False)
    description = Column(Text)
    release_year = Column(Integer)
    rental_duration = Column(SmallInteger, nullable=False, default=3)
    rental_rate = Column(Numeric(4, 2), nullable=False, default=4.99)
    length = Column(SmallInteger)
    replacement_cost = Column(Numeric(5, 2), nullable=False, default=19.99)
    rating = Column(String(5), nullable=False, default='G')
    last_update = Column('last_update', DateTime(timezone=False), nullable=False, server_default=func.now())
    special_features = Column(Text)
    fulltext = Column(Text, nullable=False)

    def __repr__(self):
        return f'{self.film_id} {self.title} {self.description} '


class FilmActor(Base):
    __tablename__ = 'film_actor'
    actor_id = Column('actor_id', SmallInteger, ForeignKey('actor.actor_id'), primary_key=True)
    film_id = Column('film_id', SmallInteger, ForeignKey('film.film_id'), primary_key=True)
    last_update = Column('last_update', DateTime(timezone=False), nullable=False, server_default=func.now())

    def __repr__(self):
        return f'{self.actor_id} {self.film_id} {self.last_update}'


class Actor(Base):
    __tablename__ = 'actor'
    actor_id = Column('actor_id', Integer, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    last_update = Column('last_update', DateTime(timezone=False), nullable=False, server_default=func.now())

    def __repr__(self):
        return f'{self.actor_id} {self.first_name} {self.last_name} {self.last_update}'


class Address(Base):
    __tablename__ = 'address'
    address_id = Column('address_id', Integer, primary_key=True)
    address = Column(String(50), nullable=False)
    address2 = Column(String(50), nullable=False)
    district = Column(String(20), nullable=False)
    city_id = Column("city_id", SmallInteger, ForeignKey("city.city_id"), primary_key=True)
    postal_code = Column(String(10), nullable=False)
    phone = Column(String(20), nullable=False)
    last_update = Column('last_update', DateTime(timezone=False), nullable=False, server_default=func.now())

    def __repr__(self):
        return f"{self.address_id} {self.address} {self.address2} {self.phone}"


class City(Base):
    __tablename__ = 'city'
    city_id = Column('city_id', Integer, primary_key=True)
    city = Column(String(50), nullable=False)
    country_id = Column("country_id", SmallInteger, ForeignKey("country.country_id"), primary_key=True)
    last_update = Column('last_update', DateTime(timezone=False), nullable=False, server_default=func.now())

    def __repr__(self):
        return f"{self.city_id} {self.city} {self.country_id}"


class Country(Base):
    __tablename__ = 'country'
    country_id = Column('country_id', SmallInteger, primary_key=True)
    country = Column(String(50), nullable=False)
    last_update = Column('last_update', DateTime(timezone=False), nullable=False, server_default=func.now())

    def __repr__(self):
        return f"{self.country_id} {self.country} {self.last_update}"


class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column('customer_id', Integer, primary_key=True)
    store_id = Column('store_id', SmallInteger, ForeignKey('store.store_id'), primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(50), nullable=False)
    address_id = Column('address_id', SmallInteger, ForeignKey('address.address_id'), primary_key=True)
    activebool = Column(Boolean, default='true', nullable=False)
    create_date = Column(DateTime(timezone=False), nullable=False, )
    last_update = Column('last_update', DateTime(timezone=False), nullable=False, server_default=func.now())
    active = Column(Integer)

    def __repr__(self):
        return f'{self.customer_id} {self.email} {self.first_name} {self.last_name}'


class Inventory(Base):
    __tablename__ = 'inventory'
    inventory_id = Column('inventory_id', Integer, primary_key=True)
    film_id = Column('film_id', SmallInteger, ForeignKey('film.film_id'), primary_key=True)
    store_id = Column('store_id', SmallInteger, ForeignKey('store.store_id'), primary_key=True)
    last_update = Column('last_update', DateTime(timezone=False), nullable=False, server_default=func.now())

    def __repr__(self):
        return f'{self.inventory_id} {self.film_id} {self.store_id} {self.last_update}'


class Language(Base):
    __tablename__ = 'language'
    language_id = Column('language_id', Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    last_update = Column('last_update', DateTime(timezone=False), nullable=False, server_default=func.now())

    def __repr__(self):
        return f'{self.language_id} {self.name} {self.last_update}'


class Payment(Base):
    __tablename__ = 'payment'
    payment_id = Column('payment_id', Integer, primary_key=True)
    customer_id = Column('customer_id', SmallInteger, ForeignKey('customer.customer_id'), primary_key=True)
    staff_id = Column('staff_id', SmallInteger, ForeignKey('staff.staff_id'), primary_key=True)
    rental_id = Column('rental_id', SmallInteger, ForeignKey('rental.rental_id'), primary_key=True)
    amount = Column(Numeric(5, 2), nullable=False)
    payment_date = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return f'{self.payment_id} {self.customer_id} {self.staff_id} {self.rental_id} {self.amount}'


class Rental(Base):
    __tablename__ = 'rental'
    rental_id = Column('rental_id', Integer, primary_key=True)
    rental_date = Column(TIMESTAMP, nullable=False)
    inventory_id = Column('inventory_id', SmallInteger, ForeignKey('inventory.inventory_id'), primary_key=True)
    customer_id = Column('customer_id', SmallInteger, ForeignKey('customer.customer_id'), primary_key=True)
    return_date = Column(TIMESTAMP, nullable=False)
    staff_id = Column('staff_id', SmallInteger, ForeignKey('staff.staff_id'), primary_key=True)
    last_update = Column('last_update', DateTime(timezone=False), nullable=False, server_default=func.now())

    def __repr__(self):
        return f'{self.rental_id} {self.rental_date} {self.inventory_id} {self.customer_id}'


class Staff(Base):
    __tablename__ = 'staff'
    staff_id = Column('staff_id', Integer, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    address_id = Column('address_id', SmallInteger, ForeignKey('address.address_id'), primary_key=True)
    email = Column(String(50))
    store_id = Column('store_id', SmallInteger, ForeignKey('store.store_id'), primary_key=True)
    active = Column(Boolean, nullable=False, default=True)
    username = Column(String(16), nullable=False)
    password = Column(String(16), nullable=False)
    last_update = Column('last_update', DateTime(timezone=False), nullable=False, server_default=func.now())

    def __repr__(self):
        return f'{self.staff_id} {self.first_name} {self.last_name} {self.username} {self.password}'


class Store(Base):
    __tablename__ = 'store'
    store_id = Column('store_id', Integer, primary_key=True, nullable=False)
    manager_staff_id = Column(SmallInteger, ForeignKey('staff.staff_id'), primary_key=True)
    address_id = Column('address_id', SmallInteger, ForeignKey('address.address_id'), primary_key=True)
    last_update = Column('last_update', DateTime(timezone=False), nullable=False, server_default=func.now())

    def __repr__(self):
        return f'{self.store_id} {self.manager_staff_id} {self.address_id} {self.last_update}'
