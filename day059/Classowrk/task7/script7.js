function generateEven(border) {
    const numbers = [];
    
    for (let num = 0; num <= border; num++) {
        numbers.push(num);
    }
    
    const evenNumbers = numbers.filter(num => num % 2 === 0);
    
    const totalSum = evenNumbers.reduce((sum, num) => sum + num, 0);
    
    return totalSum;
}


const borderValue = 10;
const result = generateEven(borderValue);
console.log(`The sum of even numbers from 0 to ${borderValue} is: ${result}`);


