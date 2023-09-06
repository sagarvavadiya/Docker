const express = require("express");
const CRUDController = require("../../controller/Crud/CrudController");
crudRoutes = express.Router();

crudRoutes.get("/", CRUDController.TakeScreenShot);
crudRoutes.get("/activeScreen", CRUDController.ActiveScreen);
module.exports = crudRoutes;
