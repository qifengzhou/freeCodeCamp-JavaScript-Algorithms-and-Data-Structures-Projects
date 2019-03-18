const lookUp = new Map([
  ["A", "N"],
  ["B", "O"],
  ["C", "P"],
  ["D", "Q"],
  ["E", "R"],
  ["F", "S"],
  ["G", "T"],
  ["H", "U"],
  ["I", "V"],
  ["J", "W"],
  ["K", "X"],
  ["L", "Y"],
  ["M", "Z"],
  ["N", "A"],
  ["O", "B"],
  ["P", "C"],
  ["Q", "D"],
  ["R", "E"],
  ["S", "F"],
  ["T", "G"],
  ["U", "H"],
  ["V", "I"],
  ["W", "J"],
  ["X", "K"],
  ["Y", "L"],
  ["Z", "M"]
]);

function rot13(str) { // LBH QVQ VG!
  var len = str.length;
  var res = '';
  for (let i = 0; i < len; i++) {
    if (str[i].match(/[A-Z]/)) {
      res += lookUp.get(str[i]);
    }
    else {
      res += str[i];
    }
  }
  return res;
}

// Change the inputs below to test
rot13("SERR PBQR PNZC");
