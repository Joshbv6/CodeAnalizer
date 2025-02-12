document.addEventListener("DOMContentLoaded", (event) => {
    let isMobile = window.innerWidth < 768;
    let svg = document.getElementById("waveSvg");

    svg.setAttribute("viewBox", isMobile ? "0 0 500 620" : "0 0 500 200");

    document.getElementById("wave1").setAttribute("d", isMobile
        ? "M -40 200 C 150 400 220 95 500 275 L 500 0 L 0 0"
        : "M 0 50 C 150 150 300 0 500 95 L 500 0 L 0 0"
    );

    document.getElementById("wave2").setAttribute("d", isMobile
        ? "M -40 200 C 150 400 240 90 500 235 L 500 0 L 0 0"
        : "M 0 50 C 150 150 330 -30 500 65 L 500 0 L 0 0"
    );

    document.getElementById("wave3").setAttribute("d", isMobile
        ? "M -40 200 C 150 400 160 95 500 310 L 500 0 L 0 0"
        : "M 0 50 C 150 150 250 0 500 120 L 500 0 L 0 0"
    );
});

