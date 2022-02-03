const fs = require("fs") //exporting the c++ file handling bindings

const add = require("./util.js") //exporting the function from another file
let sum = add(4, 2);

fs.writeFileSync("temp.txt", "Writing the file using c++ node bindings");

fs.appendFileSync("temp.txt", `Appended the data using appendfilesync ${sum}`);

// console.log(sum);

//----------------------------------------------
const validator = require("validator");
const chalk = require("chalk");
const yargs = require("yargs");

// console.log(chalk.bgRed.white.bold(validator.isEmail("singhankit226")));

//-----------------getting args from command

// console.log(process.argv);

//create a new add command using yargs
yargs.command({
    command: 'add',
    describe: 'Adding a new note',
    builder:{
        title:{//adding a required variable with type string 
            describe: 'Note tile',
            demandOption: true,
            type:'string'
        }
    },
    handler: (argv) => {
        console.log("Title:-- ",argv.title);
    }
})
//remove a note using yargs package
yargs.command({
    command: 'remove',
    describe: 'Remove a note',
    handler: () => {
        console.log("remove a new note");
    }
})
// console.log(yargs.argv);
//parse the arguments using yargs
yargs.parse();