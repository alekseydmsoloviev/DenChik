from sqlalchemy import (Column, Integer, BigInteger, Text, ForeignKey, Boolean, TIMESTAMP,
                        create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from bot.config import load_config

config = load_config()
engine = create_engine(config.db_url)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    topics = relationship('Topic', back_populates='user')

    @staticmethod
    async def id_by_telegram(tid: int) -> int:
        session = SessionLocal()
        user = session.query(User).filter_by(telegram_id=tid).first()
        return user.id if user else None


class Topic(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(Text)
    current_step = Column(Integer, default=1)
    user = relationship('User', back_populates='topics')
    mantras = relationship('Mantra', back_populates='topic')


class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey('topics.id'))
    question_index = Column(Integer)
    answer_text = Column(Text)


class Mantra(Base):
    __tablename__ = 'mantras'
    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey('topics.id'))
    text = Column(Text)
    step_index = Column(Integer)
    topic = relationship('Topic', back_populates='mantras')
    reminders = relationship('Reminder', back_populates='mantra')


class Reminder(Base):
    __tablename__ = 'reminders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    mantra_id = Column(Integer, ForeignKey('mantras.id'))
    remind_at = Column(TIMESTAMP)
    sent = Column(Boolean, default=False)
    user = relationship('User')
    mantra = relationship('Mantra', back_populates='reminders')


def get_or_create_user(telegram_id: int) -> User:
    session = SessionLocal()
    user = session.query(User).filter_by(telegram_id=telegram_id).first()
    if not user:
        user = User(telegram_id=telegram_id)
        session.add(user)
        session.commit()
        session.refresh(user)
    return user

