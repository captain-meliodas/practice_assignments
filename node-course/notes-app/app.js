const notes = require("./notes");
const yargs = require("yargs");

yargs.command({
    command: 'add',
    describe: 'Adding a new note',
    builder: {
        title: {
            describe: 'Note tile',
            demandOption: true,
            type: 'string'
        },
        body: {
            describe: 'Body of note',
            demandOption: true,
            type: 'string'
        }
    },
    handler: (argv) => {
        notes.addNotes(argv.title, argv.body);
    }
})

yargs.command({
    command: 'remove',
    describe: 'Remove a new note',
    builder: {
        title: {
            describe: 'Note tile',
            demandOption: true,
            type: 'string'
        },
    },
    handler: (argv) => {
        const title = notes.removeNotes(argv.title);
        if(title){
            console.log(title);
        }
        else{
            console.log("Note not found");
        }
    }
})

yargs.parse();