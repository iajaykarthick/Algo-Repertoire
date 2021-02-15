const readline = require('readline');

function reverseAnArray(){
    var start = -1;
    var end = arr.length;
    while (++start < --end) {
        [arr[start], arr[end]] = [arr[end], arr[start]]; // Swapping using es6(ES2015) Destructuring assignment
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  var arr = new Array();
  
  rl.question('Enter the number of elements in the array ', (answer) => {
    rl.on('line', (input) => {
        var nums = input.split(' ');
        for(var i = 0; i < nums.length; i++)
            arr.push(nums[i]);
        if (arr.length < answer) {
            console.log(`You have entered only ${arr.length} numbers. Please enter remaining ${answer-arr.length} numbers`);
        }
        else if (arr.length > answer) {
            console.log(`You have entered only more than ${answer} numbers. No Problem! I will reverse the entered array of numbers for you`);
            rl.close();     
        }
        else {
            rl.close();     
            reverseAnArray();
            console.log(arr.toString());
        }
    });
  });

