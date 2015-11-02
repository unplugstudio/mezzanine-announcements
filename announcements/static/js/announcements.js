$(document).ready(function() {
    // http://www.w3schools.com/JS/js_cookies.asp
    function setCookie(c_name, value, expiredays) {
        var exdate = new Date();
        exdate.setDate(exdate.getDate() + expiredays);
        document.cookie=c_name + "=" + escape(value) +
            ((expiredays === null) ? "" : ";expires=" + exdate.toUTCString());
    }

    $(".close-announcement").on("click", function() {
        var announcementId = $(this).data("announcementId");
        setCookie("announcements_dismiss", announcementId, 365);
    });
});
