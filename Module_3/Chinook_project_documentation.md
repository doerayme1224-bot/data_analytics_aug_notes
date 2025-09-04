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
2. Show 