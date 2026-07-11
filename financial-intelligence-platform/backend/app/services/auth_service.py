from sqlalchemy.orm import Session
from app.utils.security import verify_password, create_access_token
from app.models.user import User
from app.schemas.user_schema import UserRegister, UserLogin
from app.utils.security import hash_password
from fastapi.security import OAuth2PasswordRequestForm

def register_user(user: UserRegister, db: Session):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        return None

    new_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(user_data: OAuth2PasswordRequestForm, db: Session):
    user = db.query(User).filter(
    User.email == user_data.username
).first()

    if not user:
        return None

    if not verify_password(user_data.password, user.hashed_password):
        return None

    token = create_access_token({"sub": user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }