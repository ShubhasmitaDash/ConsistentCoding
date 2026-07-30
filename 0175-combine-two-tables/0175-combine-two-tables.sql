# Write your MySQL query statement below
SELECT Person.firstName, lastName, Address.city, state
FROM Person LEFT JOIN Address
ON Person.personId=Address.personId