// Author: Abdulrahman Jouhari
// Date: July 3, 2020
// Project: Re-creating the Lodash Library

// Instructions: Make a lodash implementation with these 10 functions:
// clamp, inRange, words, pad, has, invert, findKey, drop, dropWhile, chunk.
// The functionalities of the methods can be found at https://lodash.com/docs/4.17.15

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
    },
    findKey (obj, func) {
        const keys = Object.keys(obj);
        for (let i = 0; i < keys.length; i++) {
            if (func(obj[keys[i]]) == true) {
                return keys[i];
            };
        };
        return undefined;
    },
    drop (arr, num) {
        if (num == null) {
            num = 1;
        };
        for (let i = 0; i < num; i++) {
            arr.shift();
        }
        return arr;
    },
    dropWhile (arr, func) {
        while (func(arr[0], 0, arr)) {
            arr.shift();
        };
        return arr;
    },
    chunk (arr, size) {
        if (size == null) {
            size = 1;
        };
        let new_arr = [];
        let start = 0;
        while (start < arr.length) {
            if (start + size <= arr.length) {
                let sec = arr.slice(start, start + size);
                new_arr.push(sec);
            } else {
                size = arr.length;
                let sec = arr.slice(start, size);
                new_arr.push(sec);
            };
            start += size;
        }
        return new_arr;
    }
};




// Do not write or modify code below this line.
module.exports = _;