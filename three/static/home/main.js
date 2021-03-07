$(document).ready(function () {
    window.setTimeout(function () {
      $(".alert").fadeTo(500, 0).slideUp(500, function () {
        $(this).remove();
      });
    }, 2000);
  });


  function removeRedacted() {
    var categories = document.getElementsByClassName("redacted");

    while (categories.length > 0) {
      categories[0].classList.remove("redacted");   
    }
  }