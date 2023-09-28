from typing import NamedTuple, Optional
from .base import BaseRepository, DbContext

class CreateIngredient(NamedTuple):
  name: str
  quantity: Optional[int]
  unit: Optional[str]

class ReadIngredient(NamedTuple):
  id: int
  name: str
  quantity: Optional[int]
  unit: Optional[str]

class UpdateIngredient(NamedTuple):
  name: str
  quantity: Optional[int]
  unit: Optional[str]
  id: int

class IngredientRepository(BaseRepository):
  def __init__(self, db_context: DbContext) -> None:
    super().__init__(db_context)
  
  def create_ingredient(self, values: CreateIngredient) -> int:
    ingredient_id = self._create_row_from_values("INSERT INTO ingredients (name, quantity, unit) VALUES (?,?,?);", values)

    return ingredient_id
    
  def read_ingredient(self, ingredient_id: int) -> ReadIngredient | None:
    result = self._read_row_by_id("SELECT * FROM ingredients WHERE id=?;", ingredient_id)

    return result
  
  def update_ingredient(self, ingredient: UpdateIngredient) -> UpdateIngredient | None:
    self._update_row_with_values("UPDATE ingredients SET name = ?, quantity = ?, unit = ? WHERE id = ?;", ingredient)

    return self.read_ingredient(ingredient[-1])
  
  def delete_ingredient(self, ingredient_id: int) -> ReadIngredient | None:
    ingredient = self.read_ingredient(ingredient_id)
    self._delete_row_by_id("DELETE FROM ingredients WHERE id = ?;", ingredient_id)

    return ingredient