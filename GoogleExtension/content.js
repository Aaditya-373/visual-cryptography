// Function to set styles to make the page 25% visible, blurred, and not clickable
function setLoginPageStyles() {
  // document.body.style.opacity = '0.25';
  // document.body.style.filter = 'blur(5px)';
  document.body.style.pointerEvents = 'none';

  // Save original page content and styles to Chrome storage
  chrome.storage.local.set({
    originalPageContent: document.body.innerHTML,
    originalOpacity: '1',
    originalFilter: 'none',
    originalPointerEvents: 'auto'
  });
}

// Function to revert back to the original page styles
function revertPageStyles() {
  chrome.storage.local.get(["originalPageContent", "originalOpacity", "originalFilter", "originalPointerEvents"], function(result) {
    // document.body.innerHTML = result.originalPageContent;
    // document.body.style.opacity = result.originalOpacity;
    // document.body.style.filter = result.originalFilter;
    document.body.style.pointerEvents = result.originalPointerEvents;
  });
}

// Execute the function to set login page styles when the content script runs
setLoginPageStyles();

// Listen for messages from popup.js
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "revertStyles") {
    revertPageStyles();
  }
});
