/*
Created on Thu Aug 12 12:29:00 2021

@author: Fabrizio Romano
transcript: SCelis

switch / case , that in Python is missing.
It is the equivalent of a cascade of if / elif /.../ elif / else clauses

# switch.js

*/
/* switch.js */
switch (day_number) {
    case 1:
        day = "Monday";
        break;
    case 2:
        day = "Tuesday";
        break;
    case 3:
        day = "Wednesday";
        break;
    case 4:
        day = "Thursday";
        break;
    case 5:
        day = "Friday";
        break;
    case 6:
        day = "Saturday";
        break;
    case 0:
        day = "Sunday";
        break;
    default:
        day = "";
        alert(day_number + ' is not a valid day number.');
}
/* ór in this case From 1 to 5 there is a cascade, which means no matter the number, 
[ 1 , 5 ] all go down to the bit of logic that sets day as
"Weekday" . */
switch (day_number) {
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        day = "Weekday";
        break;
    case 6:
        day = "Saturday";
        break;
    case 0:
        day = "Sunday";
        break;
    default:
        day = "";
        alert(day_number + ' is not a valid day number.')
}