#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
//
req.get(url + id, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const i of dd) {
    req.get(i, function (err1, response, body1) {
      if (err1) {
        console.log(err1);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
