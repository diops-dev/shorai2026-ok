/* =============================================================
   shōrAI — Interactions
   Nav mobile · reveal · FAQ · cookies · formulaire EmailJS
   ============================================================= */
(function () {
  "use strict";

  /* ---- Mobile menu ---- */
  var burger = document.querySelector(".nav__burger");
  var mobile = document.getElementById("mobileMenu");
  var mClose = document.querySelector(".mobile-menu__close");
  if (burger && mobile) {
    burger.addEventListener("click", function () { mobile.classList.add("open"); document.body.style.overflow = "hidden"; });
    if (mClose) mClose.addEventListener("click", function () { mobile.classList.remove("open"); document.body.style.overflow = ""; });
    mobile.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { mobile.classList.remove("open"); document.body.style.overflow = ""; });
    });
  }

  /* ---- Reveal on scroll ---- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); obs.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    revealEls.forEach(function (el) { obs.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- FAQ accordion ---- */
  document.querySelectorAll(".faq__q").forEach(function (q) {
    q.addEventListener("click", function () {
      var item = q.closest(".faq__item");
      var ans = item.querySelector(".faq__a");
      var open = item.classList.toggle("open");
      q.setAttribute("aria-expanded", open ? "true" : "false");
      ans.style.maxHeight = open ? ans.scrollHeight + "px" : "0";
    });
  });

  /* ---- Cookie banner ---- */
  var cookie = document.getElementById("cookie");
  if (cookie) {
    var KEY = "shorai_cookie_choice";
    var choice = null;
    try { choice = localStorage.getItem(KEY); } catch (e) {}
    if (!choice) cookie.classList.add("show");
    cookie.querySelectorAll("[data-cookie]").forEach(function (b) {
      b.addEventListener("click", function () {
        try { localStorage.setItem(KEY, b.getAttribute("data-cookie")); } catch (e) {}
        cookie.classList.remove("show");
      });
    });
  }

  /* ---- Contact form (EmailJS, mailto fallback) ---- */
  var form = document.getElementById("contactForm");
  if (form) {
    // EmailJS config — à renseigner pour activer l'envoi côté client.
    var EMAILJS = { serviceId: "YOUR_SERVICE_ID", templateId: "YOUR_TEMPLATE_ID", publicKey: "YOUR_PUBLIC_KEY", to: "frederic@shorai-group.com" };
    if (window.emailjs && EMAILJS.publicKey !== "YOUR_PUBLIC_KEY") {
      try { emailjs.init(EMAILJS.publicKey); } catch (e) {}
    }
    var msg = document.getElementById("formMsg");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = {
        name: form.name.value.trim(),
        company: form.company ? form.company.value.trim() : "",
        email: form.email.value.trim(),
        phone: form.phone ? form.phone.value.trim() : "",
        message: form.message.value.trim()
      };
      if (!form.consent.checked) { show("Merci d'accepter le traitement de vos données.", "err"); return; }
      var btn = form.querySelector("[type=submit]");
      btn.disabled = true; var label = btn.textContent; btn.textContent = "Envoi…";

      function done(ok) {
        btn.disabled = false; btn.textContent = label;
        if (ok) { show("Merci. Nous revenons vers vous sous 24 h. — Frédéric", "ok"); form.reset(); }
        else { show("Un détail manque. Réessayez ou écrivez-nous directement.", "err"); }
      }

      if (window.emailjs && EMAILJS.publicKey !== "YOUR_PUBLIC_KEY") {
        emailjs.send(EMAILJS.serviceId, EMAILJS.templateId, {
          from_name: data.name, from_company: data.company, from_email: data.email,
          from_phone: data.phone, message: data.message, to_email: EMAILJS.to
        }).then(function () { done(true); }, function () { done(false); });
      } else {
        // Fallback : ouvrir le client mail
        var subj = encodeURIComponent("[shōrAI] Demande de " + data.name + (data.company ? " — " + data.company : ""));
        var body = encodeURIComponent(
          "Nom : " + data.name + "\nSociété : " + data.company + "\nEmail : " + data.email +
          "\nTéléphone : " + data.phone + "\n\n" + data.message
        );
        window.location.href = "mailto:" + EMAILJS.to + "?subject=" + subj + "&body=" + body;
        done(true);
      }
      function show(t, cls) { if (msg) { msg.textContent = t; msg.className = "form__msg " + cls; } }
    });
  }
})();
