const socket = new WebSocket("ws://127.0.0.1:5000/ws");

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    document.getElementById("cpuUsage").innerText = data.cpu;
    document.getElementById("ramUsage").innerText = data.ram;

    const fileList = document.getElementById("fileList");
    fileList.innerHTML = ""; // Clear previous list

    data.files.forEach(file => {
        const listItem = document.createElement("li");
        listItem.innerText = `${file.filename} - ${file.allocated ? "✅ Allocated" : "❌ Not Allocated"}`;
        fileList.appendChild(listItem);
    });
};

function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a file to upload.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    fetch("/upload/", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error("Upload error:", error));
}
