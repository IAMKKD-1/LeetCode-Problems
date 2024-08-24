# Write your MySQL query statement below
select d.name as Department, e.name as Employee, salary as Salary
from employee e
join department d on e.departmentid = d.id 
where (e.departmentId, Salary) IN (
        SELECT 
            departmentId, 
            MAX(Salary) 
        FROM 
            Employee 
        GROUP BY 
            departmentId
    );