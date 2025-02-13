document.addEventListener("DOMContentLoaded", function () {

    const trustedOrigin = "https://my-app.com";

    window.addEventListener("message", (event) => {
        if (event.origin !== trustedOrigin) {
            console.error("Untrusted origin:", event.origin);
            return;
        }
    });

    const form = document.getElementById("repository-form");
    const resultDiv = document.getElementById('sast-result');

    form.addEventListener("submit", function (event) {

        window.addEventListener("message", (event) => {
            if (event.origin !== trustedOrigin) {
                console.error("Untrusted origin:", event.origin);
                return;
            }
        });

        event.preventDefault();
        startTitleAnimation();
        resultDiv.classList.remove("result_container");
        resultDiv.innerHTML = ""; // Clear previous results
        showSpinner();

        const formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest', // Identify the request as AJAX
            },
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(html => {
                hideSpinner();
                stopTitleAnimation();
                resultDiv.classList.add("result_container");
                resultDiv.innerHTML = html;
            })
            .catch(error => {
                hideSpinner();
                console.error('Error:', error);
                resultDiv.innerHTML = "<p>There was an error processing your request.</p>";
            });
    });
});
