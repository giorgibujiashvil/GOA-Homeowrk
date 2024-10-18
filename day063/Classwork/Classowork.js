//1)შექმენით ფუნქცია სახელად manualFilter რომელსაც პირველი გადაეცემა ფუნქცია და მეორე მასივი, ამ ფუნქციაში უნდა გამოიყენოთ for ციკლი და გადაუარეთ გადმოცემულ მასივს, გამოიყენეთ if და გამოიძახეთ გადმოცემული ფუნქცია ამჟამინდელ ინდექსზე მდგომი მნიშნელობით, თუ დაბრუნებული მნიშნელობა არის true დაამატეთ ახალ მასივში და თუ არის false არ დაამატოთ ახალ მასივში, როცა მორჩება for ციკლის მუშაობა დააბრუნეთ ახალი მასივი=, გადაცემული ფუნქციიდან აუცილებლად უნდა ბრუნდებოეს boolean მნიშვნელობა, და უნდა იღებდეს ერთ მნიშნელობას გადაცემულ ფუნქციაში რას შეამოწმებთ თქვენზეა დამოკიდებული

function manualFilter(callback, array) {
    const newArray = [];
    for (let i = 0; i < array.length; i++) {
        if (callback(array[i])) {
            newArray.push(array[i]);
        }
    }
    return newArray;
}


const numbers = [1, 2, 3, 4, 5];
const isEven = (num) => num % 2 === 0;

const evenNumbers = manualFilter(isEven, numbers);
console.log(evenNumbers); 



//2)გააკეთეთ 5 მაგალითი თითოეულ მათემატიკური ობიექტის მეთოდზე რომლებიც ვისწავლეთ: sqrt,ceil,floor,trunc,pow,abs,min,max

//Math.sqrt()
console.log(Math.sqrt(16)); 
console.log(Math.sqrt(25)); 
console.log(Math.sqrt(2));  
console.log(Math.sqrt(0));  
console.log(Math.sqrt(-9));


//Math.ceil()
console.log(Math.ceil(4.2)); 
console.log(Math.ceil(7.8)); 
console.log(Math.ceil(-3.1)); 
console.log(Math.ceil(5));    
console.log(Math.ceil(-5.9));


//Math.floor()
console.log(Math.floor(4.9)); 
console.log(Math.floor(7.1)); 
console.log(Math.floor(-3.5)); 
console.log(Math.floor(5));    
console.log(Math.floor(-5.1));



//Math.trunc()

console.log(Math.trunc(4.9)); 
console.log(Math.trunc(-7.8)); 
console.log(Math.trunc(3.14)); 
console.log(Math.trunc(-5.99)); 
console.log(Math.trunc(0));


//Math.pow()

console.log(Math.pow(2, 3)); 
console.log(Math.pow(5, 2)); 
console.log(Math.pow(10, 0)); 
console.log(Math.pow(3, 4)); 
console.log(Math.pow(-2, 3));


//Math.abs()

console.log(Math.abs(-5));   
console.log(Math.abs(5));    
console.log(Math.abs(-3.14)); 
console.log(Math.abs(0));     
console.log(Math.abs(-10));


//Math.min()

console.log(Math.min(1, 2, 3)); 
console.log(Math.min(-1, -2, -3)); 
console.log(Math.min(5, 10, 0)); 
console.log(Math.min(100, 50, 25)); 
console.log(Math.min(-5, 0, 5));


//Math.max()

console.log(Math.max(1, 2, 3)); 
console.log(Math.max(-1, -2, -3)); 
console.log(Math.max(5, 10, 0)); 
console.log(Math.max(100, 50, 25)); 
console.log(Math.max(-5, 0, 5));




//3)შექმენით ინეტრვალი, გადაცემულ ფუნციაში ყოველ ჯერზე შექმენით date ობიექტი, როცა ამჟამინდელი წუთი გაუტოლდება 35, უნდა გაითიშოს ინეტრვალი

function startInterval() {
    const intervalId = setInterval(() => {
        const now = new Date();
        const minutes = now.getMinutes();

        console.log(`ამჟამინდელი წუთი: ${minutes}`);

        if (minutes === 35) {
            clearInterval(intervalId);
            console.log("ინტერვალი გაწვდილია, რადგან minute 35 გახდა.");
        }
    }, 1000); 
}

startInterval();



//4)შექმენით date ობიექტი, რომელიც შეინახავს ახლანდელ დროს, შემდეგ გამოიტანეთ ამ ობიექტის კუთვნილებები ნასწავლი მეთოდების საშვალებით:
//getFullYear(), getMonth(), getDate(), getDay(), getHours(), getMinutes(), getSeconds(), get Millieseconds()

const now = new Date();

// Date ობიექტის კუთვნილებების გამოყვანა
const year = now.getFullYear(); 
const month = now.getMonth(); 
const date = now.getDate(); 
const day = now.getDay(); 
const hours = now.getHours(); 
const minutes = now.getMinutes(); 
const seconds = now.getSeconds(); 
const milliseconds = now.getMilliseconds(); 


console.log(`წელი: ${year}`);
console.log(`თვე: ${month + 1}`); 
console.log(`დღე: ${date}`);
console.log(`კვირის დღე: ${weekday}`);
console.log(`საათი: ${hours}`);
console.log(`წუთი: ${minutes}`);
console.log(`წამი: ${seconds}`);
console.log(`მილიწამი: ${milliseconds}`);



//5)შექენით 2 date ობიექტი რომელთა დროის კუთვნილებებს გამოიტანთ ნასწავლი get მეთოდებით, ობიექტებს არგუმენტებად უნდა გადასცეთ სტრინგები შემდეგი ფორმატით:
//პირველს: "2022-03-25",
//მეორეს: "October 13, 2014 11:13:00"

const date1 = new Date("2022-03-25");
const date2 = new Date("October 13, 2014 11:13:00");


console.log("პირველი თარიღი (2022-03-25):");
console.log(`წელი: ${date1.getFullYear()}`);
console.log(`თვე: ${date1.getMonth() + 1}`); 
console.log(`დღე: ${date1.getDate()}`);
console.log(`კვირის დღე: ${date1.getDay()}`);
console.log(`საათი: ${date1.getHours()}`);
console.log(`წუთი: ${date1.getMinutes()}`);
console.log(`წამი: ${date1.getSeconds()}`);
console.log(`მილიწამი: ${date1.getMilliseconds()}`);
console.log('');


console.log("მეორე თარიღი (October 13, 2014 11:13:00):");
console.log(`წელი: ${date2.getFullYear()}`);
console.log(`თვე: ${date2.getMonth() + 1}`);
console.log(`დღე: ${date2.getDate()}`);
console.log(`კვირის დღე: ${date2.getDay()}`);
console.log(`საათი: ${date2.getHours()}`);
console.log(`წუთი: ${date2.getMinutes()}`);
console.log(`წამი: ${date2.getSeconds()}`);
console.log(`მილიწამი: ${date2.getMilliseconds()}`);