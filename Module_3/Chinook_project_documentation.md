![Image on schema](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcPLnvrhvqHqRHo2cleRh0l09_0benSZpSAFBC6Pg-nwFEUNOiOmx-0JuSWc5pp_4xub5bOVbIp3wmN08z1dELXogRSkQ9Rf5s2BwDuhlnTGXdB6_DjF6GIrXxyX3phIv7b7L2V?key=lXni6_mNz9qqCZ7Kjudz-HpJ)

### Album Table
`select * `
`from Album;`

`select distinct ArtistId,`
`count(artistid) as number_of_albums`
`from Album`
`group by artistid`
`order by number_of_albums desc;`
- shows amount of albums by artist id in descending order

### artist table
`select * `
`from artist;`
- shows artist table (could be good with query above it/Album Table)

### Customer table
`select * `
`from Customer;`
- will be good with employee table

### Employee Table
`select * `
`from Employee;`
- will be good with customer table
- I think this is one of the more important tables

### Genre table
`select * `
`from Genre;`

### Invoice Table
- probably one of the more important ones
`select * `
`from Invoice; `
- would be good with Customer table


### Invoiceline table
`select *  `
`from InvoiceLine;`
- sale price, probably important 


### Media type
`select *  `
`from MediaType;`


### Playlist table
`select *  `
`from Playlist;`

### playlisttrack id
`select *  `
`from PlaylistTrack;`
- good with track and playlist table

### Track
`select *  `
`from Track;`
- brings many tables together (Mediatype, playlist, playlisttrack, and there is probably more)

### Questions
1. How does the sale price compare to the average of that media type
2. which employee works the hardest (helps the most people)
3. What are the demographics of their customers

### Bulid off of these queries

select *,
	employee.EmployeeId,
	customer.SupportRepId
from employee
full outer join customer on employee.EmployeeId = customer.SupportRepId;

**What do I want to Look at**
- employee id
- employee full name
- support rep id
- customer country
- potentually build on it so I could see how much a customer spent on an invoiceline


select *,
	track.MediaTypeId,
	MediaType.MediaTypeId
from track
full outer join MediaType on MediaType.MediaTypeId = track.MediaTypeId;

**What do I want to look at**
- MediaTypeID
- Name (from MediaType table)
- UnitPrice
- 

select *
from Customer;
**What do I want to look at**
- country
- if they work for a company
- look into how many invoices they have made 


### Slide Presentation Outline

1. Intro to Client
- show what type of business it is
- show how my analysis will help their business
2. Show my questions
- How does the sale price compare to the average of that media type
- which employee works the hardest (helps the most people)
- What are the demographics of their customers
3. present my findings for each question (with the sql scripts)
**The scripts:**
```sql
select 	
	c.FirstName,
	c.LastName,
	c.CustomerId,
	count(i.customerid) as amount_of_invoices,
	sum(i.total) as total_spent
from customer as c 
join invoice as i
on c.CustomerId = i.CustomerId
group by c.customerid
order by total_spent desc;
-- this query shows me the customers information, like the country they are from, if they work for a company or not, and the aamount of invoices and what they spent on those invoices.
```
avg price for each media type;
- 0.15 to 2.00 dollars

**[for mpeg audio file licensing](https://r.search.yahoo.com/_ylt=AwrhcZe6Jb5ocScBjhdXNyoA;_ylu=Y29sbwNiZjEEcG9zAzIEdnRpZAMEc2VjA3Ny/RV=2/RE=1758501562/RO=10/RU=https%3a%2f%2fsicorps.com%2fcoding%2fmpeg-audio-standards-and-their-licensing-fees%2f/RK=2/RS=Gft_oEVzV7wBdJFUDuTYoNdsDOc-)**

```sql
select 
	t.MediaTypeId,
	avg(t.UnitPrice),
	m.name
from track as t
join MediaType as m
on t.MediaTypeId = m.MediaTypeId
group by t.MediaTypeId;
-- this shows me the average price for each mediatype
```
```sql
select 
	c.SupportRepId,
	e.FirstName,
	e.LastName,
	count(c.SupportRepId) as customers_serviced
from Customer as c
join employee as e
on c.SupportRepId = e.EmployeeId
join invoice as i
on c.CustomerId = i.CustomerId
group by c.SupportRepId;
-- shows me the amount that each employee has helped a customer
```
4. conclusion/recommendations 

Protected MPEG-4 video file