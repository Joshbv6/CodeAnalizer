const last_title = document.title
let titleAnimation;
let dots = 0;

function startTitleAnimation() {
    titleAnimation = setInterval(() => {
        let dotsStr = ".".repeat(dots % 5);
        document.title = `Analyzing${dotsStr} 🔍`;
        dots++;
    }, 300);
}

function stopTitleAnimation() {
    clearInterval(titleAnimation);
    document.title = "Done! ✅";
    if (!document.hidden) {
        document.title = last_title;
    }
}

document.addEventListener("visibilitychange", function () {
    if (!document.hidden) {
        // User returns to the tab
        document.title = last_title;
    }
});