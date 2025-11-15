let currentVideoId = null;

async function uploadVideo() {
    const fileInput = document.getElementById("videoInput");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a video first!");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    document.getElementById("uploadStatus").textContent = "Uploading...";

    try {
        const response = await fetch("https://few-bobcats-strive.loca.lt/api/videos", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        console.log(data);

        currentVideoId = data.video_id;

        // Update UI
        document.getElementById("uploadStatus").textContent = "Upload successful!";
        document.getElementById("videoPreview").classList.remove("hidden");
        document.getElementById("question-section").classList.remove("hidden");

        // Show the video in a player
        document.getElementById("videoPlayer").src = `https://few-bobcats-strive.loca.lt/${data.path}`;

    } catch (error) {
        alert("Error uploading video");
        console.error(error);
    }
}

async function askQuestion() {
    const question = document.getElementById("questionInput").value;

    if (!question) {
        alert("Please enter a question.");
        return;
    }

    if (!currentVideoId) {
        alert("Please upload a video first.");
        return;
    }

    document.getElementById("answerOutput").textContent = "Thinking...";

    try {
        const response = await fetch(`https://few-bobcats-strive.loca.lt/api/videos/${currentVideoId}/ask`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question })
        });

        const data = await response.json();
        document.getElementById("answerOutput").textContent = data.answer;

    } catch (error) {
        alert("Error asking question");
        console.error(error);
    }
}