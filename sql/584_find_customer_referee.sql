--https://leetcode.com/problems/find-customer-referee/submissions/1397362835/

SELECT c.name FROM Customer AS c
WHERE c.referee_id != 2 OR c.referee_id IS NULL;