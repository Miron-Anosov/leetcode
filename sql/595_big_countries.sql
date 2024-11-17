-- https://leetcode.com/problems/big-countries/

-- Write your PostgreSQL query statement below
SELECT name, population,  area FROM World
Where area >= 3000000 OR population >= 25000000;