$(document).ready(function() {
  //Animate dropdown
  $('#navbar li').hover(
    function () {
      $('ul', this).stop().slideDown(200);
    },
    function () {
      $('ul', this).stop().slideUp(200);
    }
  );

  //Resize iframe to full length
  $('#contentFrame').on("load", function() {
    this.style.height = this.contentWindow.document.body.scrollHeight + 'px';
  });

  //Fallback for without JS
  $('#navbar li ul').hide().removeClass('fallback');
});