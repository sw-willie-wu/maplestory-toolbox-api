from typing import Optional, Literal

from pydantic import Field

from .base import BaseSchema


class Rune(BaseSchema):
    
    ID: int = Field(
        title='ID'
    )

    Name: str = Field(
        title='Name'
    )

    NameEn: str = Field(
        title='NameEn'
    )

    DailyGain: int = Field(
        title='DailyGain',
        default=10
    )

    PartyName: Optional[str] = Field(
        title='PartyName',
        default=None
    )
    
    PartyGain: int = Field(
        title='PartyGain',
        default=0
    )

    BonusArea: Optional[str] = Field(
        title='BonusArea',
        default=None
    )

    BonusGain: int = Field(
        title='BonusGain',
        default=0
    )

    Symbol: Literal['ARC', 'AUT'] = Field(
        default='ARC'
    )

    MaxLevel: int = Field(
        title='MaxLevel',
        default=20
    )

    RuneNeed: dict = Field(
        title='RuneNeed',
        default=dict()
    )

    MoneyNeed: dict = Field(
        title='MoneyNeed',
        default=dict()
    )