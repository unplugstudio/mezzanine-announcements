# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

## [3.0.0](https://github.com/unplugstudio/mezzanine-announcements/compare/v2.0.0...v3.0.0) (2020-04-07)


### ⚠ BREAKING CHANGES

* all content fields use RichTextField by default and
settings.ANNOUNCEMENTS_RICHTEXT_CONTENT has been deprecated.

### Features

* use RichTextField on all content fields ([f909d32](https://github.com/unplugstudio/mezzanine-announcements/commit/f909d326f6b815a68462ff79db016d3bcdfdcf63))

## [2.0.0](https://github.com/unplugstudio/mezzanine-announcements/compare/v1.0.1...v2.0.0) (2020-04-03)


### ⚠ BREAKING CHANGES

* settings.ANNOUNCEMENT_TEMPLATES (singular) has been renamed to
settings.ANNOUNCEMENTS_TEMPLATES (plural) for consistency. Changing templates will no longer cause migrations
* support for south and Django < 1.8 has been dropped
* settings.ANNOUNCEMENTS_MAX_NUMBER doesn't exist anymore

### Features

* add default start date to announcement ([e8d9ae6](https://github.com/unplugstudio/mezzanine-announcements/commit/e8d9ae6177d2167dbb54ef47cca09d3dd3c7c15b))
* add default value to frequency field ([08a43d5](https://github.com/unplugstudio/mezzanine-announcements/commit/08a43d5ee8f455546c73f8e8b0580484a0ea7e69))
* remove ANNOUNCEMENTS_MAX_NUMBER ([0622ecc](https://github.com/unplugstudio/mezzanine-announcements/commit/0622ecc82466546b525812f1947987c5daa472b4))
* remove jQuery dependency ([2e5ecf4](https://github.com/unplugstudio/mezzanine-announcements/commit/2e5ecf4763751c0889a693021abfd4d6256fb059))


* fix template choices ([c815417](https://github.com/unplugstudio/mezzanine-announcements/commit/c8154172ad9d5aec41ded08e0478f2515de22bec))
* remove south migrations ([ff85b98](https://github.com/unplugstudio/mezzanine-announcements/commit/ff85b989d31a516dd99dc2a3e5df971632cb604c))

### [1.0.1](https://github.com/unplugstudio/mezzanine-announcements/compare/v1.0.0...v1.0.1) (2020-04-02)


### Bug Fixes

* fix JSON view ([2f362fe](https://github.com/unplugstudio/mezzanine-announcements/commit/2f362fe4d58a3f4705a1c9a8011ac2afbd4d4ea6))

## 1.0.0 (2020-04-02)


### Features

* allow adding fields to the admin from settings ([3bd327b](https://github.com/unplugstudio/mezzanine-announcements/commit/3bd327becb0bf3a384f2e02c5b8d75fe3eece542))
* allow RichText widgets in content fields ([82c7e73](https://github.com/unplugstudio/mezzanine-announcements/commit/82c7e73a5892bdaa3539de3449247f95d3205519))
* deprecate video setting ([b01fa2a](https://github.com/unplugstudio/mezzanine-announcements/commit/b01fa2aa85bafc76c8c17186952d70b1f5e0ee8f))
