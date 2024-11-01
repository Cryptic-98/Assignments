const amount = document.getElementById("amount");

let USD = 18.24;
let EUR = 19.89;
let GBP = 23.6;
let JPY = 0.12;
let AUD = 12.22;
let CAD = 13.31;
let CHF = 20.56;
let CNY = 2.51;
let INR = 0.22;

function convert() {
  const amount_converting = Number(amount.value);
  let in_usd = amount_converting * USD;
  let in_eur = amount_converting * EUR;
  let in_gbp = amount_converting * GBP;
  let in_jpy = amount_converting * JPY;
  let in_aud = amount_converting * AUD;
  let in_cad = amount_converting * CAD;
  let in_chf = amount_converting * CHF;
  let in_cny = amount_converting * CNY;
  let in_inr = amount_converting * INR;
  document.getElementById("currency_usd").innerText = "USD";
  document.getElementById("currency_eur").innerText = "EUR";
  document.getElementById("currency_gbp").innerText = "GBP";
  document.getElementById("currency_jpy").innerText = "JPY";
  document.getElementById("currency_aud").innerText = "AUD";
  document.getElementById("currency_cad").innerText = "CAD";
  document.getElementById("currency_chf").innerText = "CHF";
  document.getElementById("currency_cny").innerText = "CNY";
  document.getElementById("currency_inr").innerText = "INR";
  document.getElementById("exchange_rate_usd").innerText = USD;
  document.getElementById("exchange_rate_eur").innerText = EUR;
  document.getElementById("exchange_rate_gbp").innerText = GBP;
  document.getElementById("exchange_rate_jpy").innerText = JPY;
  document.getElementById("exchange_rate_aud").innerText = AUD;
  document.getElementById("exchange_rate_cad").innerText = CAD;
  document.getElementById("exchange_rate_chf").innerText = CHF;
  document.getElementById("exchange_rate_cny").innerText = CNY;
  document.getElementById("exchange_rate_inr").innerText = INR;
  document.getElementById("converted_amount_usd").innerText = in_usd.toFixed(2);
  document.getElementById("converted_amount_eur").innerText = in_eur.toFixed(2);
  document.getElementById("converted_amount_gbp").innerText = in_gbp.toFixed(2);
  document.getElementById("converted_amount_jpy").innerText = in_jpy.toFixed(2);
  document.getElementById("converted_amount_aud").innerText = in_aud.toFixed(2);
  document.getElementById("converted_amount_cad").innerText = in_cad.toFixed(2);
  document.getElementById("converted_amount_chf").innerText = in_chf.toFixed(2);
  document.getElementById("converted_amount_cny").innerText = in_cny.toFixed(2);
  document.getElementById("converted_amount_inr").innerText = in_inr.toFixed(2);
}
