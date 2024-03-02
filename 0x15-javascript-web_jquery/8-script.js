#!/usr/bin/node
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (resp) {
  const movies = resp.results;

  movies.forEach (movie => {
    $('UL#list_movies').append($('<li></li>').text(movie.title));
  })
});
