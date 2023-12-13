#!/usr/bin/node

exports.converter = function (base) {
  return convert = (number) => number.toString(base);
};
