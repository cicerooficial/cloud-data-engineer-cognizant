const mysql = require('mysql');

const Connection = mysql.createConnection({
    host: 'localhost',
    user: 'ch',
    password: '04917180',
    database: 'movies-controll'
})

module.exports = Connection;
