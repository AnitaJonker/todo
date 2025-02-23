// function toggleEditMode(taskPk) {
//     const taskText = document.getElementById(`task-name-${taskPk}`);
//     const taskEdit = document.getElementById(`edit-task-${taskPk}`);
    
//     taskText.style.display = taskText.style.display === 'none' ? 'block' : 'none';
//     taskEdit.style.display = taskEdit.style.display === 'none' ? 'block' : 'none';
//   }

  // Function to handle saving the task name
//   function saveTask(taskPk) {
//      save_task_name = async (installationID, datatab) => {
//       const url = "save_task";
//       try {
//         const response = await fetch(url, {
//           method: "POST",
//           headers: {
//             "Content-Type": "application/json",
//             "X-CSRFToken": csrftoken,
//           },
//           body: JSON.stringify({ InstallId: installationID, tab: datatab }),
//         })
//           .then((response) => {
//             if (!response.ok) {
//               throw new Error(`Response status: ${response.status}`);
//             }
//             return response.json().then((data) => {
//               const dynamicTab = document.getElementById("dynamic-tab");
//               if (dynamicTab) {
//                 dynamicTab.innerHTML = data.html;
//               } else {
//                 console.error("Element with ID 'dynamic-tab' not found.");
//               }
//             });
//           })
//           .then((data) => {
//             document.getElementById("dynamic-tab").innerHTML = data.html;
//           });
//       } catch (error) {
//         console.error(error.message);
//       }
//     };
  function saveTask(taskPk) {
    const newTaskName = document.getElementById(`task-input-${taskPk}`).value;
    const url = `/save_task/${taskPk}`; 

    // Send AJAX request to save the task name
    
    try {
            fetch(url, {
                method: "POST",
                headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                },
                body: JSON.stringify({newTaskName: newTaskName }),
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                window.location.reload();
                // document.getElementById("body-test").innerHTML = data.html;
            })
            .catch(error => console.error('Error:', error));
            } catch (error) {
            console.error(error.message);
            }
        };

  // Function to handle canceling the edit
  function cancelEdit(taskPk) {
    toggleEditMode(taskPk);  // Switch back to the view mode without saving
  }