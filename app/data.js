window.MOCK_USERS = {
  ORION: {
    callsign: 'ORION',
    accessCode: 'NEBULA_7',
    role: 'Commander',
    fullName: 'Orion',
    roleIcon: '🏅',
    function: 'Command & Strategy',
    accessLevel: '1',
    id: '001-1A'
  },
  AURORA: {
    callsign: 'AURORA',
    accessCode: 'COMET_42',
    role: 'Specialist',
    fullName: 'Aurora',
    roleIcon: '🛰️',
    function: 'Comms & Diagnostics',
    accessLevel: '2',
    id: '884-2A'
  },
  KNOPA: {
    callsign: 'KNOPA',
    role: 'PILOT',
    fullName: 'Knopa',
    roleIcon: '✈️',
    function: 'Flight Operations',
    accessLevel: '1',
    recoveryCipher: 'AERO',
    id: '769-1A',
    accessCode: 'AERO_99'
  }
};

window.sagittariusA = {
  designation: "Sagittarius A* (Sgr A*)",
  classification: "Supermassive Black Hole (SMBH)",
  mass: "4.3 million M☉ (Solar Masses)",
  distance: "26,000 ly",
  eventHorizon: "~24 million km (Diameter)",
  status: "Quiescent (Low accretion rate)",
  overview:
    "The gravitational anchor of the Milky Way galaxy. " +
    "First directly imaged by the Event Horizon Telescope collaboration in May 2022. " +
    "All stellar trajectories in this sector are bound to its immense gravity well.",
  warning:
    "Gravitational tidal forces exceed structural integrity limits. " +
    "Do not cross the event horizon."
};

window.starDatabase = {
  "sun": {
    designation: "Sol",
    classification: "G2V Yellow Dwarf",
    mass: "1.989 × 10³⁰ kg",
    distance: "0 ly (Our home star)",
    radius: "696,340 km",
    surfaceTemp: "5,778 K",
    age: "~4.6 billion years",
    name: "Sol (Sun)",
    planets: 8,
    sphereClass: "sphere-sun",
    description: "The star at the center of our Solar System.",
    planetData: [
      { id: "mercury", name: "Mercury", emoji: "🌑", type: "Terrestrial", color: "#8c8c8c", size: "xs", distance: "0.39 AU", description: "Smallest and closest planet to the Sun." },
      { id: "venus", name: "Venus", emoji: "🌕", type: "Terrestrial", color: "#e3bb76", size: "s", distance: "0.72 AU", description: "Hottest planet with toxic atmosphere." },
      { id: "earth", name: "Earth", emoji: "", type: "Terrestrial", color: "#4da6ff", size: "s", distance: "1.00 AU", description: "Our home. The only known planet with life." },
      { id: "mars", name: "Mars", emoji: "", type: "Terrestrial", color: "#c1440e", size: "s", distance: "1.52 AU", description: "The Red Planet. Target for future colonization." },
      { id: "jupiter", name: "Jupiter", emoji: "", type: "Gas Giant", color: "#d8ca9d", size: "l", distance: "5.20 AU", description: "Largest planet in the Solar System." },
      { id: "saturn", name: "Saturn", emoji: "🪐", type: "Gas Giant", color: "#e8d191", size: "l", distance: "9.58 AU", description: "Famous for its extensive ring system." },
      { id: "uranus", name: "Uranus", emoji: "", type: "Ice Giant", color: "#4b70dd", size: "m", distance: "19.22 AU", description: "Rotates on its side. Pale blue ice giant." },
      { id: "neptune", name: "Neptune", emoji: "🔵", type: "Ice Giant", color: "#2e5c8a", size: "m", distance: "30.05 AU", description: "Windiest planet. Deep blue ice giant." }
    ]
  },

  "alpha-centauri": {
    designation: "Alpha Centauri",
    classification: "G2V / K1V Binary Star System",
    mass: "2.2 M (Combined A & B)",
    distance: "4.37 ly",
    radius: "1.22 R☉ (Alpha Cen A)",
    surfaceTemp: "5,790 K (A) / 5,260 K (B)",
    age: "~4.85 billion years",
    name: "Alpha Centauri",
    planets: 3,
    sphereClass: "sphere-alpha",
    description: "The closest star system to the Solar System.",
    planetData: [
      { id: "proxima-b", name: "Proxima b", emoji: "", type: "Terrestrial", color: "#a65e5e", size: "s", distance: "0.048 AU", description: "Potentially habitable exoplanet in the Goldilocks zone." },
      { id: "proxima-c", name: "Proxima c", emoji: "❄️", type: "Super-Earth", color: "#88aaff", size: "m", distance: "1.49 AU", description: "Cold, distant super-Earth candidate." },
      { id: "proxima-d", name: "Proxima d", emoji: "🌑", type: "Sub-Earth", color: "#777777", size: "xs", distance: "0.029 AU", description: "One of the lightest known exoplanets." }
    ]
  },

  "epsilon-eridani": {
    designation: "Epsilon Eridani",
    classification: "K2V Orange Dwarf",
    mass: "0.82 M",
    distance: "10.5 ly",
    radius: "0.735 R☉",
    surfaceTemp: "5,084 K",
    age: "~0.8 billion years",
    name: "Epsilon Eridani",
    planets: 2,
    sphereClass: "sphere-epsilon",
    description: "A young orange dwarf star with a confirmed debris disk and two known planetary companions.",
    planetData: [
      { id: "epsilon-eridani-b", name: "Epsilon Eridani b", emoji: "🪐", type: "Gas Giant", color: "#cc8844", size: "l", distance: "3.39 AU", description: "Confirmed Jupiter-like exoplanet in an eccentric orbit." },
      { id: "epsilon-eridani-c", name: "Epsilon Eridani c", emoji: "", type: "Super-Earth", color: "#aa6633", size: "m", distance: "40 AU", description: "Candidate super-Earth in the outer system, near the debris belt." }
    ]
  },

  "tau-ceti": {
    designation: "Tau Ceti",
    classification: "G8V Yellow-Orange Dwarf",
    mass: "0.783 M",
    distance: "11.9 ly",
    radius: "0.793 R☉",
    surfaceTemp: "5,344 K",
    age: "~5.8 billion years",
    name: "Tau Ceti",
    planets: 4,
    sphereClass: "sphere-tau",
    description: "One of the closest Sun-like stars. A prime target in the search for extraterrestrial life.",
    planetData: [
      { id: "tau-ceti-e", name: "Tau Ceti e", emoji: "", type: "Super-Earth", color: "#d4a055", size: "m", distance: "0.552 AU", description: "Potentially habitable super-Earth near the inner edge of the Goldilocks zone." },
      { id: "tau-ceti-f", name: "Tau Ceti f", emoji: "", type: "Super-Earth", color: "#b88c44", size: "m", distance: "1.35 AU", description: "Super-Earth candidate within the conservative habitable zone." },
      { id: "tau-ceti-g", name: "Tau Ceti g", emoji: "", type: "Super-Earth", color: "#a07a33", size: "m", distance: "0.538 AU", description: "Innermost candidate planet, likely too hot for liquid water." },
      { id: "tau-ceti-h", name: "Tau Ceti h", emoji: "", type: "Super-Earth", color: "#886622", size: "m", distance: "1.78 AU", description: "Outer candidate planet at the edge of the habitable zone." }
    ]
  },

  "teegarden": {
    designation: "Teegarden's",
    classification: "M7V Red Dwarf",
    mass: "0.089 M☉",
    distance: "12.5 ly",
    radius: "0.114 R☉",
    surfaceTemp: "2,900 K",
    age: "~8 billion years",
    name: "Teegarden's Star",
    planets: 2,
    sphereClass: "sphere-teegarden",
    description: "An ultra-cool red dwarf with extremely low luminosity. Hosts two Earth-sized planets.",
    planetData: [
      { id: "teegarden-b", name: "Teegarden b", emoji: "", type: "Terrestrial", color: "#cc4444", size: "s", distance: "0.025 AU", description: "Earth-sized planet in the habitable zone. High probability of liquid water." },
      { id: "teegarden-c", name: "Teegarden c", emoji: "", type: "Terrestrial", color: "#aa3333", size: "s", distance: "0.044 AU", description: "Second Earth-sized planet, likely tidally locked." }
    ]
  },

  "trappist-1": {
    designation: "TRAPPIST-1",
    classification: "M8V Ultra-Cool Red Dwarf",
    mass: "0.0898 M",
    distance: "40.7 ly",
    radius: "0.121 R☉",
    surfaceTemp: "2,566 K",
    age: "~7.6 billion years",
    name: "TRAPPIST-1",
    planets: 7,
    sphereClass: "sphere-trappist",
    description: "The most famous compact planetary system. Seven Earth-sized worlds packed closely together.",
    planetData: [
      { id: "trappist-1b", name: "TRAPPIST-1b", emoji: "", type: "Terrestrial", color: "#dd5555", size: "s", distance: "0.011 AU", description: "Innermost planet. Likely tidally locked with scorching dayside." },
      { id: "trappist-1c", name: "TRAPPIST-1c", emoji: "", type: "Terrestrial", color: "#cc4444", size: "s", distance: "0.016 AU", description: "Rocky world receiving twice the radiation Earth gets from the Sun." },
      { id: "trappist-1d", name: "TRAPPIST-1d", emoji: "", type: "Terrestrial", color: "#bb3333", size: "s", distance: "0.022 AU", description: "Lightest planet in the system. Possibly has a thin atmosphere." },
      { id: "trappist-1e", name: "TRAPPIST-1e", emoji: "", type: "Terrestrial", color: "#aa2222", size: "s", distance: "0.029 AU", description: "Most likely to be habitable. Receives similar energy flux to Earth." },
      { id: "trappist-1f", name: "TRAPPIST-1f", emoji: "", type: "Terrestrial", color: "#992222", size: "s", distance: "0.038 AU", description: "Cold terrestrial world. May harbor subsurface oceans under ice." },
      { id: "trappist-1g", name: "TRAPPIST-1g", emoji: "", type: "Terrestrial", color: "#881111", size: "s", distance: "0.046 AU", description: "Largest planet in the system. Potentially icy with a thick atmosphere." },
      { id: "trappist-1h", name: "TRAPPIST-1h", emoji: "", type: "Terrestrial", color: "#770000", size: "xs", distance: "0.062 AU", description: "Outermost planet. Frozen world beyond the traditional habitable zone." }
    ]
  }
};
