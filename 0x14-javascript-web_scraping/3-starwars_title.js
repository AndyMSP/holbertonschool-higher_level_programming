#!/usr/bin/node

const process = require('process');
const axios = require('axios');

const id = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + id + '/';

async function getName (url) {
  try {
    const response = await axios.get(url);
    console.log(response.data.title);
  } catch (error) {
    console.log(error.response.status);
  }
}

getName(url);
