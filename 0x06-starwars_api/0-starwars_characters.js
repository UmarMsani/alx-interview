#!/usr/bin/node

const request = require('request');

function fetchCharacterData(characterUrl) {
    return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
            if (error || response.statusCode !== 200) {
                reject(error || `API request failed with status code ${response.statusCode}`);
                return;
            }
            
            const characterData = JSON.parse(body);
            resolve(characterData.name);
        });
    });
}

async function fetchCharacters(movieId) {
    const apiUrl = `https://swapi.dev/api/films/${movieId}/`;
    
    try {
        const filmDataResponse = await new Promise((resolve, reject) => {
            request(apiUrl, (error, response, body) => {
                if (error || response.statusCode !== 200) {
                    reject(error || `API request failed with status code ${response.statusCode}`);
                    return;
                }
                resolve(body);
            });
        });

        const filmData = JSON.parse(filmDataResponse);
        const characters = filmData.characters;

        const characterNames = await Promise.all(characters.map(fetchCharacterData));

        characterNames.forEach(name => console.log(name));
    } catch (error) {
        console.error('Error:', error);
    }
}

function main() {
    const movieId = process.argv[2];
    
    if (!movieId || isNaN(movieId)) {
        console.error('Usage: ./0-starwars_characters.js <Movie ID>');
        process.exit(1);
    }
    
    fetchCharacters(movieId);
}

main();
