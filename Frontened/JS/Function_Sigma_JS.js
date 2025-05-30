// Function in JS

// without function
console.log("hello, World");
console.log("hello, World");
console.log("hello, World");
console.log("hello, World");
console.log("hello, World");
console.log("hello, World");

// function
function Demo(){
console.log("hello, World function");
}
// Repeat these line just to recall function
Demo();
Demo();
Demo();
Demo();
Demo();
Demo();
Demo();

// paasing parameter
function cousins(name){
    console.log("My name is :"+name)
    console.log("My name is :"+name)
    console.log("My name is :"+name)
    console.log("My name is :"+name)
    console.log("My name is :"+name)
}
cousins("Ahsan Raza Talpur");

function Biography(name,age,dept){
    console.log("My name is "+name+" ,my age is "+age+" and my Department is "+dept);
}
    Biography("Ahsan Raza",20,"Computer Science");
    Biography("Alee Raza",25,"Graduate");
    Biography("Gull talpur",24,"Lecturare");
 
function sum(a , b){
    console.log(a + b);
} 
sum(10 , 15);
sum(100 , 200);
sum(5 , 9);

//function Math(a, b, c = 1){
 //    return a + b  +c;
  // console.log(result)
//}
//Math(10 ,20);

//Arrow Function
const name = (name) =>{
    console.log(name);
}
name("Ahsan");

const country = (country) =>{
    console.log('My country name is '+country);
}
country("Pakistan");
country("Turkey");
country("China");
