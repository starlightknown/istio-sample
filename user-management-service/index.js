const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3001;

// Temporary storage for user data
const users = [];

app.use(bodyParser.json());

// Route to create a new user
app.post('/user', (req, res) => {
    const { username, email } = req.body;
    users.push({ username, email });
    res.status(201).json({ message: 'User created successfully' });
});

// Route to get all users
app.get('/users', (req, res) => {
    res.json(users);
});

// Start the server
app.listen(PORT, () => {
    console.log(`User Management Service listening on port ${PORT}`);
});
