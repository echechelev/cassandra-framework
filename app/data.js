// ========================================================================
//#region 1️⃣ ‍🚀 ДАННЫЕ ПОЛЬЗОВАТЕЛЕЙ (MOCK USERS)
// ========================================================================

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

// ========================================================================
//#region 2️⃣ 🌌 АСТРОНОМИЧЕСКИЕ ОБЪЕКТЫ (STAR-INFO)
// ========================================================================
window.sagittariusA = {
  id: "sagittarius-a",
  name: "Sagittarius A*",
  type: "black-hole",
  path: "MILKY WAY // SAGITTARIUS SECTOR",

  tech: {
    mass: "4.3 million M☉",
    radius: "24 million km (diameter)",
    temperature: "~10^7 K (accretion disk)",
    luminosity: "Low (quiescent)",
    distance: "26,000 ly"
  },

  info: {
    classification: "Supermassive Black Hole (SMBH)",
    spectralType: "N/A",
    age: "~13.8 billion years",
    location: "Sagittarius constellation",
    description: "This supermassive object acts as the gravitational anchor of the Milky Way's galactic center. Identified as a powerful radio source, it was directly imaged by the Event Horizon Telescope in May 2022. All stellar trajectories in this sector are strictly bound to its immense gravity well. The object exhibits minimal accretion activity despite its enormous mass, making it one of the most studied yet enigmatic structures in our galaxy.",
    warning: "Gravitational tidal forces exceed structural integrity limits. Do not cross the event horizon."
  },

  visual: {
    sphereClass: "black-hole",
    glowColor: "rgba(255, 140, 60, 0.6)"
  }
};

window.sun = {
  id: "sun",
  name: "Sol (The Sun)",
  type: "star",
  path: "MILKY WAY > ORION ARM > SOL SYSTEM",

  tech: {
    mass: "1.0 M☉ (Solar Masses)",
    radius: "696,340 km (109 Earth radii)",
    temperature: "5,778 K (Surface) / 15M K (Core)",
    luminosity: "1.0 L☉ (3.828 × 10^26 W)",
    distance: "1 AU / 149.6 million km)"
  },

  info: {
    classification: "G-type Yellow Dwarf",
    spectralType: "G2V",
    age: "~4.6 billion years",
    location: "Orion Arm, Milky Way Galaxy",
    description: "The central star of our planetary system, containing 99.86% of the system's total mass. It is a nearly perfect sphere of hot plasma, heated to incandescence by nuclear fusion reactions in its core. This stable energy output sustains all known life on Earth and drives the climate and weather systems of our home world. Currently in the middle of its main-sequence lifespan, it will eventually expand into a red giant in approximately 5 billion years.",
    warning: "Extreme thermal radiation and solar flare activity detected. Unshielded proximity will result in immediate catastrophic biological and structural failure."
  },

  visual: {
    sphereClass: "star-sphere sun",
    glowColor: "rgba(255, 200, 50, 0.8)"
  }
};

window.alphaCentauri = {
  id: "alpha-centauri",
  name: "Alpha Centauri A",
  type: "star-system",
  path: "MILKY WAY > ORION ARM > ALPHA CENTAURI",

  tech: {
    mass: "2.2 M☉ (Combined)",
    radius: "N/A (Triple System)",
    temperature: "5,790 K (Alpha Centauri A)",
    luminosity: "1.5 L☉ (Combined)",
    distance: "4.37 ly"
  },

  info: {
    classification: "Triple Star System",
    spectralType: "G2V + K1V + M5.5Ve",
    age: "~4.85 billion years",
    location: "Centaurus constellation",
    description: "The closest star system to our Solar System, located just 4.37 light-years away. It consists of three stars: Alpha Centauri A (a Sun-like yellow dwarf), Alpha Centauri B (an orange dwarf), and Proxima Centauri (a red dwarf). Proxima Centauri hosts at least one confirmed exoplanet in its habitable zone, making this system humanity's most promising target for future interstellar exploration and colonization efforts.",
    warning: "Complex gravitational dynamics detected in triple-star configuration. Navigation requires precise orbital calculations to avoid stellar collisions and gravitational capture."
  },

  visual: {
    sphereClass: "star-sphere alpha",
    glowColor: "rgba(255, 220, 100, 0.7)"
  }
};

window.epsilonEridani = {
  id: "epsilon-eridani",
  name: "Epsilon Eridani",
  type: "star",
  path: "MILKY WAY > ORION ARM > ERIDANUS SECTOR",

  tech: {
    mass: "0.82 M☉",
    radius: "73% of Solar Radius",
    temperature: "5,084 K (Surface)",
    luminosity: "0.34 L☉",
    distance: "10.48 ly"
  },

  info: {
    classification: "K-type Orange Dwarf",
    spectralType: "K2V",
    age: "~400-800 million years",
    location: "Eridanus constellation",
    description: "A young orange dwarf star located approximately 10.5 light-years from Earth, notable for its extensive debris disk resembling the early Solar System. It hosts at least one confirmed gas giant, Epsilon Eridani b, orbiting at roughly 3.4 AU. The system's youth and active debris field make it a prime laboratory for studying planetary formation processes and the evolution of young stellar environments.",
    warning: "High-density debris disk detected. Elevated risk of micrometeoroid impacts. Enhanced deflector shields and continuous trajectory monitoring required during approach."
  },

  visual: {
    sphereClass: "star-sphere epsilon",
    glowColor: "rgba(255, 160, 60, 0.7)"
  }
};

window.tauCeti = {
  id: "tau-ceti",
  name: "Tau Ceti",
  type: "star",
  path: "MILKY WAY > ORION ARM > CETUS SECTOR",

  tech: {
    mass: "0.783 M☉",
    radius: "79% of Solar Radius",
    temperature: "5,344 K (Surface)",
    luminosity: "0.52 L",
    distance: "11.91 ly"
  },

  info: {
    classification: "G-type Yellow Dwarf",
    spectralType: "G8V",
    age: "~5.8 billion years",
    location: "Cetus constellation",
    description: "A stable, metal-poor yellow dwarf remarkably similar to our Sun, located nearly 12 light-years away. The system contains at least four candidate super-Earths in or near its habitable zone, designated Tau Ceti e, f, g, and h. Its low stellar activity and long-term stability make it one of the most promising targets in the search for potentially habitable exoplanets and future human settlement.",
    warning: "Dense asteroid belt detected interior to habitable zone. Planetary candidates show elevated impact flux. Long-term surface habitation requires reinforced atmospheric shielding."
  },

  visual: {
    sphereClass: "star-sphere tau",
    glowColor: "rgba(255, 230, 120, 0.7)"
  }
};

window.teegarden = {
  id: "teegarden",
  name: "Teegarden's",
  type: "star",
  path: "MILKY WAY > AQUARIUS SECTOR > TRAPPIST-1",

  tech: {
    mass: "0.089 M☉",
    radius: "~11% of Solar Radius",
    temperature: "~2,600 K (Surface)",
    luminosity: "0.00073 L☉",
    distance: "12.48 ly"
  },

  info: {
    classification: "M-type Ultra-Cool Dwarf",
    spectralType: "M7V",
    age: "~8 billion years",
    location: "Aries constellation",
    description: "An extremely faint ultra-cool red dwarf, one of the smallest and dimmest stars known, located approximately 12.5 light-years from Earth. Despite its low luminosity, it hosts two confirmed Earth-sized planets, Teegarden b and c, both orbiting within the star's narrow habitable zone. The system's advanced age and quiet stellar activity profile make it a compelling candidate for the search for ancient, potentially evolved biospheres.",
    warning: "Extreme proximity required for habitable zone orbit due to low stellar luminosity. High risk of tidal locking and stellar flare exposure. Biological systems may experience circadian disruption."
  },

  visual: {
    sphereClass: "star-sphere teegarden",
    glowColor: "rgba(255, 80, 40, 0.6)"
  }
};

window.trappist1 = {
  id: "trappist-1",
  name: "TRAPPIST-1",
  type: "star-system",

  tech: {
    mass: "0.089 M☉",
    radius: "~12% of Solar Radius",
    temperature: "~2,566 K (Surface)",
    luminosity: "0.000522 L☉",
    distance: "40.66 ly"
  },

  info: {
    classification: "Ultra-Cool Planetary Dwarf",
    spectralType: "M8V",
    age: "~7.6 billion years",
    location: "Aquarius constellation",
    description: "An extraordinary ultra-cool red dwarf hosting seven Earth-sized rocky planets, the largest known collection of terrestrial worlds around a single star. At least three of these planets — TRAPPIST-1e, f, and g — orbit within the habitable zone and may possess conditions suitable for liquid water. The tightly packed orbital configuration and potential for atmospheric retention make this system a flagship target for the James Webb Space Telescope and future interstellar missions.",
    warning: "Seven-planet resonant chain creates complex gravitational interference. Tidal forces across the system are extreme. Close-proximity operations require continuous multi-body orbital recalibration."
  },

  visual: {
    sphereClass: "star-sphere trappist",
    glowColor: "rgba(255, 60, 30, 0.7)"
  }
};

// ========================================================================
//#region 3️⃣ 🌠 ЗВЕЗДНЫЕ СИСТЕМЫ (STAR SYSTEMS)
// ========================================================================

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
    designation: "Alpha Centauri A",
    classification: "G2V / K1V Binary Star System",
    mass: "2.2 M (Combined A & B)",
    distance: "4.37 ly",
    radius: "1.22 R☉ (Alpha Cen A)",
    surfaceTemp: "5,790 K (A) / 5,260 K (B)",
    age: "~4.85 billion years",
    name: "Alpha Centauri А",
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
