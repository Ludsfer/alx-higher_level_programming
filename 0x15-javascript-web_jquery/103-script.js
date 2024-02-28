(document).ready(function () {
  function translate () {
    $('div#hello').empty();
    const len = $('input#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=' + len,
      success: function (data) {
        $('div#hello').append(data.hello);
      }
    });
  }
  $('input#btn_translate').click(function () {
    translate();
  });
  $('input#language_code').keypress(function (e) {
    const key = e.which;
    if (key === 13) {
      translate();
    }
  });
});
