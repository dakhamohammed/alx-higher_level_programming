#!/usr/bin/node

exports.converter = function (base) {
  const convert = (number) => number.toString(base);
  return convert;
};
