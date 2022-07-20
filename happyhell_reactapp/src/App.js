import react from 'react'
import './App.css';
import Navbar from './components/navbar-menu';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Admin from './pages/admin';
import Documents from './pages/documents';
import Fabrica from './pages/fabrica';
import Massive from './pages/massive';
import Messages from './pages/messages';
import Paymen from './pages/paymen';
import Polit from './pages/polit';
import Process from './pages/process';
import Support from './pages/support';

function App() {
    return (
        <Router>
            <Navbar />
            <switch>
                <Route path='/admin' component={Admin} />
                <Route path='/documents' component={Documents} />
                <Route path='/fabrica' component={Fabrica} />
                <Route path='/massive' component={Massive} />
                <Route path='/messages' component={Messages} />
                <Route path='/paymen' component={Paymen} />
                <Route path='/polit' component={Polit} />
                <Route path='/process' component={Process} />
                <Route path='/support' component={Support} />
            </switch>
        </Router>
    );
}

export default App;
