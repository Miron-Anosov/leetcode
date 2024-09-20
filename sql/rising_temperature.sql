--https://leetcode.com/problems/rising-temperature/description/

SELECT w1.id
FROM Weather AS w1
WHERE w1.temperature > (
  SELECT MAX(w2.temperature)
  FROM Weather AS w2
  WHERE w2.recordDate < w1.recordDate
);