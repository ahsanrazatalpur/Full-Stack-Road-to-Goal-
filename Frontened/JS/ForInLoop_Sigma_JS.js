// for in loop
let obj = {
    name : "Ahsan",
    Dept : "Computer Science",
    company : "TechnoClone"
}

for(const key in obj){
    const element = obj[key];
    console.log(key,element);
}

let bio ={
    
    student1 : "Ahsan",
    student2 : "Ali",
    student3 : "Ayaz",
    student4 : "Gull",
}
for(const names in bio){
    element = bio[names]
console.log(names,element)    
}
