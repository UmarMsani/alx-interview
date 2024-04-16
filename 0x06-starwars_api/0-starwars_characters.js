#!/usr/bin/node

const request = require('request');


function fetchCharacters(movieId) {
    const apiUrl = `https://swapi.dev/api/films/${movieId}/`;
    
    request(apiUrl, (error, response, body) => {
        if (error) {
            console.error('Error:', error);
            return;
        }
        
        if (response.statusCode !== 200) {
            console.error('API request failed with status code:', response.statusCode);
            return;
        }
        
        const filmData = JSON.parse(body);
        const characters = filmData.characters;
        
        characters.forEach(characterUrl => {
            request(characterUrl, (error, response, body) => {
                if (error) {
                    console.error('Error:', error);
                    return;
                }
                
                if (response.statusCode !== 200) {
                    console.error('API request failed with status code:', response.statusCode);
                    return;
                }
                
                const characterData = JSON.parse(body);
                console.log(characterData.name);
            });
        });
    });
}


function main() {
    const movieId = process.argv[2];
    
    if (!movieId || isNaN(movieId)) {
        console.error('Usage: node script.js <Movie ID>');
        process.exit(1);
    }
    
    fetchCharacters(movieId);
}

main();
