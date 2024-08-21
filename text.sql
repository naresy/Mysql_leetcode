
-- Maximum salary
select 
e.department,
e.employeeid,
e.salary
from
employee e
where 
e.salary=(
    select max(salary)
    from employee
    where department=e.department

)

e.department,e.employeeid






-- question 2

-- select 
-- c.customer_id,
-- c.customer_name
-- count(o.orderid)as ordercount
-- from customer c
-- join 
-- order o on c customer_id=o.customer_id
-- group by
-- c.customer_id, c.customer_name
-- having
-- count (o.orderid)>3
-- order by
-- ordercount desc
