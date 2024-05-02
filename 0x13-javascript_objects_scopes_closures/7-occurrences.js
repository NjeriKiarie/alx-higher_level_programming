#!/usr/bin/node
#!/usr/bin/node
/**
 * function that returns number of occurrences in a list
 * @param {list} list - list ti examine
 * @param {number} searchElement - element to search for
 * @returns {number} - the number of occurrences in a list
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((item) => {
    if (item === searchElement) {
      count++;
    }
  });
  return count;
};
// alternative of the arrow function
// list.forEach(function (item) {
//   if (item === searchElement) {
//     i++;
//   }
// });
