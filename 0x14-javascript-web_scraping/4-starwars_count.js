#!/usr/bin/node

const process = require('process');
const axios = require('axios');

const url = process.argv[2];

async function numMovies (url, id) {
  try {
    let count = 0;
    const response = await axios(url);
    const data = response.data;
    const films = data.results;
    films.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes('18')) {
          count++;
        }
      });
    });
    console.log(count);
  } catch (error) {
    console.log(error.response.status);
  }
}

numMovies(url, 18);
