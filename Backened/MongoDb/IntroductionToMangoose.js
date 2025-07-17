// Mangoose ( A JavaScript Library)

// make validation easy
// schema base solution

import mongoose from "mongoose";
import express from "express"
import Todo from "./models/Todo"
import { title } from "process";

let conn = await mongoose.connect("mongodb://localhost:27017/todo")


const app = express()
const port = 3000

app.get('/', (req, res) => {
    const Todo = new Todo({ title: "Hey first Todo", Desc: "Descipton of Todo", isDone: false })
    Todo.save()
    res.send('Hello World!')
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})


