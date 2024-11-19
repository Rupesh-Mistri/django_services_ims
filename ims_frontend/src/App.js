
import './App.css';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import ItemList from './components/ItemList';
function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <nav>
          <ul type=''>
            <li>
              <Link to="item" >Item Master</Link>
            </li>
            {/* <li>
              <Link to="supplier" >Supplier Master</Link>
            </li> */}
          </ul>
        </nav>
        <Routes>
          <Route path="/item_list" element={<ItemList />} />
          {/* <Route path="item_master/item_insert" element={<CreateItem />} />
          <Route path="item_master/item_update/:id" element={<UpdateItem />} />
          <Route path="item_master/item_view/:id" element={<ViewItem />} />
          <Route path="item_master/item_delete/:id" element={<DeleteItem />} />
          <Route path='supplier_master/supplier_list' element={<SupplierList />} />
          <Route path='supplier_master/supplier_insert' element={<CreateSupplier />} /> */}
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
