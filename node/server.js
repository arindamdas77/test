const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("<h1> Express ARINDAM DAS its a Pipline on Jankins test 2!</h1>");
});

app.listen(3000, () => console.log);

