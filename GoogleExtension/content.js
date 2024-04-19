// Function to set styles to make the page 25% visible, blurred, and not clickable
function setLoginPageStyles() {
  document.body.style.opacity = '0';
  document.body.style.pointerEvents = 'none';
  chrome.storage.local.set({
    originalPageContent: document.body.innerHTML,
    originalOpacity: '1',
    originalPointerEvents: 'auto',
  });
}

function revertPageStyles() {
  chrome.storage.local.get(["originalPageContent", "originalOpacity", "originalPointerEvents"], function(result) {
    document.body.style.opacity = result.originalOpacity;
    document.body.style.pointerEvents = result.originalPointerEvents;
  });
}

setLoginPageStyles();

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "revertStyles") {
    revertPageStyles();
  }
});
