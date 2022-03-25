from sqlalchemy import Column, BigInteger, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ChannelMember(Base):
    __tablename__ = "members"

    user_id = Column(BigInteger, primary_key=True, unique=True)
    user_name = Column(Text, default="NotName")
    user_position = Column(Text, default="NotPosition")
    invite_link = Column(Text, default="NotInviteLink")
    user_status = Column(Text, default="member")

    def __init__(self, request_id: int, user_id: int,
                 user_name: str, user_position: str, invite_link: str, user_status: str):
        self.request_id = request_id
        self.user_id = user_id
        self.user_name = user_name
        self.user_position = user_position
        self.invite_link = invite_link
        self.user_status = user_status









