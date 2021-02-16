const rotation = require('./RotateAnArray');

rotation.getUserInput((arr, num_rotations, choice) => {
    num_rotations = num_rotations.trim() || 0
    choice = ( choice.toUpperCase() != "L" ) && ( choice.toUpperCase() != "R" ) ?  "L" : choice
    console.log(choice)
    var a_end, b_start;
    if ( choice.toUpperCase() == "L" ) {
        a_end = num_rotations - 1;
        b_start = num_rotations;
    } else if ( choice.toUpperCase() == "R" ) {
        a_end = arr.length - num_rotations - 1;
        b_start = arr.length - num_rotations;
    }
    rotation.rotateAnArray(arr, a_end, b_start);
});