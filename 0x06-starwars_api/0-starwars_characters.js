#!/usr/bin/node
const request = require('request');
const host = "https://swapi-api.alx-tools.com/api/films/";

if (process.argv.length < 3){
	console.log("Usage: files MovieID");
	return
}
const movie_id = process.argv[2];

const url = host + movie_id; 

request(url, function (error, response, body){
	console.log(response);
});
