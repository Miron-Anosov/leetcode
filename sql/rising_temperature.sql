--https://leetcode.com/problems/rising-temperature/description/

SELECT w1.id
FROM Weather AS w1
WHERE w1.temperature > (
  SELECT MAX(w2.temperature)
  FROM Weather AS w2
  WHERE (w1.recordDate - w2.recordDate) = 1
);