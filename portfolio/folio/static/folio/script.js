$(document).ready(function () {
    $('#sidebarClose').on('click', function () {
        $('#sidebar').toggleClass('active');
        $(this).toggleClass('active');
    });
});