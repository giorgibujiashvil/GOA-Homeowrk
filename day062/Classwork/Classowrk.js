//1)შექმენით მასივი რომელშიც ჩაამატებთ ყველა რიცხვს 0-იდან 100-ის ჩათვლით,
//შემდეგ მასივზე კიდევ იმუშავებთ for ციკლით და ყველა ლუწი რიცხვის ჯამს გამოიტანთ

let arr = [];
for(let i =0; i < 100; i++){
    arr.push(i)
}

let evenSum = 0;
for (let i = 0; i < evenSum.length; i++){
    if(i % 2 === 0){
        evenSum += i;
    }
}


console.log(evenSum)
//2)შექმენით მასივი სცადეთ კონსოლში გამოიტანოთ ისეთ ინდექსზე მყოფი ელემენტი რომელიც არ გაქვს მასივში

const Arr = ("giorgi","dato")
console.log(Arr[5])


//3)ყველა ახალ ნასწავლი მეთოდის გამოყენებით შექმენით თითოეულ ატგანზე 2-2 მაგალითი
//და ახსენით კომენტარებით თქვენი სიტყვებით თუ რას აკეთებს თითოეული მეთოდი (push,pop,unshift,shift, slice, splice)

//shift
myArr = [1,2,3];
myArr.shift()

console.log(myArr)


//shift2
myArr = [1,4,7];
myArr.shift()

console.log(myArr)


//unshift1
myArr = [12,3,5,6,]
myArr.unshift()

console.log(myArr)


//unshift2
myArr = [45,7,9,1,10]
myArr.unshift()

console.log(myArr)


//splice1

myArr = [1,2,3,4,5,6,7,8,9,10]
myArr.splice(2,5,12,13)

console.log(myArr)

//splice2

myArr = ["giorgi","dato","nika","ilia"]
myArr.splice(1,2,"lado","givi")

console.log(myArr)


//push1
const fruits = ["pinallpe", "Orange", "Apple", "wathhermellon"];
fruits.push("Kiwi");

console.log(fruits)

//push2

const car = ["BMW","Mercedes","Bugatti"]
car.push("Ferrari")

console.log(Fruits)


//pop1

const Telephone = ["iphone","hoco","samsung"]
Telephone.pop()

console.log(Telephone)

//pop2
const subjects = ["sport","english","math"]
subjects.pop()

console.log(subjects)


//slice1
let text = "Apple, orange, Kiwi";
let part = text.slice(7, 13);

//slice2
let Car = "BMW, Mercedes, Audi";
let Cars = Text.slice(8, 12);

console.log(Cars)










//4)შექმენით ფუნქცია სახელად manualSlice რომელსაც გადაეცემა პირველი მასივი, და ორი რიცხვი საწყისის ინდექსი და დასდასრულის ინდექსი,
//თქვენიო დავალებაა გადმოცემული ინდექსიდან მეორე ინდექსამდე ჩამოაჭრათ სიას ნაწილი და დააბრუნოთ ფუნქციიდან გამოიყენეთ for ციკლი

function manualSlice(array,startindex,endindex) {
    const listn = [];
    for(let i = array; startindex < endindex; i++)
       listn.push(i)
}


//5)შექმენით ფუნქცია სახელად manualReverse რომესლაც გადმოეცემა სია, და უნდა დააბრუნოთ შემოტრიალებული ვერსია სიის
function manualReverse(arr) {
    let reversedArray = [];
    for (let i = arr.length - 1; i >= 0; i--) {
        reversedArray.push(arr[i]);
    }
    return reversedArray;
}

// მაგალითი
const originalArray = [1, 2, 3, 4, 5];
const reversedArray = manualReverse(originalArray);
console.log(reversedArray);




//6)შექმენით ფუნქცია სახელად manualIndexOf რომელსაც გადაეცემა მნიშნელობა და სია, თქვენი დავალებაა ფუნქციიდან დააბრუნოთ ნაპოვნი მნბიშნელობის ინდექსი,
//თუ გადმოცემული მნიშნელობა სიაში არ მოიძებნა დააბრუნეთ -1
function manualIndexOf(value, arr) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === value) {
            return i; 
        }
    }
    return -1;  
}

// მაგალითი
const myArray = [10, 20, 30, 40, 50];
console.log(manualIndexOf(30, myArray)); 
console.log(manualIndexOf(60, myArray));





//7)გააკეთეთ 3-3 მაგალითი შესწავლილ მეთოდებზე: .indexOf(), .lastIndexOf(),.sort(),.reverse() და ახსენით რას აკეთებს თითოეული კომენტარებით

//1):indexOf()
let textt = "Hello world, welcome to the universe.";
let result = text.indexOf("Welcome");

//2)indexOf()
let texxt = "Hello world, welcome to the universe.";
text.indexOf("e", 5);

//3)indexOf()
let texttt = "Hello world, welcome to the universe.";
text.indexOf("a");


//1lastIndexOf()

let teext = "Hello planet earth, you are a great planet.";
let resultt = text.lastIndexOf("planet");

//2)lastIndexOf()

let ttext = "Hello planet earth, you are a great planet.";
let resul = text.lastIndexOf("you");

//3)lastIndexOf()

let tex = "Hello great planet earth, you are a great planet.";
let resutat = text.lastIndexOf("great");


//1)sort

const fruitss = ["Banana", "Orange", "Apple", "Mango"];
fruits.sort();

//2)sort

const fruitts = ["wathermalon", "pinaple", "Apple", "Mango"];
fruits.sort();

//3)sort

const fruiits = ["Banana", "Orange", "Apple", "Mango"];
fruits.sort();


//1)reverse

const fruuits = ["Banana", "Orange", "Apple", "Mango"];
fruits.reverse();

//2)reverse

const ffruits = ["Orange", "Apple", "Mango"];
fruits.reverse();

//3)reverse

const frruits = ["Banana", "Orange"];
fruits.reverse();



