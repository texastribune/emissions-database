Most fined (by value) 2014

```sql
select regulated_entity_rn_number, sum(penalty_value) as total
from emissions_issuedorder
where agended_at > '2014-01-01'
group by regulated_entity_rn_number
order by total desc
```


most fined (by value) 2013

```sql
select regulated_entity_rn_number, sum(penalty_value) as total
from emissions_issuedorder
where agended_at > '2013-01-01' and agended_at < '2014-01-01'
group by regulated_entity_rn_number
order by total desc
```

most fined (freq) 2014

```sql
select regulated_entity_rn_number, count(regulated_entity_rn_number) as total
from emissions_issuedorder
where agended_at > '2014-01-01'
group by regulated_entity_rn_number
order by total desc
```

most fined (freq) all history

```sql
select regulated_entity_rn_number, count(regulated_entity_rn_number) as total
from emissions_issuedorder
group by regulated_entity_rn_number
order by total desc
```

most fined (value) all history

```sql
select regulated_entity_rn_number, sum(penalty_value) as total
from emissions_issuedorder
group by regulated_entity_rn_number
order by total desc
```
