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
    


/* Checkpoint */

/* As you begin exploring the city table from the world database, a place to start is to determine */
/* how many cities are in the table. Write a query that returns this value */

SELECT COUNT(name) 
FROM city;


/* A natural thing to wonder about these cities is how they are distributed around the world. */
/* To start with this topic, write a query to return the countrycode and count of cities in that country */
/* for only the country with the most cities in the city table */

SELECT countrycode, COUNT(name) 
FROM city 
GROUP BY 1 /* countrycode */ 
ORDER BY 2 
DESC LIMIT 1;


/* You could look at the number of cities per country to try to get a sense about cities all over the world, */
/* but since there are several hundred countries this is not easily digestible. Instead, look at the counts of cities */
/* per continent. Write a query that returns each continent and the number of cities in that continent. */
/* Be sure that each city in the city table is included in the counts from your query */

SELECT co.continent, COUNT(co.name) 
FROM country co 
LEFT JOIN city ci 
ON co.code = ci.countrycode 
GROUP BY co.continent;

SELECT co.continent, COUNT(ci.name) 
FROM city ci 
LEFT JOIN country co 
ON co.code = ci.countrycode 
GROUP BY co.continent;
