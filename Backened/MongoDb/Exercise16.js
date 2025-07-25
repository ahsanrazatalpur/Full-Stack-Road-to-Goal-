const express = require('express')
const app = express()
const port = 3000

app.set('view engine', 'ejs'); // Tells Express to use EJS
app.set('views', './views');   // Optional: sets the views folder (default is './views')

app.get('/', (req, res) => {
   res.render('Exercise16'); // Looks for views/Exercise16.ejs
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

