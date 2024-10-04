const express = require('express');
const bodyParser = require('body-parser');
const { Pool } = require('pg');
const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection details from Neon DB
const pool = new Pool({
    user: 'your-db-user',         // Replace with your Neon DB user
    host: 'your-db-host',         // Replace with your Neon DB host
    database: 'neondb',           // Replace with your database name (neondb)
    password: 'your-db-password', // Replace with your Neon DB password
    port: 'your-db-port',         // Replace with your Neon DB port
});

// Route for donor sign-up
app.post('/donor-signup', (req, res) => {
    const { name, email, password, contact } = req.body;
    const query = 'INSERT INTO donors (name, email, password, contact) VALUES ($1, $2, $3, $4)';
    pool.query(query, [name, email, password, contact], (error, result) => {
        if (error) {
            console.error(error);
            res.status(500).send('Error saving data');
        } else {
            res.status(200).send('Sign-up successful!');
        }
    });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
