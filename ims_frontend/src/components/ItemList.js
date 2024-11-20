import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const ItemList = () => {
    const [items, setItems] = useState([]);

    useEffect(() => {
        getItems();
    }, []);

    // function getItems() {
    //     fetch('http://127.0.0.1:8080/item_list')
    //         .then(response => response.json())
    //         .then(data => {
    //             console.log(data);
    //             setItems(data);
    //         })
    //         .catch(error => {
    //             console.error(error);
    //         });
    // }
    const getItems = async () => {
        try {
            const response = await axios.get('http://192.168.1.5:8001/item');
            setItems(response.data);
        } catch (error) {
            console.error('Error fetching items:', error);
        }
    };


    return (
        <div>
            <h1>Item List</h1>


            <Link to="/item_insert" >Add Item</Link>

            <table border={3}>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Name</th>
                        <th>Rate</th>

                        <th colSpan={3}>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {items.map((item, key) => (
                        <tr key={key}>
                            <td>{key}</td>
                            <td>{item.item_name}</td>
                            <td>{item.rate}</td>

                            <td> <Link to={`/item_update/${item.id}`}>Update</Link></td>
                            <td><Link to={`/item_view/${item.id}`} >View </Link></td>
                            <td><Link to={`/item_delete/${item.id}`} >Delete </Link></td>

                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ItemList;
