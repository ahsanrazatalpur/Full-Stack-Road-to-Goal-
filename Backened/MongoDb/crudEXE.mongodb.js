// Creating Database
use("First")

//Creating collection
db.createCollection("Second")

// CRUD operation

//Create
//create one docs with object
db.Second.insertOne(
    {Name : "Ahsan Raza",Fname : "Amir Ali",age : 20, Department : "Computer Science"}
)

//create many docs with an Array
db.Second.insertMany[
    {   'Name' : "Ahsan Raza", 
        "Age"  : 20,
        "Deparment" : "Computer Science"
    },
    {   'Name' : "Alee Raza", 
        "Age"  : 25,
        "Deparment" : "Computer Science Graduate"
    },
    {   'Name' : "Mehdi Raza", 
        "Age"  : 18,
        "Deparment" : "Doctor Physiology"
    }
    
    
]

// Read
let ex = db.Second.find({age  : 20})
console.log(ex)

let ex2 = db.Second.findOne({Name : "Ahsan Raza"})
console.log(ex2)

// to count
console.log(Age.count())

// to print
console.log(name.toArray())


//Update

// update one
db.Second.updateOne({age : 20},{$set: {age : 22}})

// update Many
db.Second.updateMany({age : 20},{$set: {age : 22}})

// Delete 

//Delete One 
db.Second.deleteOne({age : 20})

//Delete Many
db.Second.deleteMany({age : 20})