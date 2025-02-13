const last_title = document.title
let titleAnimation;
let dots = 0;

function startTitleAnimation() {
    titleAnimation = setInterval(() => {
        let dotsStr = ".".repeat(dots % 5);
        document.title = `Analyzing${dotsStr} 🔍`;
        dots++;
    }, 500);
}

function stopTitleAnimation() {
    clearInterval(titleAnimation);
    document.title = "Done! ✅";
    if (!document.hidden) {
        document.title = last_title;
    }
}

document.addEventListener("visibilitychange", function () {
    const trustedOrigin = "https://my-app.com";

    window.addEventListener("message", (event) => {
        if (event.origin !== trustedOrigin) {
            console.error("Untrusted origin:", event.origin);
            return;
        }
    });

    if (!document.hidden) {
        // User returns to the tab
        document.title = last_title;
    }
});