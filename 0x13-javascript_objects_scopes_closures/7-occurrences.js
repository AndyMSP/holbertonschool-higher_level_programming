#!/usr/bin/node

function nbOccurences (list, target) {
  const valid = list.filter((val) => val === target);
  const len = valid.length;
  return (len);
}

module.exports = { nbOccurences };
