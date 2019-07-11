/* simple queries */

/* Use the WHERE clause to show the appearance of rats */
SELECT appearance
FROM animals
WHERE species = "rat";

/* Use IN to show the species for animals with vertebrate_class 'mammal' and 'amphibian' */
SELECT species
FROM animals
WHERE vertebrate_class IN ('mammal', 'amphibian');


