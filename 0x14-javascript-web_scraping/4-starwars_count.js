#!/usr/bin/node

const process = require('process');
const axios = require('axios');

const url = process.argv[2];

async function numMovies (url, id) {
  try {
    let count = 0;
    const response = await axios(url);
    const data = response.data;
    const numFilms = data.count;
    const films = data.results;
    for (let i = 0; i < numFilms; i++) {
      if (films[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  } catch (error) {
    console.log('error');
    console.log(error.response.status);
  }
}

numMovies(url, 18);
