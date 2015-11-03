$(document).ready(function() {
    $(".close-announcement").on("click", function() {
        $this = $(this);
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
    });
});
