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

# 197. Rising Temperatures 
SELECT e.id AS Id
FROM Weather w, Weather e
WHERE e.temperature > w.temperature
AND DATEDIFF(e.recordDate, w.recordDate) = 1

