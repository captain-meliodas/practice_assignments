const app = require("./app")

const port = process.env.PORT //for deployment purpose (on server)

const swaggerUI = require("swagger-ui-express")
const YAML = require("yamljs")
const swaggerJsDocs = YAML.load("./src/api.yaml")
app.use("/api-docs", swaggerUI.serve, swaggerUI.setup(swaggerJsDocs))

app.listen(port, () => {
    console.log('Server is up on port ' + port)
})