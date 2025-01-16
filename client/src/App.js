import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './index.css';

const App = () => {
    const [characters, setCharacters] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Fetch characters from the backend
        axios.get('http://127.0.0.1:8000/genshin_characters')
            .then(response => {
                setCharacters(response.data.characters);
                setLoading(false);
            })
            .catch(err => {
                setError('Failed to fetch data');
                setLoading(false);
            });
    }, []);

    if (loading) return <div className="text-center mt-10">Loading...</div>;
    if (error) return <div className="text-center mt-10 text-red-500">{error}</div>;

    return (
        <div className="bg-gray-100 min-h-screen p-5">
            <h1 className="text-3xl font-bold text-center text-gray-800 mb-8">Genshin Impact Characters</h1>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                {characters.map((character, index) => (
                    <div key={index} className="bg-white shadow-md rounded-lg overflow-hidden hover:shadow-xl transition-shadow duration-300">
                        <img 
                            src={character.Icon || 'https://via.placeholder.com/150'} 
                            alt={character.Name} 
                            className="w-full h-48 object-cover"
                        />
                        <div className="p-4">
                            <h2 className="text-lg font-semibold text-gray-800">{character.Name}</h2>
                            <p className="text-sm text-gray-600">Quality: {character.Quality}</p>
                            <p className="text-sm text-gray-600">Element: {character.Element}</p>
                            <p className="text-sm text-gray-600">Weapon: {character.Weapon}</p>
                            <p className="text-sm text-gray-600">Region: {character.Region}</p>
                            <p className="text-sm text-gray-600">Model Type: {character['Model Type']}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default App;
