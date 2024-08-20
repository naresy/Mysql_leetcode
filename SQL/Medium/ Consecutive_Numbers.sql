-- Table: Logs

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | num         | varchar |
-- +-------------+---------+
-- In SQL, id is the primary key for this table.
-- id is an autoincrement column.
 

-- Find all numbers that appear at least three times consecutively.

-- Return the result table in any order.

-- The result format is in the following example.

-- solution


WITH ConsecutiveNums AS (
    SELECT
        num,
        LEAD(num, 1) OVER (ORDER BY id) AS next_num,
        LEAD(num, 2) OVER (ORDER BY id) AS next_next_num,
        LAG(num, 1) OVER (ORDER BY id) AS prev_num,
        LAG(num, 2) OVER (ORDER BY id) AS prev_prev_num
    FROM Logs
)
SELECT DISTINCT
    num AS ConsecutiveNums
FROM ConsecutiveNums
WHERE (num = next_num AND num = next_next_num)
   OR (num = prev_num AND num = next_num)
   OR (num = prev_prev_num AND num = prev_num);

-- short method
SELECT DISTINCT L1.num AS ConsecutiveNums
FROM Logs L1
JOIN Logs L2 ON L1.id = L2.id + 1
JOIN Logs L3 ON L2.id = L3.id + 1
WHERE L1.num = L2.num AND L2.num = L3.num;
