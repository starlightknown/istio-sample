const expenseForm = document.getElementById('expenseForm');
const expensesList = document.getElementById('expensesList');

expenseForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const userId = document.getElementById('userId').value;
    const amount = document.getElementById('amount').value;
    const description = document.getElementById('description').value;

    const data = { userId, amount, description };

    try {
        const response = await fetch('http://localhost:3002/expense', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            console.log('Expense added successfully');
            updateExpensesList();
        } else {
            console.error('Error adding expense');
        }
    } catch (error) {
        console.error('Error:', error);
    }
});

async function updateExpensesList() {
    try {
        const response = await fetch('http://localhost:3002/expenses');
        const expenses = await response.json();

        expensesList.innerHTML = expenses.map(expense =>
            `<li>User ID: ${expense.userId}, Amount: ${expense.amount}, Description: ${expense.description}</li>`
        ).join('');
    } catch (error) {
        console.error('Error:', error);
    }
}

updateExpensesList();
