--- https://leetcode.com/problems/combine-two-tables/
SELECT
    p.firstName as firstName,
    p.lastName as lastName,
    a.city as city,
    a.state as state
FROM Person as p
LEFT JOIN Address as a ON a.personId = p.personId;
