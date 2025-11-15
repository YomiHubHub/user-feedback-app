const API_URL = "http://localhost:5000"; // Backend endpoint

// Handle form submission
document.getElementById("feedbackForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const message = document.getElementById("message").value;

  const response = await fetch(`${API_URL}/feedback`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, message }),
  });

  if (response.ok) {
    alert("Feedback submitted successfully!");
    document.getElementById("feedbackForm").reset();
    loadFeedback();
  } else {
    alert("Failed to submit feedback.");
  }
});

// Fetch all feedback
async function loadFeedback() {
  const response = await fetch(`${API_URL}/feedback`);
  const feedbackList = await response.json();

  const listElement = document.getElementById("feedbackList");
  listElement.innerHTML = "";

  feedbackList.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = `${item.name}: ${item.message}`;
    listElement.appendChild(li);
  });
}

// Load feedback on page load
window.onload = loadFeedback;
