const path = require('path');
const express = require('express');
const rootDir = require('../util/path');

const router = express.Router();

router.get('/samples', (req, res, next) => {
    res.sendFile(path.join(rootDir, 'views', 'samples.html'));
});

module.exports = router;