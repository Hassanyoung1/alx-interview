const https = require('https');

if (process.argv.length < 3) {
    console.error('Provide the movie Id');
    process.exit(1); // Exit with a non-zero status code to indicate an error
}

const movieID = process.argv[2];


