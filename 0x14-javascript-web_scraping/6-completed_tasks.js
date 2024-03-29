#!/usr/bin/node

const process = require('process');
const axios = require('axios');

const url = process.argv[2] + '?completed=true';

const count = {};

axios.get(url)
  .then(response => {
    const todos = response.data;
    todos.forEach(task => {
      if (count[task.userId] === undefined && task.completed) {
        count[task.userId] = 0;
      }
      if (task.completed) {
        count[task.userId]++;
      }
    });
    console.log(count);
  });
