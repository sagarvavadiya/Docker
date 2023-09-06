const express = require("express");
const app = express();
const port = 5020;
const crud = require("./route/CRUDRoute/CRUDRoute");
const cors = require("cors");
app.use(cors());
app.use(express.json());

app.use(crud);
app.listen(port, () => {
  console.log(`Running on ${port} port  http://localhost:5020`);
});
