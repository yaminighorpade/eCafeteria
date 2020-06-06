import datetime

from pydantic import BaseModel


class SystemInfo(BaseModel):
    name: str
    version: str
    deployed: datetime.datetime