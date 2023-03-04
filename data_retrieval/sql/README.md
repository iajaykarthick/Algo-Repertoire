 ## SELECT / RETRIEVE Kth ranked value. 
 [[Leetcode](https://leetcode.com/problems/second-highest-salary/)]

 select $k^{th}$ ranked value (either $k^{th}$ maximum or $k^{th}$ minimum)

## LIMIT / OFFSET Approach

```
SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC[ASC]
LIMIT 1 OFFSET k-1
```

## Output null / Default value if no rows returned

```
SELECT IFNULL(
    (
        SELECT DISTINCT Salary
        FROM Employee
        ORDER BY Salary DESC[ASC]
        LIMIT 1 OFFSET k-1
    )
),NULL) AS SecondHighestSalary

```

## 177. Nth Highest Salary
 [[Leetcode](https://leetcode.com/problems/nth-highest-salary/)]


 ```
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      WITH CTE AS
      (
          SELECT salary, DENSE_RANK() OVER (ORDER BY Salary DESC) AS salary_rank FROM Employee
      )
      SELECT MAX(salary)
      FROM CTE
      WHERE salary_rank = N
  );
END
 ```


 ## 185. Department Top Three Salaries
 [[Leetcode]( https://leetcode.com/problems/department-top-three-salaries/)]


 ```
WITH CTE AS (
    SELECT  d.name as Department, 
            e.name as Employee, 
            e.salary as Salary, 
            DENSE_RANK() OVER (
                PARTITION BY d.id
                ORDER BY e.salary DESC
            ) AS salary_rank
    FROM Department d
    JOIN Employee e
    ON d.id = e.departmentId
)
SELECT Department, Employee, Salary
FROM CTE
WHERE salary_rank < 4;
 ```