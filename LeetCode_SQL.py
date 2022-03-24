# LeetCode SQL practice
# This file is updated on regular basis

## *************** Diffuculty Level: Easy ********************
# 175. Combine Two Tables (accepted)
# Write your MySQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId

# 176. Second highest salary (accepted)
# Write your MySQL query statement below
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee 
WHERE salary < (SELECT MAX(salary) 
                FROM Employee);

# 181. Employees Earning More Than Their Managers (accepted)
# Write your MySQL query statement below
SELECT e.name AS Employee
FROM Employee e JOIN Employee m
ON m.id = e.managerId
WHERE e.salary > m.salary

# 182. Duplicate Emails (accepted)
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1; 

# 183. Customers who never order (accepted)
SELECT c.name AS Customers
FROM Customers c
WHERE c.id NOT IN (SELECT customerId FROM Orders)

# 627. Swap Salary
UPDATE salary 
 SET sex = IF (sex = 'm', 'f', 'm')


# 1179. Reformat Department Table (accepted)
SELECT ID,
sum(case when month ='Jan' then revenue else NULL end) Jan_Revenue,
sum(case when month ='Feb' then revenue else NULL end) Feb_Revenue,
sum(case when month ='Mar' then revenue else NULL end) Mar_Revenue,
sum(case when month ='Apr' then revenue else NULL end) Apr_Revenue,
sum(case when month ='May' then revenue else NULL end) May_Revenue,
sum(case when month ='Jun' then revenue else NULL end) Jun_Revenue,
sum(case when month ='Jul' then revenue else NULL end) Jul_Revenue,
sum(case when month ='Aug' then revenue else NULL end) Aug_Revenue,
sum(case when month ='Sep' then revenue else NULL end) Sep_Revenue,
sum(case when month ='Oct' then revenue else NULL end) Oct_Revenue,
sum(case when month ='Nov' then revenue else NULL end) Nov_Revenue,
sum(case when month ='Dec' then revenue else NULL end) Dec_Revenue
FROM Department
GROUP BY id;

# 197. Rising Temperatures (accepted)
SELECT e.id AS Id
FROM Weather w, Weather e
WHERE e.temperature > w.temperature
AND DATEDIFF(e.recordDate, w.recordDate) = 1

# 620. Not Boring Movies (accepted)
SELECT id, movie, description, rating
FROM Cinema
WHERE id % 2 = 1
AND description NOT LIKE '%boring%'
ORDER BY rating DESC


# ******************* Difficulty Level: Medium ******************************
# 177. Nth Highest Salary (accepted)
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
     
      # Write your MySQL query statement below.
      SELECT IF (N > COUNT(s), NULL, MIN(s))
      FROM (SELECT DISTINCT (salary) AS s FROM Employee
      ORDER by salary DESC
      LIMIT N
      ) as t           
  );
END
