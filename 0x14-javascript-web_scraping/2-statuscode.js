#!/usr/bin/node

const axios = require('axios');
const process = require('process');

const url = process.argv[2];

axios.get(url)
  .then((response) => console.log('code: ' + response.status))
  .catch((error) => console.log('code: ' + error.response.status));
