$(function () {
  $.ajax({
    url: 'getkeywords',
    data: {
      userstatus: $(".navbar").hasClass('navbar-expand')
    }
  }).then(
    function (data) {
      $('#searchinput').autocomplete({
        source: data.keywords
      });
    }
  );
});