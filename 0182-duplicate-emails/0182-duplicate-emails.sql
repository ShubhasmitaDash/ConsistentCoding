# Write your MySQL query statement below
SELECT email "EMAIL"
FROM Person
GROUP BY email
HAVING COUNT(email)>1
