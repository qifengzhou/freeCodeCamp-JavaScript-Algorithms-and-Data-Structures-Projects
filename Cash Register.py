const money = [
  [100, 'ONE HUNDERD'],
  [20, 'TWENTY'],
  [10, 'TEN'],
  [5, 'FIVE'],
  [1, 'ONE'],
  [0.25, 'QUARTER'],
  [0.1, 'DIME'],
  [0.05, 'NICKEL'],
  [0.01, 'PENNY']
];

function checkCashRegister(price, cash, cid) {
  var changes = cash - price;
  var changeNum = [];
  var res = {status: "", change: []};
  var total = 0;
  for (let i = 0; i < cid.length; i++) {
    total += cid[i][1];
  }
  if (changes > total) {
    res.status = "INSUFFICIENT_FUNDS";
    return res;
  }

  if (changes == total) {
    res.status = "CLOSED";
    res.change = cid;
    return res;
  }

  var newcid = cid.reverse();

  for (let i = 0; i < money.length; i++) {
    const [key, char] = money[i];
    if (changes >= key && newcid[i][1] > 0) {
      var tochange = 0;
      while (changes >= key && newcid[i][1] > 0) {
        changes -= key;
        tochange += key;
        newcid[i][1] -= key;
        changes = Math.round(changes * 100)/100;
      }
      changeNum.push([char, tochange]);
    }
  } 
   
  if (changes == 0) {
    res.status = "OPEN";
    res.change = changeNum;
    return res;
  } 
  else {
    res.status = "INSUFFICIENT_FUNDS";
    return res;
  }

}

// Example cash-in-drawer array:
// [["PENNY", 1.01],
// ["NICKEL", 2.05],
// ["DIME", 3.1],
// ["QUARTER", 4.25],
// ["ONE", 90],
// ["FIVE", 55],
// ["TEN", 20],
// ["TWENTY", 60],
// ["ONE HUNDRED", 100]]

checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);
