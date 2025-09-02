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


### 