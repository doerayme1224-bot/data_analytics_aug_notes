```sql
select 
	region,
	count(region) as amount_of_orders
from instacart_data
group by region;
-- shows me count of orders per region
```

```sql
select
	region,
	count(issue_reported) as amount_of_issues
from instacart_data
where issue_reported != 0
group by region;
-- shows me count of issues reported per region
```

```sql

select 
	region,
	customer_order_rating,
	count(customer_order_rating)
from instacart_data
group by region, customer_order_rating
order by region, customer_order_rating desc;
-- shows me amount of stars per region
```

