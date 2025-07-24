fetch("http://localhost:5000/summarize", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ text: userInput })
})
  .then(res => res.json())
  .then(data => setSummary(data.summary))
  .catch(err => console.error(err));
