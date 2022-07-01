
        let n = 100000;
        let sum = 600851475143;
        nextPrime: for (let i = 2; i <= n; i++) {
            for (let j = 2; j < i; j++) {
                if (i % j === 0) continue nextPrime;
            }
            if (sum % i === 0) {
                console.log(i);
            }
        }
