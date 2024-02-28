$(document).ready(function () {
  $('input#btn_translate').click(function () {
    $('div#hello').empty();
    const len = $('input#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=' + len,
      success: function (data) {
        $('div#hello').append(data.hello);
      }
    });
  });
});
