var VERSION_REGEX = /\d+\.\d+\.\d+/

module.exports.readVersion = function (contents) {
	return contents.match(VERSION_REGEX)[0]
}

module.exports.writeVersion = function (contents, version) {
	return contents.replace(VERSION_REGEX, version)
}
