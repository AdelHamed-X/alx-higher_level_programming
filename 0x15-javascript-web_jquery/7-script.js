#!/usr/bin/node
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (resp) {
  $('#character').text(resp.name);
});
