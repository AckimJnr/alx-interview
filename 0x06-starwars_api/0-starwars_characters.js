#!/usr/bin/node
const request = require('request');
const host = 'https://swapi-api.alx-tools.com/api/films/';

if (process.argv.length < 3) {
  console.log('Usage: files MovieID');
  process.exit();
}
const movieId = process.argv[2];

const url = host + movieId;

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit();
  }

  if (response.statusCode !== 200) {
    console.error('Status code:', response.statusCode);
    process.exit();
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach(function (characterUrl) {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error('Error:', error);
        process.exit();
      }

      if (response.statusCode !== 200) {
        console.error('Status code:', response.statusCode);
        process.exit();
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
