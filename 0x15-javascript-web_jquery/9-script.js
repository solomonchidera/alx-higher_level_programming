$('document').ready(function () {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, status) {
      if (status === 'success') {
        $('#hello').text(data.hello);
      }
    });
  });
