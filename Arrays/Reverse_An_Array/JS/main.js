const reverse = require('./ReverseAnArray');


// get the inputs from user , reverse them and print them via callback function
reverse.getUserInput((arr) => {
    reverse.reverseAnArray(arr);
    reverse.printArray(arr);
});
