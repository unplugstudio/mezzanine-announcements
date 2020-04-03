// https://gist.github.com/alirezas/c4f9f43e9fe1abba9a4824dd6fc60a55
function fadeIn(el, display) {
	function fade() {
		var val = parseFloat(el.style.opacity)
		if (!((val += 0.05) > 1)) {
			el.style.opacity = val
			requestAnimationFrame(fade)
		}
	}
	el.style.opacity = 0
	el.style.display = display || 'block'
	fade()
}
function fadeOut(el) {
	function fade() {
		if ((el.style.opacity -= 0.05) < 0) {
			el.style.display = 'none'
		} else {
			requestAnimationFrame(fade)
		}
	}
	el.style.opacity = 1
	fade()
}

// Close the parent .announcement when a button is clicked
// And store the closed announcement ID in a cookie
// so we don't show it again to the same user
function closeHandler(event) {
	var announcement = event.target.closest('.announcement')
	var announcementId = announcement.getAttribute('data-announcement-id')
	var expireDays = parseInt(announcement.getAttribute('data-expire-days') || 365)
	var cookieName = 'announcements_dismiss'
	var cookieValue = Cookies.get(cookieName)

	// Pause video iframes inside the announcement (if any)
	// Requires the site calling this script to be under HTTPS
	announcement.querySelectorAll('iframe').forEach(function (iframe) {
		var isVimeo = iframe.src.search('vimeo') !== -1
		var msg
		if (isVimeo) {
			msg = { method: 'pause' }
		} else {
			msg = { event: 'command', func: 'pauseVideo' }
		}
		iframe.contentWindow.postMessage(JSON.stringify(msg), '*')
	})

	// Parse the cookie as an array separated by _
	// and add the current announcement ID to the dismissed list
	cookieValue = cookieValue ? cookieValue.split('_') : []
	if (cookieValue.indexOf(announcementId) === -1) {
		cookieValue.push(announcementId)
	}
	cookieValue = cookieValue.join('_')
	Cookies.set(cookieName, cookieValue, { expires: expireDays })

	// Close the announcement with a fade
	fadeOut(announcement)
}

window.addEventListener('DOMContentLoaded', function () {
	// Show announcements (include delay as needed)
	document.querySelectorAll('.announcement').forEach(function (announcement) {
		var delay = parseInt(announcement.getAttribute('data-appearance-delay') || 0)
		setTimeout(function () { fadeIn(announcement) }, delay)
	})

	// Bind the close buttons on each announcement
	document.querySelectorAll('.close-announcement').forEach(function (button) {
		button.addEventListener('click', closeHandler)
	})
})
