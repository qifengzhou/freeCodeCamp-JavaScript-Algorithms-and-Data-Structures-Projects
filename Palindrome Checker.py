function palindrome(str) {
  // Good luck!
  var newStr = str.replace(/[^a-z0-9]/gi,'').toLowerCase();
  var len = newStr.length;
  for (var i = 0; i <= Math.floor(len/2); i++) {
    if (newStr[i] !== newStr[len-1-i]) {
        return false;
    }
  }
  return true;
}



palindrome("eye");
