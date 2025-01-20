
// show/hide Password
document.getElementById('togglePassword').addEventListener('click', function () {
    togglePasswordVisibility('password', 'togglePassword', 'togglePasswordSlash');
  });
  
  document.getElementById('togglePasswordSlash').addEventListener('click', function () {
    togglePasswordVisibility('password', 'togglePassword', 'togglePasswordSlash');
  });
  
  document.getElementById('toggleConfirmPassword').addEventListener('click', function () {
    togglePasswordVisibility('confirm_password', 'toggleConfirmPassword', 'toggleConfirmPasswordSlash');
  });
  
  document.getElementById('toggleConfirmPasswordSlash').addEventListener('click', function () {
    togglePasswordVisibility('confirm_password', 'toggleConfirmPassword', 'toggleConfirmPasswordSlash');
  });
  
  function togglePasswordVisibility(passwordId, toggleIconId, toggleIconSlashId) {
    const password = document.getElementById(passwordId);
    const toggleIcon = document.getElementById(toggleIconId);
    const toggleIconSlash = document.getElementById(toggleIconSlashId);
  
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
  
    // Toggle icons
    toggleIcon.classList.toggle('hidden');
    toggleIconSlash.classList.toggle('hidden');
  }



  function validateForm() {
    var email = document.getElementById("email").value;
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm_password").value;

    var errorMessages = document.querySelectorAll('.error-message');
    var inputFields = document.querySelectorAll('input');
    errorMessages.forEach(function(error) {
      error.remove();
    });
    inputFields.forEach(function(input) {
      input.classList.remove("input-error");
    });

    var isValid = true;

    // Email validation
    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailPattern.test(email)) {
      showError("email-error", "Please enter a valid email");
      isValid = false;
    }

    // Checking the username field
    if (username == "") {
      showError("username-error", "Please enter your username");
      isValid = false;
    }

    // Check the password field
    if (password == "") {
      showError("password-error", "Please enter your password");
      isValid = false;
    }

    // Check password compatibility and password confirmation
    if (password !== confirmPassword) {
      showError("confirm_password-error", "The password and confirmation password must be the same");
      isValid = false;
    }

    // Check password length
    if (password.length < 6) {
      showError("password-error", "Password must be at least 6 characters");
      isValid = false;
    }

    return isValid;
  }

  function showError(errorId, message) {
    var errorElement = document.createElement("span");
    errorElement.classList.add("error-message");
    errorElement.textContent = message;

    var inputElement = document.getElementById(errorId.replace("-error", ""));
    inputElement.classList.add("input-error");

    var errorContainer = document.getElementById(errorId);
    errorContainer.innerHTML = ''; // پاک کردن ارورهای قبلی
    errorContainer.appendChild(errorElement);
  }




  function validateLoginForm() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
  
    var errorMessages = document.querySelectorAll('.error-message');
    var inputFields = document.querySelectorAll('input');
    errorMessages.forEach(function(error) {
      error.remove();
    });
    inputFields.forEach(function(input) {
      input.classList.remove("input-error");
    });
  
    var isValid = true;
  
    // Email validation
    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailPattern.test(email)) {
      showError("email-error", "Please enter a valid email");
      isValid = false;
    }
  
    // Check the password field
    if (password == "") {
      showError("password-error", "Please enter your password");
      isValid = false;
    }
  
    return isValid;
  }
  
  function showError(errorId, message) {
    var errorElement = document.createElement("span");
    errorElement.classList.add("error-message");
    errorElement.textContent = message;
  
    // اضافه کردن کلاس error به input برای تغییر رنگ حاشیه
    var inputElement = document.getElementById(errorId.replace("-error", ""));
    inputElement.classList.add("input-error");
  
    // پیدا کردن المان خطا و اضافه کردن پیام خطا به آن
    var errorContainer = document.getElementById(errorId);
    errorContainer.innerHTML = ''; // پاک کردن ارورهای قبلی
    errorContainer.appendChild(errorElement);
  }
  function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}