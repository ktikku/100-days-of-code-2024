/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function (n) {
  // base condition
  if (n === 1)
    return true
  if (n === 4)
    return true
  if (n < 4)
    return false
  return isPowerOfFour(n / 4)
};