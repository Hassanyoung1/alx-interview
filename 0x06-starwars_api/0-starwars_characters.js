#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    console.log(film.title);
    console.log('Characters:');

    // Function to fetch and print characters recursively
    function printCharacters (characters, index) {
      if (index < characters.length) {
        request(characters[index], function (charError, charResponse, charBody) {
          if (!charError && charResponse.statusCode === 200) {
            const character = JSON.parse(charBody);
            console.log(character.name);
            printCharacters(characters, index + 1);
          } else {
            console.error(`Error fetching character ${index + 1}: ${charError}`);
          }
        });
      }
    }

    printCharacters(film.characters, 0);
  } else {
    console.error(`Error fetching movie details: ${error}`);
  }
});
