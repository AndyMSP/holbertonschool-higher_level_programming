#!/usr/bin/node

const process = require('process');
const axios = require('axios');

const id = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + id + '/';

async function getName (url) {
  const response = await axios.get(url);
  console.log(response.data.title);
}

getName(url);
