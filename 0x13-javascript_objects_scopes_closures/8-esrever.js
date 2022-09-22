#!/usr/bin/node

exports.esrever = function (list) {
  let i, j;
  const len = list.length;
  const rev = [];
  for (i = 0, j = len - 1; j >= 0; i++, j--) {
    rev[i] = list[j];
  }
  return (rev);
};
