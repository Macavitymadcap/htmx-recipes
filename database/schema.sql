CREATE TABLE IF NOT EXISTS Ingredients (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  quantity REAL,
  unit TEXT
);

CREATE TABLE IF NOT EXISTS Methods (
  id INTEGER PRIMARY KEY,
  step INTEGER NOT NULL,
  instruction TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Recipes (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  servings INTEGER,
  cookTime TEXT,
  caloriesPerServing REAL
);

CREATE TABLE IF NOT EXISTS RecipeIngredients (
  recipeId INTEGER,
  ingredientId INTEGER,
  FOREIGN KEY (recipeId) REFERENCES Recipes(id),
  FOREIGN KEY (ingredientId) REFERENCES Ingredients(id)
);

CREATE TABLE IF NOT EXISTS RecipeMethods (
  recipeId INTEGER,
  methodId INTEGER,
  FOREIGN KEY (recipeId) REFERENCES Recipes(id),
  FOREIGN KEY (methodId) REFERENCES Methods(id)
);