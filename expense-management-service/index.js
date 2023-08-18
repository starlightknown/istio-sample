const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3002;

// Temporary storage for expense data
const expenses = [];

app.use(bodyParser.json());

// Route to create a new expense
app.post('/expense', (req, res) => {
    const { userId, amount, description } = req.body;
    expenses.push({ userId, amount, description });
    res.status(201).json({ message: 'Expense created successfully' });
});

// Route to get all expenses
app.get('/expenses', (req, res) => {
    res.json(expenses);
});

// Start the server
app.listen(PORT, () => {
    console.log(`Expense Management Service listening on port ${PORT}`);
});
