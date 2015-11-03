$(document).ready(function() {
    $(".close-announcement").on("click", function() {
        $this = $(this);
        var announcementId = $this.data("announcementId");
        var expiredays = 365
        if ($this.attr("data-expire-days")) {
            expiredays = $this.data("expireDays");
        }
        Cookies.set("announcements_dismiss", announcementId, {expires: expiredays});
    });
});
