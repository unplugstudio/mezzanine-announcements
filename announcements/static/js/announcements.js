$(document).ready(function() {
    // http://www.w3schools.com/JS/js_cookies.asp
    function setCookie(c_name, value, expiredays) {
        var exdate = new Date();
        exdate.setDate(exdate.getDate() + expiredays);
        document.cookie=c_name + "=" + escape(value) +
            ((expiredays === null) ? "" : ";expires=" + exdate.toUTCString());
    }

    $(".close-announcement").on("click", function() {
        $this = $(this);
        var announcementId = $this.data("announcementId");
        var expiredays = 365
        if ($this.attr("data-expire-days")) {
            expiredays = $this.data("expireDays");
        }
        setCookie("announcements_dismiss", announcementId, expiredays);
    });
});
