import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

//router
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

// components
import UseStateBasics from './components/usestate'
import UseStateArray from './components/usestatearry'
import UseStateObject from './components/usestateobject'
import UseStateCounter from './components/usestatecounter'
import UseEffectBasics from './components/useeffect'
import UseEffectMultiple from './components/useeffectmultiple'
import Operators from './components/operators'
import Form from './components/form'
import UseRefBasics from './components/useref'
import UseReducerBasics from './components/usereducer'
import PropDrilling from './components/propdrilling'
import ContextApi from './components/contextapi'
import Example from './components/call_custom_hook'

import Person from './components/person'

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <Switch>
        <Route exact path="/">
          <App />
        </Route>

        <Route path="/usestate">
          <div className='container'>
            <h2>UseState Basic Example</h2>
          </div>
          <UseStateBasics />
        </Route>

        <Route path="/usestatearray">
          <div className='container'>
            <h2>UseState array example</h2>
          </div>
          <UseStateArray />
        </Route>

        <Route path="/usestateobject">
          <UseStateObject />
        </Route>

        <Route path="/usestatecounter">
          <UseStateCounter />
        </Route>

        <Route path="/useseffect">
          <UseEffectBasics />
        </Route>

        <Route path="/useseffectmulti">
          <UseEffectMultiple />
        </Route>

        <Route path="/operators">
          <Operators />
        </Route>

        <Route path="/form">
          <Form />
        </Route>

        <Route path="/userefbasics">
          <UseRefBasics />
        </Route>

        <Route path="/usereducer">
          <UseReducerBasics />
        </Route>

        <Route path="/propdrilling">
          <PropDrilling />
        </Route>

        <Route path="/contextapi">
          <ContextApi />
        </Route>

        <Route path="/customhook">
          <Example />
        </Route>

        <Route  path='/person/:id' children={<Person />} />

        {/* when no routes matched root page will render always */}
        <Route path="*">
          <App />
        </Route>
      </Switch>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);
