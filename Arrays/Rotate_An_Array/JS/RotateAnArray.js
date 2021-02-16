const readline = require('readline');
const reverse = require('../Reverse_An_Array/ReverseAnArray');

function getUserInput(callback){

    reverse.getUserInput((arr) => {
        
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

        rl.question('Enter the number of rotations ', (num_rotations) => {
            rl.question('Select Left / Right (L/R)?: ', (choice) => {
                rl.close();
                callback(arr, num_rotations, choice);
            });
        });
    });

}

function rotateAnArray(arr, a_end, b_start){
    // defining callback function to rotate the user entered array which is passed to this function as parameter
    reverse.reverseAnArray(arr, 0, a_end);
    reverse.reverseAnArray(arr, b_start, arr.length - 1)
    reverse.reverseAnArray(arr);
    reverse.printArray(arr);
}

 



 module.exports = {
    getUserInput: getUserInput,
    rotateAnArray: rotateAnArray
 } 