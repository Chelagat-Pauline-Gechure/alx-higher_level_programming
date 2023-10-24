#!/usr/bin/node

if (process.argv.length !== 3) {
    console.error('Usage: node <script-file> <ID>');
    process.exit(1);
  }
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
