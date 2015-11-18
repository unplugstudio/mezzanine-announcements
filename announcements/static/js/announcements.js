function closeAnnouncement(element) {
    $this = $(element);
    var cname = "announcements_dismiss";
    var announcementId = ($this.data("announcementId")).toString();
    var expiredays = 365
    var cvalue = Cookies.get(cname);

    if (cvalue) {
        cvalue = cvalue.split("_");
        if (cvalue.indexOf(announcementId) < 0) {
            cvalue.push(announcementId)
        }
        cvalue = cvalue.join("_");
    } else {
        cvalue = announcementId;
    }
    if ($this.attr("data-expire-days")) {
        expiredays = $this.data("expireDays");
    }
    Cookies.set(cname, cvalue, {expires: expiredays});

    // Add fadeout transition to dismissable announcements
    $this.closest(".announcement").fadeOut();
}

$(document).ready(function() {
    $(".announcement").each(function() {
        $this = $(this);
        var delay_time = $this.data("appearanceDelay");
        var announcement_id = $this.data("announcementId");
        setTimeout(function(){
            $(".announcement[data-announcement-id="
                + announcement_id + "]").fadeIn("slow");
        }, delay_time);
    });

    $(".close-announcement").on("click", function() {closeAnnouncement(this);});
});
