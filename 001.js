
        let sum = 0;
        let numbersMultiples = [];
        for (let i = 1; i < 1000; i++) {
            if (i % 3 === 0 || i % 5 === 0) {
                numbersMultiples.push(i);
                sum += i;
            }
        }
        console.log(numbersMultiples);
        console.log(sum);

