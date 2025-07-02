
document.addEventListener("DOMContentLoaded", async () => {
  let access = localStorage.getItem("access_token");
  const refresh = localStorage.getItem("refresh_token");

  // If access token is missing or expired, try refreshing
  async function tryRefreshAccessToken() {
    if (!refresh) return false;

    const res = await fetch("/api/users/refresh/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ refresh })
    });

    if (!res.ok) return false;

    const data = await res.json();
    localStorage.setItem("access_token", data.access);
    console.log("✅ Refreshed access token");
    access = data.access;
    return true;
  }

  // Fetch weather data
  async function loadDashboard() {
    let res = await fetch("/api/weather/", {
      headers: {
        Authorization: `Bearer ${access}`
      }
    });

    if (res.status === 401) {
      // Try refreshing the access token
      const refreshed = await tryRefreshAccessToken();
      if (refreshed) {
        return loadDashboard();  // Retry
      } else {
        alert("Session expired. Please log in again.");
        localStorage.clear();
        window.location.href = "/login/";
        return;
      }
    }

    const data = await res.json();
    document.getElementById("weather").innerHTML = `
      <h3>City: ${data.location}</h3>
      <p>Temperature: ${data.temperature}°C</p>
      <p>Condition: ${data.description}</p>
    `;
  }

  await loadDashboard();
});

