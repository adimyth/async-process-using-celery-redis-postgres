from typing import List, Optional

from pydantic import BaseModel


class ModelResponse(BaseModel):
    state: str
    error: Optional[str] = ""
    primes: Optional[List[int]] = None
