document.addEventListener('DOMContentLoaded', function () {
  var loginForm = document.getElementById('login-form');

  loginForm.addEventListener("submit", function (event) {
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
          // Revert styles to original values
          chrome.runtime.sendMessage({ action: "revertStyles" });
        }
        return response.json();
      })
      .then(data => {
        alert(data.message);
      })
      .catch(error => {
        console.error('Error:', error);
        alert("An error occurred. Please try again.");
      });
  });

});

