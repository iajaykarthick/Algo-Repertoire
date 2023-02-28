 ## SELECT / RETRIEVE Kth ranked value.

 select $k^{th}$ rank value (either $k^{th}$ maximum or $k^{th}$ minimum)

## LIMIT / OFFSET Approach

```
SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC[ASC]
LIMIT 1 OFFSET k-1
```