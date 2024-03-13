// Check if the user is logged in
chrome.storage.local.get(['loggedIn'], function(result) {
  if (!result.loggedIn) {
    // Initial content display
    document.body.innerHTML = `
    <div class="login-reminder">
      <h1>Please Login</h1>
    </div>
    `;
  }
});

// Listen for messages from the popup
chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
  if (message.action === "hideLoginReminder") {
      // Hide the login reminder
      var loginReminder = document.querySelector('.login-reminder');
      if (loginReminder) {
          loginReminder.remove();
      }
  }
});
