// Listen for messages from the popup and forward them to the content script
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    // Forward the message to the content script
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.tabs.sendMessage(tabs[0].id, request);
    });
  });
  