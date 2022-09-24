#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const axios = require('axios');

const url = process.argv[2];
const file = process.argv[3];

axios.get(url)
  .then(response => fs.writeFile(file, response.data, 'utf8', (error) => {
    if (error) console.log(error);
  }));
