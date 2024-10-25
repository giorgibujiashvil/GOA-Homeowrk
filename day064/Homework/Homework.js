//task 1)   განიხილეთ ეს ამოცანა და მოიფიქრეთ ალტერნატივა~

function findLongest(array){
    let mostDigitNumber = array[0]
    let mostDigit = 0
    
    for(let i = 0; i < array.length; i++){
      const currentNumber = array[i];
      const numberOfDigits = currentNumber.toString().length;
      
      if(mostDigit < numberOfDigits){
        mostDigit = numberOfDigits
        mostDigitNumber = currentNumber
      }
    }
    
    return mostDigitNumber
  }


//ალტერნატივა

function findLongest(array) {
    return array.reduce((longest, current) => {
      return current.toString().length > longest.toString().length ? current : longest;
    });
  }

  const numbers = [1, 22, 333, 4444];
console.log(findLongest(numbers));




//task 2) codewars



//codewar 1)
//You will be given an array which will include both integers and characters.

//Return an array of length 2 with a[0] representing the mean of the ten integers as a floating point number. There will always be 10 integers and 10 characters. Create a single string with the characters and return it as a[1] while maintaining the original order.

//lst = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0']
//Here is an example of your return

//[3.6, "udiwstagwo"]
///In C# and Java the mean return is a double.



function mean(lst) {

    const integers = [];
    const characters = [];
    
    lst.forEach(item => {
        if (!isNaN(item)) {
            integers.push(Number(item));
        } else {
            characters.push(item);
        }
    });
    
    
    const mean = integers.reduce((acc, num) => acc + num, 0) / integers.length;
    
  
    const concatenatedString = characters.join('');
    
   
    return [mean, concatenatedString];
}

const lst = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0'];
console.log(mean(lst));  



//codewar 2)

// Write a method that will search an array of strings for all strings that contain another string, ignoring capitalization. Then return an array of the found strings.

// The method takes two parameters, the query string and the array of strings to search, and returns an array.

// If the string isn't contained in any of the strings in the array, the method returns an array containing a single string: "Empty" (or Nothing in Haskell, or "None" in Python and C)

// Examples
// If the string to search for is "me", and the array to search is ["home", "milk", "Mercury", "fish"], the method should return ["home", "Mercury"].

function wordSearch(query, seq) {
    
    const lowerQuery = query.toLowerCase();
    
    
    const results = seq.filter(str => str.toLowerCase().includes(lowerQuery));
    
  
    return results.length > 0 ? results : ["Empty"];
}


console.log(wordSearch("me", ["home", "milk", "Mercury", "fish"])); 
console.log(wordSearch("test", ["apple", "banana", "grape"])); 
console.log(wordSearch("o", ["hello", "world", "home"]));





//codewar 3)

// A sequence or a series, in mathematics, is a string of objects, like numbers, that follow a particular pattern. The individual elements in a sequence are called terms. A simple example is 3, 6, 9, 12, 15, 18, 21, ..., where the pattern is: "add 3 to the previous term".

// In this kata, we will be using a more complicated sequence: 0, 1, 3, 6, 10, 15, 21, 28, ... This sequence is generated with the pattern: "the nth term is the sum of numbers from 0 to n, inclusive".

// [ 0,  1,    3,      6,   ...]
//   0  0+1  0+1+2  0+1+2+3
// Your Task
// Complete the function that takes an integer n and returns a list/array of length abs(n) + 1 of the arithmetic series explained above. Whenn < 0 return the sequence with negative terms.

// Examples
//  5  -->  [0,  1,  3,  6,  10,  15]
// -5  -->  [0, -1, -3, -6, -10, -15]
//  7  -->  [0,  1,  3,  6,  10,  15,  21,  28]

function sumOfN(n) {
    const result = [];
    const absoluteN = Math.abs(n);

    for (let i = 0; i <= absoluteN; i++) {
        const term = (i * (i + 1)) / 2; 
        result.push(n < 0 ? -term : term);
    }

    return result;
}

console.log(sumOfN(5));  
console.log(sumOfN(-5));
console.log(sumOfN(7)); 



//codewar 4)

// In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

// Examples
// highAndLow("1 2 3 4 5"); // return "5 1"
// highAndLow("1 2 -3 4 5"); // return "5 -3"
// highAndLow("1 9 3 4 -5"); // return "9 -5"
// Notes
// All numbers are valid Int32, no need to validate them.
// There will always be at least one number in the input string.
// Output string must be two numbers separated by a single space, and highest number is first.

function highAndLow(numbers) {
  
    const numArray = numbers.split(' ').map(Number);
    
   
    const highest = Math.max(...numArray);
    const lowest = Math.min(...numArray);
    
    
    return `${highest} ${lowest}`;
}


console.log(highAndLow("1 2 3 4 5"));       
console.log(highAndLow("1 2 -3 4 5"));      
console.log(highAndLow("1 9 3 4 -5"));



//codewar 5)

// Simple, given a string of words, return the length of the shortest word(s).

// String will never be empty and you do not need to account for different data types.

function findShort(s) {
    
    const words = s.split(' ');
    
    
    const minLength = Math.min(...words.map(word => word.length));
    
    return minLength;
}


console.log(findShort("The quick brown fox")); 
console.log(findShort("Lorem ipsum dolor sit amet")); 
console.log(findShort("I am the shortest"))


//codewar 6)


// Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

// If you want to know more: http://en.wikipedia.org/wiki/DNA

// In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

// More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

// Example: (input --> output)

// "ATTGC" --> "TAACG"
// "GTAT" --> "CATA"

function dnaStrand(dna) {
    
    const complement = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    };

    
    return dna.split('').map(base => complement[base]).join('');
}


console.log(dnaStrand("ATTGC")); 
console.log(dnaStrand("GTAT"));  


//codewar 7)


// Happy Holidays fellow Code Warriors!
// It's almost Christmas Eve, so we need to prepare some milk and cookies for Santa! Wait... when exactly do we need to do that?

// Time for Milk and Cookies
// Complete the function function that accepts a Date object, and returns true if it's Christmas Eve (December 24th), false otherwise.

// Keep in mind Javascript's Date month is 0 based!

// Examples
// timeForMilkAndCookies(new Date(2013, 11, 24))  
// timeForMilkAndCookies(new Date(2013, 0, 23))   
// timeForMilkAndCookies(new Date(3000, 11, 24))

function timeForMilkAndCookies(date) {
    // Check if the month is December (11) and the date is 24
    return date.getMonth() === 11 && date.getDate() === 24;
}

// Example usage
console.log(timeForMilkAndCookies(new Date(2013, 11, 24))); // true
console.log(timeForMilkAndCookies(new Date(2013, 0, 23)));  // false
console.log(timeForMilkAndCookies(new Date(3000, 11, 24))); // true




//codewar 8)

// Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

// For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

// Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

// Note: The function accepts an integer and returns an integer.

// Happy Coding!

function squareDigits(num) {
    return Number(num.toString().split('').map(digit => {
        const squared = Math.pow(Number(digit), 2); 
        return squared; 
    }).join('')); 
}


console.log(squareDigits(9119)); 
console.log(squareDigits(765));   



//codewar 9)

// Trolls are attacking your comment section!

// A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

// Your task is to write a function that takes a string and return a new string with all vowels removed.

// For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

// Note: for this kata y isn't considered a vowel.

function disemvowel(str) {
    return str.replace(/[aeiouAEIOU]/g, '');
}


console.log(disemvowel("This website is for losers LOL!")); 


//codewar 10)

// A square of squares
// You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

// However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

// Task
// Given an integral number, determine if it's a square number:

// In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

// The tests will always use some integral number, so don't worry about that in dynamic typed languages.

// Examples
// -1  =>  false
//  0  =>  true
//  3  =>  false
//  4  =>  true
// 25  =>  true
// 26  =>  false

var isSquare = function(n) {
    if (n < 0) return false;

    var sqrt = Math.sqrt(n);
    return sqrt * sqrt === n;
};


console.log(isSquare(-1));  
console.log(isSquare(0));   
console.log(isSquare(3));   
console.log(isSquare(4));   
console.log(isSquare(25));  
console.log(isSquare(26));  



//codewar 11)

// Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

// Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

// Example:

// Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
// Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"


String.prototype.toJadenCase = function () {
    return this.split(' ').map(word => {

        return word.charAt(0).toUpperCase() + word.slice(1);
    }).join(' ');
};


const quote = "How can mirrors be real if our eyes aren't real";
console.log(quote.toJadenCase());



//codewar 12)

// Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

// Note: a and b are not ordered!

// Examples (a, b) --> output (explanation)
// (1, 0) --> 1 (1 + 0 = 1)
// (1, 2) --> 3 (1 + 2 = 3)
// (0, 1) --> 1 (0 + 1 = 1)
// (1, 1) --> 1 (1 since both are same)
// (-1, 0) --> -1 (-1 + 0 = -1)
// (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
// Your function should only return a number, not the explanation about how you get that number.

function getSum(a, b) {
    const min = Math.min(a, b);
    const max = Math.max(a, b);
    
    const sum = ((max - min + 1) * (min + max)) / 2;
    
    return sum;
}


console.log(getSum(1, 0));   
console.log(getSum(1, 2));   
console.log(getSum(0, 1));   
console.log(getSum(1, 1));   
console.log(getSum(-1, 0));  
console.log(getSum(-1, 2));  


//codewar 13)

// Given an array, find the duplicates in that array, and return a new array of those duplicates. The elements of the returned array should appear in the order when they first appeared as duplicates.

// Note: numbers and their corresponding string representations should not be treated as duplicates (i.e., "1" != 1).

// Examples
// [1, 2, 4, 4, 3, 3, 1, 5, 3, "5"]  ==>  [4, 3, 1]
// [0, 1, 2, 3, 4, 5]                ==>  []


function duplicates(arr) {
    const seen = new Set();
    const duplicates = new Set();

    for (const item of arr) {
        if (seen.has(item)) {
            duplicates.add(item);
        } else {
            seen.add(item); 
        }
    }

    return Array.from(duplicates);
}


console.log(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, "5"])); 
console.log(duplicates([0, 1, 2, 3, 4, 5]));               


//codewar 14)

// Your task in this kata is to implement a function that calculates the sum of the integers inside a string. For example, in the string 
//"The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", the sum of the integers is 3635.

function sumOfIntegersInString(s) {
    const numbers = s.match(/\d+/g);
    
    if (!numbers) return 0;

    return numbers.map(Number).reduce((sum, num) => sum + num, 0);
}


const exampleString = "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog";
console.log(sumOfIntegersInString(exampleString)); 



//codewar 15)

// Task:
// Given a list of integers, determine whether the sum of its elements is odd or even.

// Give your answer as a string matching "odd" or "even".

// If the input array is empty consider it as: [0] (array with a zero).

// Examples:
// Input: [0]
// Output: "even"

// Input: [0, 1, 4]
// Output: "odd"

// Input: [0, -1, -5]
// Output: "even"

function oddOrEven(array) {
    const sum = array.reduce((acc, num) => acc + num, 0);
    
    return sum % 2 === 0 ? "even" : "odd";
}


console.log(oddOrEven([0]));           
console.log(oddOrEven([0, 1, 4]));     
console.log(oddOrEven([0, -1, -5]));    
console.log(oddOrEven([]));             



