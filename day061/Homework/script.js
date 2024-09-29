//Task 1: Create a Basic Object Create an object representing a person with properties like name, age, and city.

const person = {
    name : "giorgi",
    age : "15",
    city : "kvareli"
}



//Task 2: Access Object Properties
//Create an object car with properties make, model, and year. Access and print each property.

const car = {
    make : "Ferrari",
    model: "La Ferrari",
    year : "2020"
}

console.log("make",car.make)
console.log("model",car.model)
console.log("year",car.year)



//Task 3: Modify Object Properties
//Take the person object from Task 1 and change the age property to a new value

const person1 = {
    name : "giorgi",
    age : 14
}

person1.age = 15


//Task 4: Add New Property
//Add a new property hobby to the person object from Task 1 and assign it a value.

const person2 ={
    name : "girogi",
    age : 15
}

person2.hobby = "programing"



//Task 5: Delete Property
//Delete the city property from the person object.

const person3 = {
    age : 15,
    city : "New york"
}

delete person3.city


//Task 6: Object Method
//Create an object calculator with properties a, b, and a method add() that returns the sum of a and b


const calculator = {
    a : 5,
    b : 15,
    add : function() {
        return this.a + this.b
    }
}

calculator.a = 5;
calculator.b = 3;

console.log(calculator.add())




//Task 7: Create Multiple Objects
//Create 3 different objects, each representing a different book. Each object 


function books(name,model,yerar) {
    //კონსტრუქტორის გამოყენებით ობიექტში დავამატეთ მთოდი
this.book1 = name1;
this.book2 = name2;
this.book3 = name3;
}

const book1 = new book1("To Kill a Mockingbird")
const book2 = new book2("F. Scott Fitzgerald")
const book3 = new book3("1984")




//Task 9: Constructor Function
//Write a constructor function Animal that creates an object with properties name and sound. Add a method makeSound() that prints the sound.

function animal() {
    this.name = name5;
    this.sound = sound;
    this.makesuound = function() {
        console.log(this.name5, this.sound)
    }

}

const dog = new animal("woof");
const cat = new animal("meow");
const buffalo = new animal("muuu");

dog.makesuound();
cat.makesuound();
buffalo.makesuound();


//Task 10: Create Objects with Constructor
//Use the Animal constructor to create two animals: a cat and a dog, each with their own sound.

function animal() {
    this.dog = dog;
    this.cat = cat;
}

const dogg = new animal("woof");
const ccat = new animal("meow")

console.log(this.dogg, this.ccat)





