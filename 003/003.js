/*
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143 ?
 */


function primeFactors(n) {
	var factors = [];
	var divisor = 2;
	while (n > 2) {
		if (n % divisor === 0) {
			factors.push(divisor);
			n = n / divisor;
		} else {
			divisor++;
		}
	}
	const largest = factors.reduce((a, b) => Math.max(a, b));
	return largest
}


// Check if answer is correct
console.log(`The largest prime factor of 600851475143 is ${primeFactors(600851475143)}`);



