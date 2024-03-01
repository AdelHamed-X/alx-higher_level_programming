#!/usr/bin/node
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  function (response, body) {
    console.log(JSON.parse(body).title);
  }
);
