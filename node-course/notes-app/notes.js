const fs = require('fs');

const removeNotes = function (title) {
    const notes = loadNotes();
    let deletednote = '';
    const notestokeep = notes.filter(function (note) {
        if(note.title === title){
            deletednote = note.title
        }
        return note.title != title
    })
    saveNotes(notestokeep);
    return deletednote;
}

const addNotes = function (title, body) {
    const notes = loadNotes();
    const duplicateNotes = notes.filter(function (note) {
        return note.title === title
    })
    if (duplicateNotes.length == 0) {
        notes.push({
            title: title,
            body: body
        });
        saveNotes(notes);
    }
}

const saveNotes = function (notes) {
    const dataJSON = JSON.stringify(notes);
    fs.writeFileSync("notes_data.json", dataJSON);
}

const loadNotes = function () {
    try {
        const dataBuffer = fs.readFileSync("notes_data.json");
        const dataJSON = dataBuffer.toString();
        return JSON.parse(dataJSON);
    }
    catch {
        return []
    }
}

defaults = {
    removeNotes: removeNotes,
    addNotes: addNotes
}

module.exports = defaults