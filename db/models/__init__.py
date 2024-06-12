from typing import Optional, Literal

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime, SMALLINT, VARCHAR, UUID, ForeignKey, TEXT, BIGINT, DECIMAL, ARRAY, INTEGER, ARRAY, JSON


class BaseModel(DeclarativeBase):
    __abstract__ = True
    __table_args__ = {
        'quote': False,
        'extend_existing': True,
    }
    __allow_unmapped__ = True

    def dict(self) -> dict:
        return {key: value for key, value in self.__dict__.items() if not key.startswith('_')}


class Rune(BaseModel):

    __tablename__='Rune'
    
    ID: int = Column(
        SMALLINT,
        name='ID',
        primary_key=True,
        nullable=False
    )

    Name: str = Column(
        VARCHAR(10),
        name='Name',
        nullable=False
    )

    NameEn: str = Column(
        VARCHAR(30),
        name='NameEn',
        nullable=False
    )

    DailyGain: int = Column(
        SMALLINT,
        name='DailyGain',
        default=10,
        nullable=False
    )

    PartyName: Optional[str] = Column(
        VARCHAR(20),
        name='PartyName',
        nullable=True
    )
    
    PartyGain: int = Column(
        SMALLINT,
        name='PartyGain',
        default=0,
        nullable=False
    )

    BonusArea: Optional[str] = Column(
        VARCHAR(20),
        name='BonusArea',
        nullable=True
    )

    BonusGain: int = Column(
        SMALLINT,
        name='BonusGain',
        default=0,
        nullable=False
    )

    Symbol: Literal['ARC', 'AUT'] = Column(
        VARCHAR(5),
        default='ARC',
        nullable=False
    )

    MaxLevel: int = Column(
        SMALLINT,
        name='MaxLevel',
        default=20,
        nullable=False
    )

    RuneNeed: dict = Column(
        JSON,
        name='RuneNeed',
        default=dict(),
        nullable=False
    )

    MoneyNeed: dict = Column(
        JSON,
        name='MoneyNeed',
        default=dict(),
        nullable=False
    )
