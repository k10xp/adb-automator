function runCommands() {
  const outputDiv = document.getElementsByClassName("commands-output-text")[0];

  const checkboxes = document.querySelectorAll(
    '.commands-checkbox-container input[type="checkbox"]'
  );

  //append, always in commands list order
  //ie Screen On is always 1st
  const lines = [];
  checkboxes.forEach((cb) => {
    if (cb.checked) {
      const labelText = cb.parentElement.textContent.trim();
      lines.push("Running: " + labelText);
    }
  });

  //show on R panel
  if (lines.length === 0) {
    lines.push("No commands selected.");
  }

  outputDiv.innerHTML = "";
  lines.forEach((text) => {
    const p = document.createElement("p");
    p.textContent = text;
    outputDiv.appendChild(p);
  });
}

function showHelp() {
  alert('Select commands, then click "Run Commands" to run them.');
}
