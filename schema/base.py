from typing import Any

from pydantic import BaseModel


class BaseSchema(BaseModel):
    def encode(self) -> bytes:
        return self.model_dump_json().encode("utf-8")

    @classmethod
    def decode(cls, json_string: str):
        return cls.model_validate_json(cls, json_string)


class BaseResponse(BaseModel):
    StatusCode: int
    Description: str
    Data: Any
