// Introduction to Mongoose

// Mogoose is MongoDb base ODM
// Mongoose is javaScript Library
// used to make validation easy , provide shema based solution mean typecasting , validation and query 
// building easy for us 
// There is MongoDb Raw pkg 
// Advanced pkg called Mongoose
// Mongoose is just a pkg
//  we use Mongoose  in express app to connect it with MongoDb
// validation Bulit-in
// MongoDb has no any Shcema Ex: we make a user ,name ,status here we set name as in int so its valid fpr MDb
// But in Mogoose we can set a Schema that we shoula type name  as string no as integer etc



// commands are 
// npm init -y
// npm i express

import mongoose from "mongoose";
import express from "express";
import { Todo } from "./models/Todo.js";

let conn = await mongoose.connect("mongodb://localhost:27017/") // connection string from mongoDb local storage
// Dummy hello world code from Expree js web 
//const express = require('express') // we cant use require else we use import
const app = express()
const port = 3000

app.get('/', (req, res) => {
    const todo = new Todo({ title: "my first Todo", desc: "Discription of this Todo", isDone: false ,days : 3})
    todo.save()

    res.send('Hello World!')
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})

app.get('/', async(req, res) => {
let todo =await  Todo.findOne("{}")
    res.json({title:todo.title,desc:todo.dsec})
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})
