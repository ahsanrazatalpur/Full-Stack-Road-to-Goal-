// crrating SCHEMA  GETTING FROM MONGOOSE WEB
import mongoose from "mongoose";
// import Todo from "./models/Todo";
//const kittySchema = new mongoose.Schema({ craeting own schema change kitten to Todo
const TodoSchema = new mongoose.Schema({
    // todo has two thing tile and desc both are string 
  name: String,
  desc: String,
  isDone : Boolean,
  days : Number
});
//const Kitten = mongoose.model('Kitten', kittySchema); chnging kitten schema to Todo Schema 
// type export before const
export const Todo = mongoose.model('Todo', TodoSchema);

// here we have created Schema Whenever we craet Todo  may contain title = String , desc  =String, isDone= Boolean 

//  "dev": "nodemon main.js" creat this line in pkgjson

// type localhost:3000 in browser to run express js