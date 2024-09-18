const apiUrl = 'http://127.0.0.1:8000/api/todos/'; // Adjust based on your API's URL

// Select form and task list
const todoForm = document.getElementById('todo-form');
const taskInput = document.getElementById('task-input');
const taskList = document.getElementById('task-list');

// Fetch all tasks from API
async function getTasks() {
    const response = await fetch(apiUrl);
    const tasks = await response.json();
    
    taskList.innerHTML = ''; // Clear task list
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.innerHTML = `
            <span>${task.title}</span>
            <button onclick="deleteTask(${task.id})">Delete</button>
        `;
        taskList.appendChild(li);
    });
}

// Add a new task
todoForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const taskTitle = taskInput.value;
    
    const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title: taskTitle }),
    });

    if (response.ok) {
        taskInput.value = ''; // Clear the input
        getTasks(); // Reload the task list
    }
});

// Delete a task
async function deleteTask(id) {
    const response = await fetch(`${apiUrl}${id}/`, {
        method: 'DELETE',
    });

    if (response.ok) {
        getTasks(); // Reload the task list
    }
}

// Initialize the app by loading all tasks
getTasks();
