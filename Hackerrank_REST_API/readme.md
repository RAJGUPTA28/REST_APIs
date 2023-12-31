# Question: REST API: City Weather Station

Use the HTTP GET method to retrieve information from a database of weather records. Query https://sonmock.hackerrank.com/api/weather/search?name=(keyword) to search all the records where name has a keyword anywhere in its string value. The query result is paginated and can be further accessed by appending to the query string &page=num where num is the page number.

The query response from the API is a JSON with the following five fields:

page the current page
per page: the maximum number of results per page total, the total number of records in the search result
total pages the total number of pages to query to get all the results
data: an array of JSON objects that contain weather records
The data field in the response contains a list of weather records with the following

schema:

name the name of the city
weather: temperature recorded
status: an array of wind speed and humidity records
Filter records to include a given keyword in the name parameter. Return an array such that each element is a string of comma-separated values: city name, temperature, wind, humidity.

For example,

"name": "Adelaide", "weather": "15 degree",

"status": [

"Wind: 8Kmph", "Humidity: 61%

The JSON record is stored as Adelaide, 15,8,61 Return the list sorted by city name.

Function Description

Complete the function weatherStation(keyword) in the editor below.

weatherStation has the following parameter(s): string keyword: the string to search

Returns

string[]: the weather data for each city

Note: Please review the header in the code stub to see available libraries for API requests in the selected language. Required libraries can be imported in order to sol the question. Check our full list of supported libraries at

https://www.hackerrank.com/environment.

Sample input: all
Sample output:
Dallas,12,5,5
Dallupura:10,9,14
Vallejo,1,24,56
