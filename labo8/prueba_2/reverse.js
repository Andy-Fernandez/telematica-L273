
// En este caso estamos exportando una función que recibe un string y lo devuelve al revés.
function reverse(str) {
  return str.split('').reverse().join('');
}

module.exports = reverse;
