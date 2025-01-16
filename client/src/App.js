import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './index.css';

const ElementColors = {
  Pyro: 'text-red-500',
  Hydro: 'text-blue-500',
  Anemo: 'text-green-500',
  Electro: 'text-purple-500',
  Dendro: 'text-lime-500',
  Cryo: 'text-cyan-500',
  Geo: 'text-yellow-500',
};

const WeaponIcons = {
  Sword: '⚔️',
  Claymore: '🗡️',
  Polearm: '🔱',
  Catalyst: '📘',
  Bow: '🏹',
};

const App = () => {
  const [characters, setCharacters] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
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

  const renderStars = (quality) => {
    const starCount = parseInt(quality.split(' ')[0]);
    return '★'.repeat(starCount) + '☆'.repeat(5 - starCount);
  };

  if (loading) return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
    </div>
  );

  if (error) return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="text-center p-8 bg-white rounded-lg shadow-lg">
        <h2 className="text-2xl font-bold text-red-500 mb-4">Error</h2>
        <p className="text-gray-700">{error}</p>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen p-8 bg-gradient-to-br from-blue-100 to-purple-100">
      <h1 className="text-4xl font-bold text-center text-gray-800 mb-12">Genshin Impact Characters</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">
        {characters.map((character, index) => (
          <div key={index} className="bg-white rounded-xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2">
            <div className="relative">
              <img 
                src={character.Icon || '/placeholder.svg?height=200&width=200'} 
                alt={character.Name} 
                className="w-full h-56 object-cover"
              />
              <div className="absolute top-0 right-0 bg-white bg-opacity-80 rounded-bl-lg p-2">
                <span className={`text-lg font-semibold ${ElementColors[character.Element] || 'text-gray-800'}`}>
                  {character.Element}
                </span>
              </div>
            </div>
            <div className="p-6">
              <div className="flex justify-between items-center mb-2">
                <h2 className="text-2xl font-bold text-gray-800">{character.Name}</h2>
                <span className="text-yellow-500 text-lg" title={`${character.Quality} Character`}>
                  {renderStars(character.Quality)}
                </span>
              </div>
              <div className="flex justify-between items-center text-sm text-gray-700 mb-4">
                <span>
                  <span className="font-semibold">Weapon:</span> {WeaponIcons[character.Weapon]} {character.Weapon}
                </span>
                <span>
                  <span className="font-semibold">Region:</span> {character.Region}
                </span>
              </div>
              <p className="text-sm text-gray-600">
                <span className="font-semibold">Model Type:</span> {character['Model Type']}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;


