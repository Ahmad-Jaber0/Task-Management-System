    document.addEventListener('DOMContentLoaded', function() {
        const usernameInput = document.getElementById('username');
        const signUpButton = document.querySelector('button[type="submit"]');
        const passwordInput = document.getElementById('password1');
        const confirmPasswordInput = document.getElementById('password2');
        const passwordMatchMessage = document.getElementById('password-match-message');
        const errorMessage = document.getElementById('username-message');

        function updateButtonStatus() {
            const isEmpty = Array.from(document.querySelectorAll('input')).some(input => input.value.trim() === '');
            if (isEmpty || passwordInput.value !== confirmPasswordInput.value) {
                signUpButton.disabled = true;
            } else {
                signUpButton.disabled = false;
            }
        }

        function checkPasswordMatch() {
            if (passwordInput.value !== confirmPasswordInput.value) {
                passwordMatchMessage.textContent = 'Passwords do not match.';
                passwordMatchMessage.style.display = 'block';
                signUpButton.disabled = true;
            } else {
                passwordMatchMessage.textContent = '';
                passwordMatchMessage.style.display = 'none';
                updateButtonStatus();
            }
        }

        function checkUsernameAvailability() {
            const username = usernameInput.value.trim();
            if (username.length === 0) {
                errorMessage.textContent = '';
                updateButtonStatus();
                return;
            }

            fetch('/check-username/', {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
                },
                body: JSON.stringify({ username: username })
            })
            .then(response => response.json())
            .then(data => {
                if (data.is_taken) {
                errorMessage.textContent = 'Username is already taken. Please choose a different one.';
                errorMessage.style.display = 'block';
                signUpButton.disabled = true;
                } else {
                errorMessage.textContent = '';
                errorMessage.style.display = 'none';
                updateButtonStatus();
                }
            })
            .catch(error => {
                console.error('Error:', error);
                errorMessage.textContent = 'An error occurred while checking the username.';
                errorMessage.style.display = 'block';
                signUpButton.disabled = true;
            });
        }

        signUpButton.addEventListener('click', function() {
            checkPasswordMatch();
            checkUsernameAvailability();
        });

        passwordInput.addEventListener('input', function() {
            checkPasswordMatch();
        });

        confirmPasswordInput.addEventListener('input', function() {
            checkPasswordMatch();
        });

        usernameInput.addEventListener('input', function() {
            checkUsernameAvailability();
        });

        updateButtonStatus();
    });