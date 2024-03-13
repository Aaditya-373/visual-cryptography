document.addEventListener('DOMContentLoaded', function () {
  var loginForm = document.getElementById('login-form');
  loginForm.innerHTML = `
    <div class="login-container">
      <h2>Login</h2>
      <form class="login-form" id="loginForm" enctype="multipart/form-data">
        <input type="text" name="userId" id="userId" placeholder="UserID" required>
        <input type="file" name="image" id="image" accept="image/*" required>
        <input type="submit" value="Login" id="submitButton">
      </form>
    </div>`;

  document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault();

    var formData = new FormData();
    formData.append("userId", document.getElementById("userId").value);
    formData.append("image", document.getElementById("image").files[0]);

    fetch("http://localhost:5000/sso", {
      method: "POST",
      body: formData
    })
      .then(response => {
        if (response.ok) {
          chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            chrome.scripting.executeScript({
              target: {tabId: tabs[0].id},
              function: hideLoginReminder
            });
          });
        }
        return response.json();
      })
      .then(data => {
        alert(data.message)
      })
      .catch(error => {
        console.error('Error:', error);
        alert("An error occurred. Please try again.");
      });
  });
});

function hideLoginReminder() {
  var loginReminder = document.querySelector('.login-reminder');
  if (loginReminder) {
    loginReminder.style.display = 'none';
  }
}
