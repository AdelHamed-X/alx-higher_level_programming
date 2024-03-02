#!/usr/bin/node
$('#toggle_header').click(function () {
  const header = $('header');

  if (header.hasClass('red') && header.hasClass('green')) {
    header.removeClass('red');
  } else if (!header.hasClass('red') && !header.hasClass('green')) {
    header.addClass('red');
  } else if (header.hasClass('red')) {
    header.removeClass('red');
    header.addClass('green');
  } else if (header.hasClass('green')) {
    header.removeClass('green');
    header.addClass('red');
  }
});
