SELECT * FROM `my-dbt-project-426120.recipe_dataset.recipe` LIMIT 10;

# number of recipes published per year
SELECT COUNT(*) AS recipe_num_per_year
FROM `my-dbt-project-426120.recipe_dataset.recipe`
GROUP BY EXTRACT(YEAR FROM DATE(datePublished));

# number of recipe types
SELECT COUNT(DISTINCT name) AS num_names
FROM `my-dbt-project-426120.recipe_dataset.recipe`;

# how many recipes are there for different levels of difficulty
SELECT difficulty, COUNT(*) AS num_recipes
FROM `my-dbt-project-426120.recipe_dataset.recipe`
GROUP BY difficulty
ORDER BY num_recipes DESC;
