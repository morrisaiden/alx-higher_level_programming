#!/usr/bin/node
module.exports = {
    callMeMoby: function (q, r) {
	for (let i = 0; i < q; i++) {
	    r();
	}
    }
};
