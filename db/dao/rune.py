from typing import List

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Rune



class RuneControl:

    @staticmethod
    async def insert(
        session: AsyncSession, 
        model: Rune
    ) -> Rune:

        stamt = insert(Rune).values(**model.dict()).returning(
            Rune.ID,
            Rune.Name
        )

        result = await session.execute(statement=stamt)
        
        await session.flush()

        return Rune(**result.first()._asdict())


    @staticmethod
    async def query_all(
        session: AsyncSession, 
        offset: int, 
        limit: int
    ) -> List[Rune]:
        
        if limit == -1:
            stamt = select(Rune).offset(offset)

        else:
            stamt = select(Rune).offset(offset).limit(limit)

        result = await session.execute(stamt)
        
        return result.scalars().all()
