from pydantic import BaseModel


class ModelRequest(BaseModel):
    num: int
