const sizeSlider = document.getElementById("size");
const sizeValue = document.getElementById("sizeValue");
const form = document.querySelector("form");
const dataInput = document.querySelector("input[name='data']");

// Show Slider Value
if (sizeSlider && sizeValue) {
  sizeValue.textContent = sizeSlider.value;

  sizeSlider.addEventListener("input", () => {
    sizeValue.textContent = sizeSlider.value;
  });
}

// Form Validation
form.addEventListener("submit", function (e) {
  const value = dataInput.value.trim();

  if (value === "") {
    e.preventDefault();
    alert("Please enter URL or Text!");
    dataInput.focus();
    return;
  }

  // Disable Button while generating
  const btn = form.querySelector("button");
  btn.disabled = true;
  btn.innerHTML = "Generating...";

  // Enable again after few seconds
  setTimeout(() => {
    btn.disabled = false;
    btn.innerHTML = "Generate QR";
  }, 3000);
});

// Input Animation
dataInput.addEventListener("focus", () => {
  dataInput.style.transform = "scale(1.02)";
});

dataInput.addEventListener("blur", () => {
  dataInput.style.transform = "scale(1)";
});
