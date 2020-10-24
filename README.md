# Mezzanine Announcements

[![Workflow status](https://github.com/unplugstudio/mezzanine-announcements/workflows/Test%20and%20release/badge.svg)](https://github.com/unplugstudio/mezzanine-announcements/actions)
[![PyPI version](https://badge.fury.io/py/mezzanine-announcements.svg)](https://pypi.org/project/mezzanine-announcements/)
[![Python versions](https://img.shields.io/pypi/pyversions/mezzanine-announcements)](https://pypi.org/project/mezzanine-announcements/)
[![Follows: Semantic Versioning](https://img.shields.io/badge/follows-SemVer-blue.svg)](https://semver.org/)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Mezzanine app to create and display site-wide announcements.

## Features

- Schedulable announcements (start and end datetimes)
- Define as many announcement types as you want in settings
- Make announcements optionally dismissable by the user
- An announcement will not bother the user after they have dismissed it
- Optionally make the announcement reappear after a set amount of days
- Add an optional time delay after page load before showing an announcement

## Installation

1. Install via pip: `pip install mezzanine-announcements`
1. Add to `"announcements"` to `INSTALLED_APPS`.
1. Run migrations.
1. Add `"announcements.context_processors.announcements"` to your context processors.
1. Define the list of announcement templates that will be available for your admin users. This is a tuple of two-value tuples defined in `settings.ANNOUNCEMENTS_TEMPLATES` where the first element is the path to the Django template to be used, and the second element is the friendly name displayed in the admin for said template. For example:

   ```python
   ANNOUNCEMENTS_TEMPLATES = (
       ("announcements/modal.html", "Modal"),
       ("announcements/top_bar.html", "Top bar"),
   )
   ```
   You need to create this templates yourself. An example is provided below.
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
defined in `settings.ANNOUNCEMENTS_TEMPLATES`. You could use a Bootstrap modal,
or simple horizontal bar on the top of your page. The only conditions that you
need to keep in mind are the following:

- The template must contain a single element of the class `announcement`.
- The announcement ID, delay, and expiration must be present as data attributes
  on the `.announcement` element.
- If the announcement is dismissable, you must include a clickable element with
  the class `close-announcement` as a child of `.announcement`.

```django
{% load mezzanine_tags %}
<div
	class="announcement"
	data-appearance-delay="{{ announcement.appearance_delay }}"
	data-announcement-id="{{ announcement.id }}"
	data-expire-days="{{ announcement.expire_days }}"
>
	{{ announcement.content|richtext_filters|safe }}
	{% if announcement.can_dismiss %}
		<button class="close-announcement">Close</button>
	{% endif %}
</div>
```

## Settings

| Name                           | Default value | Description                                                                                             |
|--------------------------------|---------------|---------------------------------------------------------------------------------------------------------|
| ANNOUNCEMENTS_TEMPLATES        | None          | List of templates available for announcements. See Templates section above |
| ANNOUNCEMENTS_EXTRA_FIELDS     | None          | List of additional fields to display in the announcement admin: ["extra_content", "video_link", "form"] |

## Contributing

Review contribution guidelines at [CONTRIBUTING.md].

[CONTRIBUTING.md]: CONTRIBUTING.md
