/* ---------- LOGIN MODAL ---------- */

function openLogin() {
    const modal = document.getElementById("loginModal");
    modal.style.display = "flex";
}

function closeLogin() {
    const modal = document.getElementById("loginModal");
    modal.style.display = "none";
}

// Закрити по кліку фону
window.onclick = function(e) {
    const modal = document.getElementById("loginModal");
    if (e.target === modal) modal.style.display = "none";
};


/* ---------- TOAST ---------- */
function showToast(message) {
    let t = document.createElement('div');
    t.className = 'toast';
    t.innerText = message;
    document.body.appendChild(t);

    setTimeout(()=> t.classList.add('show'), 20);

    setTimeout(()=> {
        t.classList.remove('show');
        setTimeout(()=> t.remove(), 300);
    }, 3000);
}


/* ---------- AJAX ADD TO CART (опціонально) ---------- */
document.addEventListener('submit', function(e){
    if (e.target && e.target.classList.contains('add-cart-form')) {
        e.preventDefault();
        const form = e.target;
        const data = new FormData(form);

        fetch(form.action, {
            method: form.method,
            body: data,
        }).then(res => {
            if (res.redirected) {
                window.location = res.url;
            } else {
                showToast('Vare lagt til i handlekurven');
            }
        }).catch(err => {
            showToast('Feil ved å legge i handlekurven');
        });
    }
});


function togglePassword() {
    const input = document.getElementById("passInput");
    input.type = input.type === "password" ? "text" : "password";
}
