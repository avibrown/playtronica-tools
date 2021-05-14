const path = require('path');
const express = require('express');

const playRoutes = require('./routes/play');
const samplesRoutes = require('./routes/samples');

const app = express();

app.use('/', playRoutes.routes);
app.use(samplesRoutes);

app.listen(3000);