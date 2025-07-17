/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// Select the database to use.
use('myfirstdbDatabase');

// Insert a few documents into the sales collection.
db.getCollection('practice').insertMany(
  [
  {
    "Name": "Ahsan Raza",
    "Address": "Badin",
    "Country": "Pakistan"
  },
  {
    "Name": "Sara Ahmed",
    "Address": "Lahore",
    "Country": "Pakistan"
  },
  {
    "Name": "John Doe",
    "Address": "New York",
    "Country": "USA"
  },
  {
    "Name": "Fatima Noor",
    "Address": "Karachi",
    "Country": "Pakistan"
  },
  {
    "Name": "Liam Smith",
    "Address": "London",
    "Country": "UK"
  },
  {
    "Name": "Emily Zhang",
    "Address": "Beijing",
    "Country": "China"
  },
  {
    "Name": "Carlos Ruiz",
    "Address": "Madrid",
    "Country": "Spain"
  },
  {
    "Name": "Maya Patel",
    "Address": "Mumbai",
    "Country": "India"
  },
  {
    "Name": "Anna Müller",
    "Address": "Berlin",
    "Country": "Germany"
  },
  {
    "Name": "Omar El-Sayed",
    "Address": "Cairo",
    "Country": "Egypt"
  }
]

);


// Print a message to the output window.
console.log(`Done inserting data`);


