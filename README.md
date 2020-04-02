# Mezzanine Announcements

A Mezzanine app to create and display site-wide announcements.

## Features

- Schedulable announcements (start and end datetimes)
- Define as many announcement types as you want in settings
- Make announcements optionally dismissable by the user
- An announcement will not bother the user after they have dismissed it
- Optionally make the announcement reappear after a set amount of days
- Add an optional time delay after page load before showing an announcement

## Installation

1. Install via pip: `pip install -e git+https://gitlab.com/unplugstudio/mezzanine-announcements.git#egg=mezzanine-announcements`
1. Add to `"announcements"` to `INSTALLED_APPS`.
1. Run migrations.
1. Add `"announcements.context_processors.announcements"` to your context processors.
1. Define the list of announcement templates that will be available for your
   admin users. This is a tuple of two-value tuples defined in
   `settings.ANNOUNCEMENT_TEMPLATES` where the first element is the path to the
   Django template to be used, and the second element is the friendly name
   displayed in the admin for said template. For example:

   ```python
   ANNOUNCEMENT_TEMPLATES = (
       ("includes/announcements/modal.html", "Modal"),
       ("includes/announcements/top_bar.html", "Top bar"),
   )
   ```
1. Add some announcements in the new "Announcements" section in the admin.

Then to display the announcements in your templates:

1. Add the cookies and announcement scripts to the templates where you want to use the announcements
    ```django
    <script src="{% static 'js/js.cookie.js' %}"></script>
    <script src="{% static 'js/announcements.js' %}"></script>
    ```
1. Include the template with all announcements in a `{% nevercache %}` block:

   ```django
   {% nevercache %}
   {% include "announcements/announcements.html" %}
   {% endnevercache %}
   ```

## Templates

You can use any markup and styling you want in the announcement templates
defined in `settings.ANNOUNCEMENT_TEMPLATES`. You could use a Bootstrap modal,
or simple horizontal bar on the top of your page. The only conditions that you
need to keep in mind are the following:

- The template must contain a single element of the class `announcement`.
- The announcement ID, delay, and expiration must be present as data attributes
  on the `.announcement` element.
- If the announcement is dismissable, you must include a clickable element with
  the class `close-announcement` as a child of `.announcement`.

```django
<div class="announcement"
	data-appearance-delay="{{ announcement.appearance_delay }}"
	data-announcement-id="{{ announcement.pk }}"
	data-expire-days="{{ announcement.expire_days|default:'false' }}">
	{{ announcement.content }}
	{% if announcement.can_dismiss %}
		<button class="close-announcement">Close</button>
	{% endif %}
</div>
```

## Settings

| Name                           | Default value | Description                                                                                             |
|--------------------------------|---------------|---------------------------------------------------------------------------------------------------------|
| ANNOUNCEMENTS_MAX_NUMBER       | 1             | How many announcements should be shown in the frontend even if several are active                       |
| ANNOUNCEMENTS_EXTRA_FIELDS     | None          | List of additional fields to display in the announcement admin: ["extra_content", "video_link", "form"] |
| ANNOUNCEMENTS_RICHTEXT_CONTENT | False         | Use TinyMCE when editing announcement content fields                                                    |

## Contributing

Review contribution guidelines at [CONTRIBUTING.md].

[CONTRIBUTING.md]: CONTRIBUTING.md
