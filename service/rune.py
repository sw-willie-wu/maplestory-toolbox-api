from sqlalchemy.ext.asyncio import AsyncSession

from schema.rune import Rune
from db.dao import RuneControl
from db.models import Rune as RuneModel



class RuneWriter:

    def __init__(self, db_session: AsyncSession):
        
        self.db_session: AsyncSession = db_session

    
    async def save_data_from_schema(self, schema: Rune):

        model = RuneModel(**schema.model_dump())
        model_inserted = await RuneControl.insert(self.db_session, model)

        return model_inserted.dict()


class RuneReader:

    def __init__(self, db_session: AsyncSession):
        
        self.db_session: AsyncSession = db_session

    
    async def load_all(self, offset: int = 0, limit: int = -1):
        queryset = await RuneControl.query_all(self.db_session, offset, limit)
        # res = []
        # for elem in queryset:
        #     res.append(
        #         {col.name: f'{getattr(model, col.name)}' for col in model.__table__.columns})
        return [elem.dict() for elem in queryset]


