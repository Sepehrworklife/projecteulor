/*
* If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
* Find the sum of all the multiples of 3 or 5 below 1000.
*/

function sumOfMultiples(limit) {
	var sum = 0;
	for (var i = 0; i < limit; i++) {
		if (i % 3 === 0 || i % 5 === 0) {
			sum += i;
		}
	}
	return sum;
}


// Test output with problem description if they match
console.log(`The sum of all the multiples of 3 or 5 below 10 is ${sumOfMultiples(10)}.`);
// Test the function with given input
console.log(`The sum of all the multiples of 3 or 5 below 1000 is ${sumOfMultiples(1000)}`);



