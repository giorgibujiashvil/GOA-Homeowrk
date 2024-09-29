//1) შექმენით ჯავასკრიპტში ობიექტი, ობიექტის სახელია me დაამატეთ კუთვნილებები რომელიც დაახასიათებს თქვენს თავს,
//შექმნის შემდეგ შეცვალეთ რომელიმე კუთვნილება, დაამატეთ ახალი კუთვნილება და წაშალეთ,
//საბოლოოდ კი დაბეჭდეთ მთლიანი ობიექტი  და დაბეჭდეთ ცალ-ცალკე ყველა კუთვნილება
const me = {
    name : "girogi",
    age : 15,
    city : "tbilisi"
}


me.city = "kvareli"
me.weight = "60gk"
delete me.weight

console.log(me)

console.log("name",me.name)
console.log("age",me.age)
console.log("city",me.city)


//2) შექმენით ობიექტი სადაც
//დაამატებთ მინიმუმ 5 კუთვნილებას და 2 მეთოდს, კომენტარებით ახსენით რა არის ობიექტი რა არის მეთოდი რა არის this keyword 
//და ყველაფერი ის რაც ვისწავლეთ: კუთვნილებები,. შეცვლა წაშლა დამატბეა

const cars = {
    marka: "mercedes",
    model: "cls 63",
   year : "2020",
   color : "green",
    //A method is a function created in an object
    printInfo: function() {
       console.log("BMW,Frerrari,")//method
   },

    nameInfo() {
        console.log(this.marka)
    }
}

//The method was printed/cars.printInfo()
cars.color = "black"
cars.country = "german"
delete cars.year




//3) შექმენიტ კონსტრუქტორი რომელიც შექმნის ერთი და იგივე სტრუქტურის მქონე ობიექტებს,
//აწარმოეთ კონსტრუქტორით რობოტები,
//გამოიძახეთ კონსტრუქტორი 3 ჯერ და ახსენით თქვენი სიტყვებით რა არის კონსტურტქორი და new

function car(name,model,yerar) {
              //კონსტრუქტორის გამოყენებით ობიექტში დავამატეთ მთოდი
    this.nmae = name;
    this.model = model;
    this.yerar = year;
              //კონსტრუქტორი არის ფუნქცია რომელიც ქმნის ობიექტს
    this.printInfo = function() {
        confirm.log(this.name, this.model, this.year)
    }
}
             //new შექმნის ახალ ცარიელ ობიექტს რომელსაც გადასცემს კონსტრუქტორს შემდეგ კი კონსტრუქტორი ამ ცარიელ ობიექტის ინიციალიზებას ანუ კუთვნილებების მინიჭებას
const car1 = new car("BMW","F90", 2022)

car1.printInfo()





