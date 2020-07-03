const _ = {
    clamp (num, lower, upper) {
        const lowerClampedValue = Math.max(num, lower);
        return Math.min(lowerClampedValue, upper);
    },
    inRange (num, lower, upper) {
        if (upper == null) {
            upper = lower;
            lower = 0;
        };
        if (upper < lower) {
            let temp = lower;
            lower = upper;
            upper = temp;
        };
        
        if (num >= upper) {
            return false;
        } else if (num < lower) {
            return false;
        } else {
            return true;
        };
    },
    words (string) {
        return string.split(' ')
    },
    pad (string, length) {
        let padding = length - string.length;
        let string_list = string.split();
        while (padding > 0) {
            string_list.push(' ');
            padding --;
            if (padding > 0) {
                string_list.unshift(' ');
                padding --;
            };
        }
        return string_list.join('');
    },
    has (obj, key) {
        if (obj[key] == null) {
            return false;
        } else {
            return true;
        };
    },
    invert (obj) {
        const keys = Object.keys(obj);
        let new_obj = {};
        for (let i = 0; i < keys.length; i++) {
            let temp = obj[keys[i]];
            new_obj[temp] = keys[i];
        };
        return new_obj;
    }
};




// Do not write or modify code below this line.
module.exports = _;