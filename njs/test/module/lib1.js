function hash() {
    var h = crypto.createHash('md5');
    var v = h.update('AB').digest('hex');
    return v;
}

import crypto from 'crypto';

var state = {count:0}

function inc() {
	state.count++;
}

function get() {
	return state.count;
}

export default {hash, inc, get};
