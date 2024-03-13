#!/usr/bin/node
module.exports = {
    addMeMaybe: function (q, r) {
	return r(q + 1);
    }
};
