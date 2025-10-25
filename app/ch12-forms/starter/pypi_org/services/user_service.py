from passlib.handlers.sha2_crypt import sha512_crypt as crypto
import pypi_org.data.db_session as db_session
from pypi_org.data.users import User
from typing import Optional


def get_user_count() -> int:
    session = db_session.create_session()
    return session.query(User).count()

def find_user_by_email(email: str) -> Optional[User]:
    session = db_session.create_session()
    return session.query(User).filter_by(email=email).first()

def find_user_by_id(id: int) -> Optional[User]:
    session = db_session.create_session()
    return session.query(User).filter_by(id=id).first()


def create_user(name: str, email: str, password: str) -> Optional[User]:
    if find_user_by_email(email):
        return None
    user = User()
    user.name = name
    user.email = email
    user.hashed_password = hash_text(password)

    session = db_session.create_session()
    session.add(user)
    session.commit()

    return user


def hash_text(text: str) -> str:
    hashed_text = crypto.encrypt(text, rounds=100123)
    print(hashed_text)
    return hashed_text

def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return crypto.verify(plain_text, hashed_text)

def login_user(email: str, password: str) -> Optional[User]:
    session = db_session.create_session()

    user = session.query(User).filter_by(email=email).first()
    if not user:
        return None

    try:
        verified = verify_hash(user.hashed_password, password)
    except:
        return None

    if verified:
        return user
    else:
        return None