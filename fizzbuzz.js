// SOLVED: FizzBuzz Challenge.
for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        document.write("<p class='text-center'>" + i + " | FizzBuzz" + "</p>");
    } else if (i % 3 === 0) {
        document.write("<p class='text-center'>" + i + " | Fizz" + "</p>");
    } else if (i % 5 === 0) {
        document.write("<p class='text-center'>" + i + " | Buzz" + "</p>");
    } else {
        document.write("<p class='text-center'>" + i + "</p>");
    }
}


function fizzbuzz(range_num, first_num, second_num) {
    for (let i = 1; i <= range_num; i++) {
        if (i % first_num === 0 && i % second_num === 0) {
            document.write("<p class='text-center'>" + i + " | FizzBuzz" + "</p>");
        } else if (i % first_num === 0) {
            document.write("<p class='text-center'>" + i + " | Fizz" + "</p>");
        } else if (i % second_num === 0) {
            document.write("<p class='text-center'>" + i + " | Buzz" + "</p>");
        } else {
            document.write("<p class='text-center'>" + i + "</p>");
        }
    }
}

fizzbuzz(200, 5, 8);