$(function () {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
      if (status === 'success') {
        $.each(data.results, function (id) {
          $('UL#list_movies').append('<li>' + data.results[id].title + '</li>');
        });
      }
    });
  });
