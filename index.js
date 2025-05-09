const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Base directory (where this file and HTML files reside)
const baseDir = __dirname;

// Serve static files (HTML, CSS, JS, images if any)
app.use(express.static(baseDir));

app.get('/', (req, res) => {
  res.redirect('/starting');
});

app.get('/starting', (req, res) => {
  res.sendFile(path.join(baseDir, 'index.html'));
});

app.get('/lobby', (req, res) => {
  res.sendFile(path.join(baseDir, 'lobby.html'));
});

app.get('/training', (req, res) => {
  res.sendFile(path.join(baseDir, 'train.html'));
});

app.get('/play', (req, res) => {
  res.sendFile(path.join(baseDir, 'game.html'));
});

app.get('/share', (req, res) => {
  res.sendFile(path.join(baseDir, 'share.html'));
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
