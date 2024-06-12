from pydantic import BaseModel, Field, PostgresDsn

class PostgresSetting(BaseModel):
    Dsn: PostgresDsn = Field(
        title="DB DSN",
        default="postgres://user:pwd@host:port/db"
    )