var kvArray = [
        [1, "I"],
        [4, "IV"], 
        [5, "V"],
        [9, "IX"], 
        [10, "X"], 
        [40, "XL"], 
        [50, "L"], 
        [90, "XC"], 
        [100, "C"],
        [400, "CD"], 
        [500, "D"], 
        [900, "CM"], 
        [1000, "M"]
        ];
var newArray = kvArray.reverse();

function convertToRoman(num) {
    var result = '';
    for (let i = 0; i < newArray.length; i++) {
        const [key, char] = newArray[i];
        if (num >= key) {
            while (num >= key) {
                num -= key;
                result += char;
            }
        }
    }
    return result;
}



convertToRoman(36);
