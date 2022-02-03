import React, { Component } from 'react'
import axios from 'axios'; //axios is used for making request to backend express server

class Fib extends Component {
    //seenIndexes are the seen indexes which is already calculated
    //values are the key pair index:value which is calculated
    //index is the value upto which we have to calculate fib sequence
    state = {
        seenIndexes: [],
        values: {},
        index: ''
    };

    //helper lifecycle methods
    componentDidMount() {
        //helper methods
        this.fetchValues(); //fetch values we have currently calculated viewed from redis
        this.fetchIndexes(); // fetch indexes we have already calculated and stored in postgres
    }

    //method definitions

    handleSubmit = async (ev) =>{
        //bound function
        ev.preventDefault();

        await axios.post('/api/values',{
            index: this.state.index
        }).then(function(res){
        })
        this.setState({index: ''});
    }

    async fetchValues() {
        const values = await axios.get('/api/values/current'); //fetch values from route we have created

        this.setState({
            values: values.data
        });
    }

    async fetchIndexes() {
        const seenIndexes = await axios.get('/api/values/all'); //fetch values from route we have created
        this.setState({
            seenIndexes: seenIndexes.data
        })
    }

    renderSeenIndexes() {
        // in the seenIndexes array, each object in array has a number property which holds the number 
        //each number is followed by a comma (,) using join 
        return this.state.seenIndexes.map(({ number }) => number).join(', ')
    }

    renderValues() {
        const entries = [];
        for (let key in this.state.values){
            entries.push(
                <div key={key}>
                    For index {key} I calculated {this.state.values[key]}
                </div>
            )
        }

        return entries
    }

    //rendring the form for inputting the index to calculate fib seq
    render() {
        return (
            <div>
                <div>
                    <form onSubmit={this.handleSubmit}>
                        <label>Enter the Index</label>
                        <input 
                            value={this.state.index}
                            onChange={ev => this.setState({index:ev.target.value})}
                        />
                        <button>Submit</button>
                    </form>
                </div>
                <div>
                    <h3>I have seen indexes</h3>
                    {this.renderSeenIndexes()}
                </div>
                <div>
                    <h3>Calculated Values</h3>
                    {this.renderValues()}
                </div>
            </div>
        )
    }
}

export default Fib;