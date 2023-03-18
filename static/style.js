function showLoading() {
    var loading = document.getElementById("loading");
    var dots = document.getElementById("dots");
    loading.style.display = "block";
    var interval = setInterval(function () {
        if (dots.innerHTML.length >= 3) {
            dots.innerHTML = "";
        } else {
            dots.innerHTML += ".";
        }
    }, 1000);
    setTimeout(function () {
        clearInterval(interval);
        loading.style.display = "none";
    }, 5000);
}
