#!/usr/bin/node
/**
 * function that gives the reversed version of a list
 * @param {list} list - list to examine
 * @returns {number} - the reversed version of a list
 */
exports.esrever = function (list) {
  const newList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
