#!/usr/bin/env python3
"""The attachment module"""

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from uuid import uuid4
from typing import Dict

Base = declarative_base()

engine = create_engine(
            "mysql+mysqldb://test:test@localhost/attachment",
            pool_pre_ping=True)
sessionFactory = sessionmaker(bind=engine, expire_on_commit=False)
session = scoped_session(sessionFactory)


class Attachment(Base):
    """Defines an attachment object"""
    __tablename__ = "attachments"

    id = Column(String(60), default=str(uuid4()), primary_key=True, nullable=False)
    name = Column(String(60), nullable=False)

    def save(self) -> None:
        """Commits the state of the current session to database"""
        session.add(self)
        session.commit()

    def all(self, obj=None) -> Dict:
        """
            Retrieves all instances of obj or all entries from
            database if obj is None
        """
        objects = {}

        query = session.query(self).all()
        for result in query:
            key = f"{result.__class__.__name__}.{result.id}"
            objects[key] = result

        return objects


Base.metadata.create_all(engine)
