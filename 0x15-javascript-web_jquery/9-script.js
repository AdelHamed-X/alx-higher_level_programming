$('document').ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (resp) {
    $('DIV#hello').text(resp.hello);
  })
});
