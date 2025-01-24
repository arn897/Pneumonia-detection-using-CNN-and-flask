const form = document.getElementById('upload-form');
    const fileInput = document.getElementById('file-input');
    const uploadBox = document.getElementById('upload-box');
    const resultDiv = document.getElementById('result');
    const resultText = document.getElementById('result-text');
    const clearBtn = document.getElementById('clear-btn');
    const fileNameDisplay = document.getElementById('file-name');

    // Display selected file name or placeholder text
    fileInput.addEventListener('change', () => {
        const fileName = fileInput.files[0]?.name || "Drag & Drop image here or click to select";
        fileNameDisplay.textContent = fileName;
        uploadBox.classList.add("selected");
    });

    // Handle form submission
    form.onsubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData(form);

        try {
            const response = await fetch('/predict', { method: 'POST', body: formData });
            const data = await response.json();

            resultText.textContent = data.result === 'PNEUMONIA' ? 'Result: PNEUMONIA' : 'Result: NORMAL';
            resultText.className = data.result === 'PNEUMONIA' ? 'result-pneumonia' : 'result-normal';
            resultDiv.style.display = 'block';
        } catch (error) {
            alert('Error processing the request!');
        }
    };

    // Clear form and results
    clearBtn.addEventListener('click', () => {
        form.reset();
        resultDiv.style.display = 'none';
        fileNameDisplay.textContent = ""; // Clear file name
        uploadBox.classList.remove("selected");
    });