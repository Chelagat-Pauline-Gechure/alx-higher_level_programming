#!/usr/bin/node

const request = require('request');

// Check if the file path argument and string to write is provided
if (process.argv.length !== 3) {
    console.error('Usage: node <script-file> <ID>');
    process.exit(1);
  }

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log('Error',error);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
