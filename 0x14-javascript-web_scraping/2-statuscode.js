#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) console.log(error);

  console.log('code: ' + response.statusCode);
});
