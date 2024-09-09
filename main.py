import contextlib
import os

import logging

from sqlalchemy import BigInteger
from sqlalchemy import create_engine, text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import DeclarativeBase, mapped_column, WriteOnlyMapped
from sqlalchemy.orm import selectinload



engine = create_engine(
    url="postgresql+psycopg://postgres@db/development",
    isolation_level="AUTOCOMMIT",
    connect_args={"prepare_threshold": None},
    echo=True
)

SessionLocal = sessionmaker(
    autoflush=False, bind=engine, future=True, expire_on_commit=False
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)

    adresses: WriteOnlyMapped[list["Address"]] = relationship(back_populates="user")
    emails: Mapped[list["Email"]] = relationship(
        primaryjoin=lambda: User.id == Email.owner_id
    )


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    user: Mapped[User] = relationship()


class Email(Base):
    __tablename__ = "email"

    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[str]
    owner_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))


Base.metadata.create_all(engine)


with SessionLocal() as db:
    user1 = User()
    user2 = User()

    db.add_all([user1, user2])
    db.flush()

    def call(user):
        logging.warning("=====================================   USER_ID %s ==========================", user.id)

        scope = user.adresses.insert().returning(Address).options(
            selectinload(Address.user).joinedload(User.emails.and_(Email.owner_id == user.id))
        )

        return db.scalar(scope, [{"email_address": "test"}])

    call(user1)
    call(user2)
