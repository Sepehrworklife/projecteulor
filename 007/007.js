/*
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 * What is the 10 001st prime number?
 */

// Check if the number is prime
function isPrime(n){
	if ( n === 1 ) return false;
	for ( var i = 2; i < n; i++ ) {
		if ( n % i === 0 ) return false;
	}
	return true;
}

// Find index of prime number
function nth_prime(n){
	var count = 0;
	var i = 1;
	while ( count < n ) {
		i++;
		if ( isPrime(i) ) count++;
	}
	return i;
}


// Check if answer is correct
console.log(`The 10001st prime number is ${nth_prime(10001)}.`);
