#!/usr/bin/node
const request = require('request');
const host = 'https://swapi-api.alx-tools.com/api/films/';

if (process.argv.length < 3) {
  console.log('Usage: files MovieID');
  process.exit();
}
const movieId = process.argv[2];

const url = host + movieId;

function fetchData(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      if (response.statusCode !== 200) {
        reject(new Error(`Status code: ${response.statusCode}`));
        return;
      }
      resolve(JSON.parse(body));
    });
  });
}

async function getCharacters(movieId) {
  try {
    const film = await fetchData(host + movieId);
    const characters = film.characters;
    const characterPromises = characters.map(characterUrl => fetchData(characterUrl));
    return Promise.all(characterPromises);
  } catch (error) {
    console.error('Error:', error);
    process.exit();
  }
}

(async () => {
  try {
    const characters = await getCharacters(movieId);
    characters.forEach(character => console.log(character.name));
  } catch (error) {
    console.error('Error:', error);
    process.exit();
  }
})();

