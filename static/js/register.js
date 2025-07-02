document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("registerForm");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.getElementById("email").value.trim();
    const location = document.getElementById("location").value.trim();
    const password = document.getElementById("password").value.trim();
    const confirm = document.getElementById("confirm").value.trim();

    const error = document.getElementById("error");
    const success = document.getElementById("success");
    error.innerText = "";
    success.innerText = "";

    if (!email || !password || !confirm) {
      error.innerText = "All fields are required.";
      return;
    }

    if (password !== confirm) {
      error.innerText = "Passwords do not match.";
      return;
    }

    try {
      const res = await fetch("/api/register/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email,location, password })
      });

      const text = await res.text();
      if (!res.ok) {
        error.innerText = text || "Registration failed.";
        return;
      }

      success.innerText = "✅ Registration successful! You can now log in.";
      window.location.href = "/login/";
      success.innerText = "✅ Registration successful!";

      form.reset();
    } catch (err) {
      error.innerText = "Something went wrong.";
    }
  });
});
