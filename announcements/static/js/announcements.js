// Close the parent .announcement when a button is clicked
// And store the closed announcement ID in a cookie
// so we don't show it again to the same user
function close(event) {
    var $announcement = $(event.target).closest(".announcement");
    var announcementId = $announcement.data("announcementId").toString();
    var expiredays = $announcement.data("expireDays") || 365;
    var cookieName = "announcements_dismiss";
    var cookieValue = Cookies.get(cookieName);
    var $iframes = $(".announcement iframe");

    // If there are iframe videos in the announcements, then pause them all
    $iframes.each(function(i, iframe) {
        var isVimeo = iframe.src.search("vimeo") > -1;
        var msg;
            if (isVimeo) {
                msg = {method: "pause"};
        } else {
            msg = {event: "command", func: "pauseVideo"};
        }
        iframe.contentWindow.postMessage(
            JSON.stringify(msg), "*"
        )
    });

    // If the announcement cookie is present, parse it as an array
    if (cookieValue) {
        cookieValue = cookieValue.split("_");
        if (cookieValue.indexOf(announcementId) < 0) {
            cookieValue.push(announcementId);
        }
        cookieValue = cookieValue.join("_");
    // Else, just add the current announcement id as the first element
    } else {
        cookieValue = announcementId;
    }

    // Store the cookie with the expiration information
    Cookies.set(cookieName, cookieValue, {expires: expiredays});

    // Close the announcement with a fade
    $announcement.fadeOut();
}

$(document).ready(function() {
    // Show announcements (include delay as needed)
    $(".announcement").each(function() {
        var $this = $(this);
        var delay_time = $this.data("appearanceDelay") || 0;
        setTimeout(function(){
            $this.fadeIn();
        }, delay_time);
    });

    // Bind the close buttons on each announcement
    $(".close-announcement").on("click", close);
});
