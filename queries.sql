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
