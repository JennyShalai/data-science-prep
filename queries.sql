/* simple queries */

/* Use the WHERE clause to show the appearance of rats */
SELECT appearance
FROM animals
WHERE species = "rat";

/* Use IN to show the species for animals with vertebrate_class 'mammal' and 'amphibian' */
SELECT species
FROM animals
WHERE vertebrate_class IN ('mammal', 'amphibian');

/* Use BETWEEN to show species that have at least 1 leg, but no more than than 3 legs */
SELECT species
FROM animals
WHERE num_legs
BETWEEN 1 and 3;

/* Use LIKE to show species that have an appearance that starts with 'f' */
SELECT species
FROM animals
WHERE appearance
LIKE "f%";



/* Aggregate functions */

/* Use an aggregate function to return the number of countries that became independent in the year 1918 */
SELECT COUNT(code)
FROM country
WHERE indepyear = 1918;


/* Write a query that returns the average population of countries whose government is a Constitutional Monarchy */
SELECT avg(population)
FROM country
WHERE governmentform = "Constitutional Monarchy";

/* Write a query that returns each continent and the area of the largest country in that continent */
SELECT continent, MAX(surfacearea)
FROM country
GROUP BY continent;


/* Joining tables */

/* Using the animalshp database, return a table showing the name and appearance of every pet. Order by pet name*/
SELECT name, appearance
    FROM pets
    JOIN animals
    ON pets.species = animals.species
    ORDER BY name;
