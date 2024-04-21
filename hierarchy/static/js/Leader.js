function updateTaskStatus(taskId) {
    var status = document.getElementById("status" + taskId).value;
    fetch(NewUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken 
        },
        body: JSON.stringify({
            task_id: taskId,
            status: status
        })
    })
    .then(response => {
        if (response.ok) {
            console.log("Status updated successfully");
            window.location.reload(); 
        } else {
            console.error("Failed to update status");
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
