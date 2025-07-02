document.addEventListener("DOMContentLoaded", () => {
  console.log("✅ login.js loaded and DOM ready");

  const form = document.getElementById("loginForm");
  const loginBtn = document.getElementById("loginBtn");

  if (!form || !loginBtn) {
    console.error("❌ Form or button not found");
    return;
  }

  loginBtn.addEventListener("click", async () => {
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    if (!email || !password) {
      document.getElementById("error").innerText = "Please enter email and password.";
      return;
    }

    try {
      const res = await fetch("/api/users/login/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
      });

      const text = await res.text();
      if (!res.ok) {
        console.warn("Login failed response:", text);
        document.getElementById("error").innerText = "Invalid credentials.";
        return;
      }

      const data = JSON.parse(text);
      console.log("✅ Tokens received:", data);

      // 🔐 Store tokens using proper keys
      localStorage.setItem("access_token", data.access);
      localStorage.setItem("refresh_token", data.refresh);
      console.log("✅ Tokens stored in localStorage");

      // 🚀 Redirect to dashboard
      window.location.href = "/dashboard/";

    } catch (err) {
      console.error("Unexpected login error:", err);
      document.getElementById("error").innerText = "An error occurred during login.";
    }
  });
});
