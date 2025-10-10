document.addEventListener('DOMContentLoaded', function () {
  console.log('JavaScript loaded!');
  const pageViews = incrementPageCounter();
  console.log(`This site has had ${pageViews} page loads`);
});

// Counter function to track page loads
function incrementPageCounter() {
  // Get existing count from cookie or start at 0
  let count = getCookie('pageCount') || 0;

  // Increment count
  count = parseInt(count) + 1;

  // Save new count to cookie (expires in 30 days)
  setCookie('pageCount', count, 30);
  document.getElementById('page_count').textContent = count;

  return count;
}

// Helper function to set cookie
function setCookie(name, value, days) {
  const expires = new Date();
  expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
  document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
}

// Helper function to get cookie value
function getCookie(name) {
  const cookies = document.cookie.split(';');
  for (let cookie of cookies) {
    const [cookieName, cookieValue] = cookie.split('=').map(c => c.trim());
    if (cookieName === name) {
      return cookieValue;
    }
  }
  return null;
}