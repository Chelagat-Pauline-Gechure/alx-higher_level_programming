#!/usr/bin/node
const request = require('request');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 4-starwars_count.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error(`HTTP Status Code: ${response.statusCode}`);
  } else {
    const filmsData = JSON.parse(body);
    const characterId = 18; // Wedge Antilles' character ID
    const count = filmsData.results.reduce((total, film) => {
      return total + (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`) ? 1 : 0);
    }, 0);
    console.log(count);
  }
});
