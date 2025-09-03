# Date and Time functions
[[SQL]]
#### 1. `date()`
returns the date part of from a `datetime` expression ( returns as YYYY,MM,DD)
- good when I need the date (looking at the date a client purchased an item)
**EX:**
`SELECT date(created_at) AS date_only`
`FROM events;`
`-- Returns the date part of the created_at datetime values`
#### 2. `time()`
returns time part of a `datetime` expression (returns as HH:MM:SS)
- good for more time specific data (like when a business transaction would occur)
**EX:**
`SELECT time(created_at) AS time_only`
`FROM events;`
`-- Returns the time part of the created_at datetime values`
#### 3. `datetime()`
Returns full timestamp (YYYY,MM,DD . HH:MM:SS)
- good for precise timestamping
**EX:**
`SELECT datetime(created_at) AS full_timestamp`
`FROM events;`
`-- Returns full datetime string from created_at field`
#### 4.`strftime()`
Lets me create custom formats for how the time should return
**EX for custom format:**
`SELECT strftime('%Y-%m-%d %H:%M:%S', created_at) AS formatted_datetime`
`FROM events;`
`-- Custom format for datetime values`

**EX for extracting components:**
`SELECT`
 ` strftime('%Y', created_at) AS year,`
  `strftime('%m', created_at) AS month,`
  `strftime('%d', created_at) AS day,`
  `strftime('%H', created_at) AS hour,`
  `strftime('%M', created_at) AS minute,`
  `strftime('%S', created_at) AS second`
`FROM events;`
`-- Extracts year, month, day, hour, minute, and second from created_at`
**[for Further Details](https://sqlite.org/lang_datefunc.html)**

#### Good Tips/Practices
- Ensure dates and times are in the recognized formats (YYYY,MM,DD . HH:MM:SS)
- use `strftime()` when dealing with more intricate extractions
- `date()` and `time()` functions don't account for time zones (you'll need to adjust)
#### PostgreS/MySQL
they handle these functions differently
**EX PostgreS:**
`SELECT EXTRACT(YEAR FROM created_at) AS year`
`FROM events;`
`EXTRACT` and `TO_CHAR`

**MySQL**
`SELECT YEAR(created_at) AS year`
`FROM events;`
`DATE_FORMAT`, `YEAR`, `MONTH` (direct date functions)

**[Video on Date and Time Functions](https://www.loom.com/share/4341044291d74a2dafedc1cbd53bd198?sid=63cf0372-1ef1-4aee-9879-595d16e18c78)**