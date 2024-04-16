#!/usr/bin/node

const request = require('request');

// Function to fetch character data
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

// Function to fetch characters of a Star Wars movie
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

        // Fetch all character names concurrently
        const characterNames = await Promise.all(characters.map(fetchCharacterData));

        // Print character names
        characterNames.forEach(name => console.log(name));
    } catch (error) {
        console.error('Error:', error);
    }
}

// Main function
function main() {
    const movieId = process.argv[2];
    
    if (!movieId || isNaN(movieId)) {
        console.error('Usage: ./0-starwars_characters.js <Movie ID>');
        process.exit(1);
    }
    
    fetchCharacters(movieId);
}

// Call main function
main();
