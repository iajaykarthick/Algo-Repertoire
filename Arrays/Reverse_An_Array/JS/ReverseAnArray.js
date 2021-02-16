const readline = require('readline');

var getUserInput = function(callback){
    
    var arr = new Array();

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
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
                callback(arr);
            }
            else {
                rl.close();
                callback(arr);
            }
        });
    });

}

var reverseAnArray = function(arr, start = null, end = null){
    start = start || 0;
    end = end || arr.length-1;
    while (start < end) {
        [arr[start], arr[end]] = [arr[end], arr[start]]; // Swapping using es6(ES2015) Destructuring assignment
        start++;
        end--;
    }
}

var printArray = function(arr){
    console.log(arr.toString());
}


module.exports = {
    getUserInput: getUserInput,
    reverseAnArray: reverseAnArray,
    printArray: printArray
}