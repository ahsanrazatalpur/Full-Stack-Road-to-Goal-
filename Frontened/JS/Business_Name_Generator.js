// create a businees name generator by combining list of list of adjective and another word

// Adjective
//Crazy
//Amazing
//Fire


// Shop name:
// Engine 
// Foods
// Garments

// // Another Word 
// Bros
// limited
// Hub

// lets generate first name

let rand = Math.random();
let first ,second ,third;

if(rand < 0.33){
    first = 'Fire';
}else if(rand >0.33 && rand < 0.66){
    first = 'Foods';
}
else{
    first = 'Garment'
}

//Second name generator

if(rand < 0.33){
    second = 'Bros';
}else if(rand >0.33 && rand < 0.66){
    second = 'Limited';
}
else{
    second = 'Hub'
}

//Third name generator

if(rand < 0.33){
    third = 'Crazy';
}else if(rand >0.33 && rand < 0.66){
    third = 'Amazing';
}
else{
    third = 'Fire'
}

console.log(first +" "+ second +" "+ third)