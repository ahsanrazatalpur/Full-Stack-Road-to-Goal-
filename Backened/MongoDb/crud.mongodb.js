
use('CrudDb');

// console.log(db)  CrudDb

//Create

db.createCollection("cources") // to craete any collecttion through object

db.cources.insertOne( // to insert document in collection
    {   Name : "Ahsan raza",
        Age : 20,
        Dept : "Cs",
        Project : "Hotel_management"

    }
)

db.cources.insertMany(//create many document through Array
    [
  {
    "Name": "Ahsan Raza",
    "Age": 20,
    "Dept": "CS",
    "Project": "Hotel_management"
  },
  {
    "Name": "Sara Khan",
    "Age": 22,
    "Dept": "IT",
    "Project": "Ecommerce_platform"
  },
  {
    "Name": "Zain Malik",
    "Age": 21,
    "Dept": "SE",
    "Project": "Library_system"
  },
  {
    "Name": "Maria Ali",
    "Age": 23,
    "Dept": "CS",
    "Project": "Inventory_tracker"
  },
  {
    "Name": "Usman Tariq",
    "Age": 20,
    "Dept": "CE",
    "Project": "Smart_home"
  },
  {
    "Name": "Hira Nawaz",
    "Age": 22,
    "Dept": "IT",
    "Project": "Online_banking"
  },
  {
    "Name": "Ahmed Farooq",
    "Age": 24,
    "Dept": "CS",
    "Project": "Task_scheduler"
  },
  {
    "Name": "Fatima Noor",
    "Age": 21,
    "Dept": "SE",
    "Project": "Health_portal"
  },
  {
    "Name": "Bilal Qureshi",
    "Age": 23,
    "Dept": "CS",
    "Project": "Chatbot_assistant"
  },
  {
    "Name": "Noor Hassan",
    "Age": 22,
    "Dept": "CE",
    "Project": "Traffic_control_system"
  }
]
)

// Read  (Find)
let name = db.cources.find({Age : 20})
console.log(name)

console.log(name.count()) // to count

console.log(name.toArray()) // Full Result Set

let a = db.cources.findOne({Age : 20}) //to get first ressult
console.log(a)

//Update

db.cources.updateOne({Age : 20},{$set:{Age : 25}}) // to update 1st match

db.cources.updateMany({Age : 20},{$set:{Age : 25}}) //to update all

//Delete

db.cources.deleteOne({age : 25}) // to delete one 

db.cources.deleteMany({age : 25}) // to delete all