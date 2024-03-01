#!/usr/bin/node

exports.addMeMaybe = function addMeMaybe (number, theFunction) {
  nb = number + 1;
  theFunction (nb);
}
