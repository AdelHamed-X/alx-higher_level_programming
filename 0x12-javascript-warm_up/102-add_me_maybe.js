#!/usr/bin/node

exports.addMeMaybe = function addMeMaybe (number, theFunction) {
  const nb = number + 1;
  theFunction(nb);
};
