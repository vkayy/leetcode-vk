SELECT name, bonus
FROM Employee LEFT JOIN Bonus
ON Employee.empId = Bonus.empId
WHERE bonus < 1000 OR bonus IS NULL

-- first, we need to use LEFT JOIN to get all the employees
-- then, we need to filter out the employees whose bonus is less than 1000 or null
-- finally, we need to select the name and bonus