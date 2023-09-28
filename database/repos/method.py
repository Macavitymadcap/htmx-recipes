from typing import NamedTuple
from .base import BaseRepository, DbContext

class CreateMethod(NamedTuple):
  step: int
  instruction: str

class ReadMethod(NamedTuple):
  id: int
  step: int
  instruction: str

class UpdateMethod(NamedTuple):
  step: int
  instruction: str
  id: int

class MethodRepository(BaseRepository):
  def __init__(self, db_context: DbContext) -> None:
    super().__init__(db_context)
  
  def create_method(self, values: CreateMethod) -> int:
    method_id = self._create_row_from_values("INSERT INTO methods (step, instruction) VALUES (?,?);", values)

    return method_id
    
  def read_method(self, method_id: int) -> ReadMethod | None:
    result = self._read_row_by_id("SELECT * FROM methods WHERE id=?;", method_id)

    return result
  
  def update_method(self, method: UpdateMethod) -> UpdateMethod | None:
    self._update_row_with_values("UPDATE methods SET step = ?, instruction = ? WHERE id = ?;", method)

    return self.read_method(method[-1])
  
  def delete_method(self, method_id: int) -> ReadMethod | None:
    method = self.read_method(method_id)
    self._delete_row_by_id("DELETE FROM methods WHERE id = ?;", method_id)

    return method