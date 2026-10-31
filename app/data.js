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

//#endregion

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
  id: "alpha-centauri-a",
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

//#endregion

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

  "alpha-centauri-a": {
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

//#endregion

// ========================================================================
//#region 4️ 🌌 ДАННЫЕ ПЛАНЕТ ДЛЯ СТРАНИЦЫ PLANET
// ========================================================================

window.PlanetMetricsSun = [
  {
    id: "mercury",
    mass: "0.055 M⊕",
    radius: "2,439 km",
    gravity: "3.7 m/s²",
    temperature: "167 °C",
    pressure: "~0 Pa",
    orbitalPeriod: "88 days",
    rotationPeriod: "58.6 days",
    distance: "0.39 AU",
    description: "The smallest planet in the Solar System and closest to the Sun. Its orbital period around the Sun is 87.97 Earth days — the shortest of all planets. Surface is heavily cratered, resembling Earth's Moon. No atmosphere to retain heat, causing extreme temperature swings from -180°C to 430°C.",
    missionStatus: "NO LANDINGS",
    missionText: "Multiple flybys completed. Mariner 10 (1974-1975), MESSENGER (2011-2015). No surface missions due to extreme temperatures and solar radiation.",
    missionIcon: "🛸"
  },
  {
    id: "venus",
    mass: "0.815 M",
    radius: "6,051 km",
    gravity: "8.87 m/s²",
    temperature: "464 °C",
    pressure: "92 bar",
    orbitalPeriod: "225 days",
    rotationPeriod: "243 days",
    distance: "0.72 AU",
    description: "The second planet from the Sun, often called Earth's 'sister planet' due to similar size. It has the densest atmosphere of the terrestrial planets — 96.5% CO₂, creating a runaway greenhouse effect. Surface pressure is 92 times that of Earth. Rotates in the opposite direction to most planets.",
    missionStatus: "MULTIPLE LANDINGS",
    missionText: "Venera 13 (1982) — 127 minutes survival. Venera 14 (1982) — 57 minutes. Harsh surface conditions (464°C, 92 bar) limit mission duration.",
    missionIcon: "🪐"
  },
  {
    id: "earth",
    mass: "1 M⊕",
    radius: "6,371 km",
    gravity: "9.8 m/s²",
    temperature: "15 °C",
    pressure: "1 bar",
    orbitalPeriod: "365.25 days",
    rotationPeriod: "24 hours",
    distance: "1 AU",
    description: "The third planet from the Sun and the only known planet to harbor life. 71% of the surface is covered by water. Dense atmosphere composed of nitrogen (78%) and oxygen (21%). Protected by a strong magnetic field that shields the surface from harmful solar radiation.",
    missionStatus: "HOME PLANET",
    missionText: "Continuous human habitation. Origin point of all space exploration. No exploration status applicable.",
    missionIcon: "",
    isHomePlanet: true
  },
  {
    id: "mars",
    mass: "0.107 M",
    radius: "3,389 km",
    gravity: "3.72 m/s²",
    temperature: "-65 °C",
    pressure: "0.006 bar",
    orbitalPeriod: "687 days",
    rotationPeriod: "24.6 hours",
    distance: "1.52 AU",
    description: "The fourth planet from the Sun, known as the 'Red Planet' due to iron oxide (rust) on its surface. Home to Olympus Mons, the largest volcano in the Solar System, and Valles Marineris, a canyon system stretching 4,000 km. Thin CO₂ atmosphere. Evidence of ancient liquid water flows.",
    missionStatus: "ACTIVE OPERATIONS",
    missionText: "Perseverance (2021-present), Curiosity (2012-present), InSight (2018-2022). Multiple successful landings and ongoing surface operations.",
    missionIcon: "🤖"
  },
  {
    id: "uranus",
    mass: "14.5 M",
    radius: "25,362 km",
    gravity: "8.87 m/s²",
    temperature: "-195 °C",
    pressure: "~1.2 bar",
    orbitalPeriod: "84 years",
    rotationPeriod: "17.2 hours",
    distance: "19.2 AU",
    description: "The seventh planet from the Sun, an ice giant with a unique axial tilt of 98° — it essentially rotates on its side. Atmosphere composed of hydrogen, helium, and methane, giving it a pale blue-green color. Has 13 known rings and 27 known moons.",
    missionStatus: "FLYBY ONLY",
    missionText: "Voyager 2 flyby (January 1986). No dedicated missions. Extreme distance and harsh conditions prevent landing attempts.",
    missionIcon: "🛸"
  },
  {
    id: "neptune",
    mass: "17.1 M⊕",
    radius: "24,622 km",
    gravity: "11.15 m/s²",
    temperature: "-200 °C",
    pressure: "~1.2 bar",
    orbitalPeriod: "165 years",
    rotationPeriod: "16.1 hours",
    distance: "30.1 AU",
    description: "The eighth and farthest known planet from the Sun, an ice giant similar to Uranus. Known for supersonic winds reaching 2,100 km/h — the fastest in the Solar System. Deep blue color from methane in its atmosphere. Has 14 known moons, including Triton with its geysers of nitrogen.",
    missionStatus: "FLYBY ONLY",
    missionText: "Voyager 2 flyby (August 1989). No dedicated missions. Extreme distance prevents landing attempts.",
    missionIcon: "🛸"
  }
];

window.PlanetMetricsAlphaCentauriA = [
  {
    id: "proxima-b",
    mass: "~1.2 M⊕",
    radius: "~1.1 R⊕",
    gravity: "~10.8 m/s²",
    temperature: "-39 °C",
    pressure: "Unknown",
    orbitalPeriod: "11.2 days",
    rotationPeriod: "Tidally locked",
    distance: "4.246 ly",
    description: "The closest known exoplanet to the Solar System, orbiting within the habitable zone of Proxima Centauri. Likely a rocky world with a mass slightly larger than Earth. Subject to intense stellar flares from its host red dwarf star.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (4.246 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "📡",
    unreachable: true
  },
  {
    id: "proxima-c",
    mass: "~7 M",
    radius: "~2.5 R",
    gravity: "~1.1 g",
    temperature: "-234 °C",
    pressure: "Unknown",
    orbitalPeriod: "5.2 years",
    rotationPeriod: "Unknown",
    distance: "4.246 ly",
    description: "A super-Earth or mini-Neptune candidate orbiting much further out in the Proxima Centauri system. Extremely cold due to its wide orbit. Its existence is still debated among astronomers, but it remains a compelling target for future astrometry.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (4.246 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "📡",
    unreachable: true
  },
  {
    id: "proxima-d",
    mass: "~0.26 M⊕",
    radius: "~0.81 R⊕",
    gravity: "~3.9 m/s²",
    temperature: "-13 °C",
    pressure: "Unknown",
    orbitalPeriod: "5.1 days",
    rotationPeriod: "Unknown",
    distance: "4.246 ly",
    description: "One of the lightest exoplanets ever discovered, with a mass roughly a quarter of Earth's. Orbits very close to Proxima Centauri, completing a revolution in just over 5 days. Too close to the star to support liquid water on its surface.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (4.246 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "📡",
    unreachable: true
  }
];

window.PlanetMetricsTauCeti = [
  {
    id: "tau-ceti-e",
    mass: "~4.29 M⊕",
    radius: "~1.78 R⊕",
    gravity: "~1.35 g",
    temperature: "~23 °C",
    pressure: "Unknown",
    orbitalPeriod: "168 days",
    rotationPeriod: "Unknown",
    distance: "11.9 ly",
    description: "A super-Earth located in the habitable zone of Tau Ceti. With a calculated mean temperature of ~23°C, it could potentially support liquid water if atmospheric conditions are favorable. Its mass suggests a rocky composition with possible thick atmosphere.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (11.9 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "📡",
    unreachable: true
  },
  {
    id: "tau-ceti-f",
    mass: "~3.93 M⊕",
    radius: "~1.73 R⊕",
    gravity: "~1.31 g",
    temperature: "-17 °C",
    pressure: "Unknown",
    orbitalPeriod: "642 days",
    rotationPeriod: "Unknown",
    distance: "11.9 ly",
    description: "Another super-Earth in the outer edge of Tau Ceti's habitable zone. With an orbital period of 642 days and mean temperature of -17°C, it may have subsurface oceans beneath an icy crust. Prime candidate for astrobiology studies.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (11.9 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "📡",
    unreachable: true
  },
  {
    id: "tau-ceti-g",
    mass: "~1.75 M⊕",
    radius: "~1.25 R⊕",
    gravity: "~1.11 g",
    temperature: "-40 °C",
    pressure: "Unknown",
    orbitalPeriod: "20 days",
    rotationPeriod: "Unknown",
    distance: "11.9 ly",
    description: "A mini-Neptune or large rocky world orbiting close to Tau Ceti with a rapid 20-day period. Its proximity to the star and low temperature suggest a thin or absent atmosphere. Likely tidally locked with extreme temperature gradients.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (11.9 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "",
    unreachable: true
  },
  {
    id: "tau-ceti-h",
    mass: "~1.83 M⊕",
    radius: "~1.27 R",
    gravity: "~1.13 g",
    temperature: "-50 °C",
    pressure: "Unknown",
    orbitalPeriod: "49 days",
    rotationPeriod: "Unknown",
    distance: "11.9 ly",
    description: "A super-Earth with a 49-day orbital period, positioned between the inner and outer regions of Tau Ceti's system. Cold surface temperatures and unknown atmospheric composition make it a challenging but intriguing target for future spectroscopic analysis.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (11.9 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "📡",
    unreachable: true
  }
];

window.PlanetMetricsEpsilonEridani = [
  {
    id: "epsilon-eridani-c",
    mass: "~248 M⊕",
    radius: "~12.1 R",
    gravity: "~20.5 m/s²",
    temperature: "-143 °C",
    pressure: "Unknown",
    orbitalPeriod: "6.85 years",
    rotationPeriod: "Unknown",
    distance: "10.5 ly",
    description: "A massive gas giant orbiting Epsilon Eridani, often compared to Jupiter in our own Solar System. With a mass nearly 250 times that of Earth and an orbital period of 6.85 years, it is a cold, turbulent world dominated by hydrogen and helium. Its immense gravity and lack of a solid surface make physical landing impossible.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (10.5 ly) and its nature as a gas giant. Deep-space telemetry and remote observation only.",
    missionIcon: "",
    unreachable: true
  }
];

window.PlanetMetricsTeegarden = [
  {
    id: "teegarden-b",
    mass: "~1.05 M⊕",
    radius: "~1.02 R⊕",
    gravity: "~9.9 m/s²",
    temperature: "~28 °C",
    pressure: "Unknown",
    orbitalPeriod: "4.9 days",
    rotationPeriod: "Tidally locked",
    distance: "12.5 ly",
    description: "One of the most Earth-like exoplanets ever discovered, with a mass and radius almost identical to Earth. It orbits within the habitable zone of Teegarden's Star, a cool red dwarf. Due to its close 4.9-day orbit, it is likely tidally locked, meaning one side permanently faces the star while the other remains in eternal darkness.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (12.5 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "📡",
    unreachable: true
  },
  {
    id: "teegarden-c",
    mass: "~1.11 M⊕",
    radius: "~1.04 R⊕",
    gravity: "~10.2 m/s²",
    temperature: "-47 °C",
    pressure: "Unknown",
    orbitalPeriod: "11.4 days",
    rotationPeriod: "Tidally locked",
    distance: "12.5 ly",
    description: "A rocky super-Earth located at the outer edge of the habitable zone. With a mean temperature of -47°C, it is significantly colder than its sibling, Teegarden's Star b. Like its neighbor, it is tidally locked, creating extreme temperature contrasts between its day and night sides.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (12.5 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "📡",
    unreachable: true
  }
];

window.PlanetMetricsTrappist1 = [
  {
    id: "trappist-1b",
    mass: "~1.02 M⊕",
    radius: "~1.12 R⊕",
    gravity: "~0.81 g",
    temperature: "~127 °C",
    pressure: "Unknown",
    orbitalPeriod: "1.51 days",
    rotationPeriod: "Tidally locked",
    distance: "40.7 ly",
    description: "The innermost known planet of the TRAPPIST-1 system. With a mean temperature of ~127°C, it is far too hot to support liquid water on its surface. Likely a rocky world similar in size to Earth, completely tidally locked to its host star.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (40.7 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "📡",
    unreachable: true
  },
  {
    id: "trappist-1c",
    mass: "~1.16 M⊕",
    radius: "~1.10 R⊕",
    gravity: "~0.97 g",
    temperature: "~107 °C",
    pressure: "Unknown",
    orbitalPeriod: "2.42 days",
    rotationPeriod: "Tidally locked",
    distance: "40.7 ly",
    description: "The second planet from the star, still well inside the habitable zone. Recent observations suggest it lacks a thick atmosphere, making it a barren, rocky world with extreme temperature gradients between its day and night sides.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (40.7 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "📡",
    unreachable: true
  },
  {
    id: "trappist-1d",
    mass: "~0.30 M⊕",
    radius: "~0.79 R⊕",
    gravity: "~0.48 g",
    temperature: "~15 °C",
    pressure: "Unknown",
    orbitalPeriod: "4.05 days",
    rotationPeriod: "Tidally locked",
    distance: "40.7 ly",
    description: "The smallest planet in the system, located right at the inner edge of the habitable zone. Its calculated mean temperature of ~15°C is remarkably similar to Earth's. If it possesses a sufficient atmosphere, it could harbor liquid water.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (40.7 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "📡",
    unreachable: true
  },
  {
    id: "trappist-1e",
    mass: "~0.77 M",
    radius: "~0.92 R⊕",
    gravity: "~0.91 g",
    temperature: "-22 °C",
    pressure: "Unknown",
    orbitalPeriod: "6.10 days",
    rotationPeriod: "Tidally locked",
    distance: "40.7 ly",
    description: "Widely considered the most Earth-like planet in the TRAPPIST-1 system. Located squarely in the middle of the habitable zone, it has a rocky composition and density very similar to Earth. The prime candidate for potential extraterrestrial life.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (40.7 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "📡",
    unreachable: true
  },
  {
    id: "trappist-1f",
    mass: "~0.93 M",
    radius: "~1.05 R⊕",
    gravity: "~0.86 g",
    temperature: "-54 °C",
    pressure: "Unknown",
    orbitalPeriod: "9.21 days",
    rotationPeriod: "Tidally locked",
    distance: "40.7 ly",
    description: "Located in the outer region of the habitable zone. Colder than its inner siblings, it may be covered by a global ocean beneath an icy crust. A fascinating target for astrobiology, as subsurface life could thrive in its dark oceans.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (40.7 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "",
    unreachable: true
  },
  {
    id: "trappist-1g",
    mass: "~1.15 M⊕",
    radius: "~1.13 R⊕",
    gravity: "~0.90 g",
    temperature: "-74 °C",
    pressure: "Unknown",
    orbitalPeriod: "12.35 days",
    rotationPeriod: "Tidally locked",
    distance: "40.7 ly",
    description: "The largest planet in the system, situated near the outer edge of the habitable zone. Likely an 'eyeball planet' — a world with a frozen night side and a small region of liquid water on the day side, or completely covered in ice.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (40.7 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "📡",
    unreachable: true
  },
  {
    id: "trappist-1h",
    mass: "~0.33 M⊕",
    radius: "~0.76 R",
    gravity: "~0.58 g",
    temperature: "-100 °C",
    pressure: "Unknown",
    orbitalPeriod: "18.77 days",
    rotationPeriod: "Tidally locked",
    distance: "40.7 ly",
    description: "The outermost known planet in the system. With a mean temperature of -100°C, it is far too cold to support surface liquid water. Likely a frozen, icy world similar to the outer moons of our own Solar System.",
    missionStatus: "BEYOND REACH",
    missionText: "Physical landing currently impossible due to extreme interstellar distance (40.7 ly). Deep-space telemetry and remote observation only.",
    missionIcon: "📡",
    unreachable: true
  }
];

//#endregion

// ========================================================================
//#region 5️⃣ 🚀 ДАННЫЕ ДЛЯ КАЛЬКУЛЯТОРА ПОЛЕТОВ
// ========================================================================



window.FlightCalculator = {
  systems: [
    { id: 'sol', name: 'Sol', x: 0, y: 0, z: 0 },
    { id: 'alpha', name: 'Alpha Centauri A', x: 4.0, y: 1.0, z: 1.5 }, // ~4.37 св. года
    { id: 'epsilon', name: 'Epsilon Eridani', x: 8.5, y: -5.0, z: 3.5 }, // ~10.5 св. года
    { id: 'tau', name: 'Tau Ceti', x: -10.5, y: 4.5, z: 3.5 }, // ~11.9 св. года
    { id: 'teegarden', name: "Teegarden's Star", x: 1.5, y: -8.5, z: -9.0 }, // ~12.5 св. года
    { id: 'trappist', name: 'TRAPPIST-1', x: -35.0, y: 15.0, z: -12.0 } // ~39.6 св. года
  ],

  planets: [
    // --- SOL SYSTEM ---
    { id: 'sun', name: 'Sun', systemId: 'sol', orbitRadius: 0, img: 'assets/stars/g-dwarf-max.jpg', phrase: 'Sun — The Heart of the System' },
    { id: 'mercury', name: 'Mercury', systemId: 'sol', orbitRadius: 0.39, img: 'assets/sun/mercury-max.jpg', phrase: 'Mercury — The Swift Messenger' },
    { id: 'venus', name: 'Venus', systemId: 'sol', orbitRadius: 0.72, img: 'assets/sun/venus-max.jpg', phrase: 'Venus — The Morning Star' },
    { id: 'earth', name: 'Earth', systemId: 'sol', orbitRadius: 1.00, img: 'assets/sun/earth-max.jpg', phrase: 'Earth — The Cradle of Life' },
    { id: 'mars', name: 'Mars', systemId: 'sol', orbitRadius: 1.52, img: 'assets/sun/mars-max.jpg', phrase: 'Mars — The Red Planet' },
    { id: 'uranus', name: 'Uranus', systemId: 'sol', orbitRadius: 19.2, img: 'assets/sun/uranus-max.jpg', phrase: 'Uranus — The Ice Giant' },
    { id: 'neptune', name: 'Neptune', systemId: 'sol', orbitRadius: 30.1, img: 'assets/sun/neptune-max.jpg', phrase: 'Neptune — The Azure Giant' },

    // --- ALPHA CENTAURI A SYSTEM ---
    { id: 'alpha-centauri-a', name: 'Alpha Centauri A', systemId: 'alpha', orbitRadius: 0, img: 'assets/stars/g-dwarf-max.jpg', phrase: 'Alpha Centauri A — The Nearest Sun' },
    { id: 'proxima-b', name: 'Proxima b', systemId: 'alpha', orbitRadius: 0.05, img: 'assets/alpha-centauri-a/proxima-b-max.jpg', phrase: 'Proxima b — The Habitable Frontier' },
    { id: 'proxima-c', name: 'Proxima c', systemId: 'alpha', orbitRadius: 1.49, img: 'assets/alpha-centauri-a/proxima-c-max.jpg', phrase: 'Proxima c — The Distant Ice World' },
    { id: 'proxima-d', name: 'Proxima d', systemId: 'alpha', orbitRadius: 0.03, img: 'assets/alpha-centauri-a/proxima-d-max.jpg', phrase: 'Proxima d — The Inner Ember' },

    // --- EPSILON ERIDANI SYSTEM ---
    { id: 'epsilon-eridani', name: 'Epsilon Eridani', systemId: 'epsilon', orbitRadius: 0, img: 'assets/stars/k-dwarf-max.jpg', phrase: 'Epsilon Eridani — The Young Neighbor' },
    { id: 'epsilon-eridani-c', name: 'Epsilon Eridani c', systemId: 'epsilon', orbitRadius: 40.0, img: 'assets/epsilon-eridani/epsilon-eridani-c-max.jpg', phrase: 'Epsilon Eridani c — The Hidden Giant' },

    // --- TAU CETI SYSTEM ---
    { id: 'tau-ceti', name: 'Tau Ceti', systemId: 'tau', orbitRadius: 0, img: 'assets/stars/g-dwarf-max.jpg', phrase: 'Tau Ceti — The Ancient Watcher' },
    { id: 'tau-ceti-e', name: 'Tau Ceti e', systemId: 'tau', orbitRadius: 0.54, img: 'assets/tau-ceti/tau-ceti-e-max.jpg', phrase: 'Tau Ceti e — The Scorched Shore' },
    { id: 'tau-ceti-f', name: 'Tau Ceti f', systemId: 'tau', orbitRadius: 1.33, img: 'assets/tau-ceti/tau-ceti-f-max.jpg', phrase: 'Tau Ceti f — The Frozen Ocean' },
    { id: 'tau-ceti-g', name: 'Tau Ceti g', systemId: 'tau', orbitRadius: 0.13, img: 'assets/tau-ceti/tau-ceti-g-max.jpg', phrase: 'Tau Ceti g — The Verdant Hope' },
    { id: 'tau-ceti-h', name: 'Tau Ceti h', systemId: 'tau', orbitRadius: 1.90, img: 'assets/tau-ceti/tau-ceti-h-max.jpg', phrase: 'Tau Ceti h — The Distant Ice' },

    // --- TEEGARDEN SYSTEM ---
    { id: 'teegarden-star', name: "Teegarden's Star", systemId: 'teegarden', orbitRadius: 0, img: 'assets/stars/m-dwarf-max.jpg', phrase: "Teegarden's Star — The Faint Red Beacon" },
    { id: 'teegarden-b', name: 'Teegarden b', systemId: 'teegarden', orbitRadius: 0.025, img: 'assets/teegarden/teegarden-b-max.jpg', phrase: 'Teegarden b — The Earth-like Shadow' },
    { id: 'teegarden-c', name: 'Teegarden c', systemId: 'teegarden', orbitRadius: 0.044, img: 'assets/teegarden/teegarden-c-max.jpg', phrase: 'Teegarden c — The Frozen Twin' },

    // --- TRAPPIST-1 SYSTEM ---
    { id: 'trappist-1', name: 'TRAPPIST-1', systemId: 'trappist', orbitRadius: 0, img: 'assets/stars/m-dwarf-max.jpg', phrase: 'TRAPPIST-1 — The Seven Sisters\' Sun' },
    { id: 'trappist-1b', name: 'TRAPPIST-1 b', systemId: 'trappist', orbitRadius: 0.011, img: 'assets/trappist-1/trappist-1b-max.jpg', phrase: 'TRAPPIST-1 b — The Scorched Inner World' },
    { id: 'trappist-1c', name: 'TRAPPIST-1 c', systemId: 'trappist', orbitRadius: 0.016, img: 'assets/trappist-1/trappist-1c-max.jpg', phrase: 'TRAPPIST-1 c — The Burning Twin' },
    { id: 'trappist-1d', name: 'TRAPPIST-1 d', systemId: 'trappist', orbitRadius: 0.022, img: 'assets/trappist-1/trappist-1d-max.jpg', phrase: 'TRAPPIST-1 d — The Twilight Border' },
    { id: 'trappist-1e', name: 'TRAPPIST-1 e', systemId: 'trappist', orbitRadius: 0.029, img: 'assets/trappist-1/trappist-1e-max.jpg', phrase: 'TRAPPIST-1 e — The Golden Hope' },
    { id: 'trappist-1f', name: 'TRAPPIST-1 f', systemId: 'trappist', orbitRadius: 0.038, img: 'assets/trappist-1/trappist-1f-max.jpg', phrase: 'TRAPPIST-1 f — The Ocean World' },
    { id: 'trappist-1g', name: 'TRAPPIST-1 g', systemId: 'trappist', orbitRadius: 0.047, img: 'assets/trappist-1/trappist-1g-max.jpg', phrase: 'TRAPPIST-1 g — The Verdant Dream' },
    { id: 'trappist-1h', name: 'TRAPPIST-1 h', systemId: 'trappist', orbitRadius: 0.062, img: 'assets/trappist-1/trappist-1h-max.jpg', phrase: 'TRAPPIST-1 h — The Frozen Frontier' }
  ]
};

//#endregion

// ========================================================================
//#region 6️⃣ 🧬 ДАННЫЕ ДЛЯ РАСЧЕТА CIS
// ========================================================================

window.CIS_THRESHOLDS = [
  { min: 75, label: "HIGHLY HABITABLE", class: "status-habitable", color: "#2ecc71", desc: "Идеальна для колонизации, жизнь вероятна" },
  { min: 60, label: "CONDITIONALLY HABITABLE", class: "status-limited", color: "#f1c40f", desc: "Условно пригодна, требуются рекомендации" },
  { min: 40, label: "MARGINALLY HABITABLE", class: "status-uninhabitable", color: "#e74c3c", desc: "Мало пригодна, требуется разведка зонда" },
  { min: 0, label: "UNINHABITABLE", class: "status-dead", color: "#7f8c8d", desc: "Непригодна, безнадёжна для земной жизни" }
];

window.CisPlanet = [
  // --- SOL SYSTEM ---
  {
    planet: "MERCURY", name: "MERCURY", star: "Sol", type: "Terrestrial", img: "assets/sun/mercury-max.jpg",
    cis_params: { habitable_zone: 10, surface: 100, hydrosphere: 0, atmosphere: 0, breathability: 0, climate: 5, gravity: 38, magnetic: 5, star_radiation: 100 },
    description: "Planet is unsuitable for colonization. No atmosphere, hydrosphere, or breathability create lethal vacuum conditions. Magnetic field is critically weak (5), blocking only 4% of lethal stellar radiation (effective exposure: 96/100). Extreme thermal swings (600°C delta) and low gravity (38%) make survival impossible without complete isolation.",
    warning: "CRITICAL: Lethal radiation exposure (96/100 effective) with only 4% magnetic shielding. Vacuum conditions require full pressure suits at all times. Extreme thermal variance (5/100) causes equipment failure. Uninhabitable for human colonization."
  },
  {
    planet: "VENUS", name: "VENUS", star: "Sol", type: "Terrestrial", img: 'assets/sun/venus-max.jpg',
    cis_params: { habitable_zone: 60, surface: 10, hydrosphere: 0, atmosphere: 0, breathability: 0, climate: 0, gravity: 90, magnetic: 0, star_radiation: 85 },
    description: "Planet is unsuitable for colonization. Despite favorable gravity (90%) and acceptable position in habitable zone (60), Venus is a hellish world with zero atmosphere, hydrosphere, and breathability. Magnetic field is completely absent (0), providing no protection against stellar radiation (effective exposure: 85/100). Surface conditions are catastrophic with climate stability at absolute zero.",
    warning: "CRITICAL: Zero magnetic shielding leaves surface fully exposed to stellar radiation (85/100). No atmosphere means vacuum conditions and immediate ebullism risk. Climate completely unstable (0/100) with extreme surface degradation. Surface integrity critically low (10/100) — landing operations highly dangerous. Uninhabitable."
  },
  {
    planet: "EARTH", name: "EARTH", star: "Sol", type: "Terrestrial", img: 'assets/sun/earth-max.jpg',
    cis_params: { habitable_zone: 100, surface: 100, hydrosphere: 100, atmosphere: 100, breathability: 100, climate: 100, gravity: 100, magnetic: 100, star_radiation: 65 }, 
    description: "Optimal candidate for colonization. All life-support parameters at maximum (100): stable atmosphere, abundant hydrosphere, full breathability, and ideal climate. Magnetic field at full strength (100) completely neutralizes stellar radiation (effective exposure: 0/100). Surface integrity and gravity are perfect for long-term human habitation without technological assistance.",
    warning: "MINIMAL RISK: Raw stellar radiation at moderate level (65/100), but magnetic shield provides full protection (effective exposure: 0/100). No critical threats detected. Standard planetary safety protocols sufficient. Ideal for unrestricted colonization."
  },
  {
    planet: "MARS", name: "MARS", star: "Sol", type: "Terrestrial", img: 'assets/sun/mars-max.jpg',
    cis_params: { habitable_zone: 85, surface: 100, hydrosphere: 10, atmosphere: 20, breathability: 0, climate: 30, gravity: 38, magnetic: 10, star_radiation: 45 },
    description: "Marginally habitable candidate with solid surface (100) and favorable position in habitable zone (85). Atmosphere is critically thin (20) with zero breathability, requiring pressurized habitats. Magnetic field is weak (10), blocking only 8% of stellar radiation — effective exposure remains at 37/100. Low gravity (38%) and minimal hydrosphere (10) demand full life support infrastructure for long-term settlement.",
    warning: "WARNING: Weak magnetic shielding (10) allows significant radiation penetration (37/100 effective). Thin atmosphere (20) provides negligible pressure protection — exterior operations require full suits. Climate instability (30) and near-zero water reserves (10) make self-sustaining colonization impossible. Terraforming or sealed dome habitats mandatory."
  },
  {
    planet: "URANUS", name: "URANUS", star: "Sol", type: "Ice Giant", img: 'assets/sun/uranus-max.jpg',
    cis_params: { habitable_zone: 10, surface: 0, hydrosphere: 80, atmosphere: 10, breathability: 0, climate: 0, gravity: 89, magnetic: 45, star_radiation: 15 },
    description: "Gas giant unsuitable for colonization. No solid surface (0) makes landing and base construction impossible. Despite strong hydrosphere (80) and favorable gravity (89), the planet lacks breathable atmosphere (10) and has zero climate stability. Magnetic field (45) fully neutralizes low stellar radiation (effective exposure: 0/100), but this offers no practical benefit without a habitable surface.",
    warning: "CRITICAL: Zero surface integrity — no landing possible, only atmospheric floating stations theoretically viable. Atmosphere too thin and unbreathable (0) for any human activity. Climate completely unstable (0/100) with extreme atmospheric pressure gradients. Hydrosphere present (80) but inaccessible without surface infrastructure. Uninhabitable."
  },
  {
    planet: "NEPTUNE", name: "NEPTUNE", star: "Sol", type: "Ice Giant", img: 'assets/sun/neptune-max.jpg',
    cis_params: { habitable_zone: 5, surface: 0, hydrosphere: 80, atmosphere: 10, breathability: 0, climate: 0, gravity: 100, magnetic: 45, star_radiation: 10 },
    description: "Gas giant unsuitable for colonization. No solid surface (0) and extreme distance from the habitable zone (5) make landing and settlement impossible. Despite perfect gravity (100) and a strong hydrosphere (80), the lack of a breathable atmosphere (0) and zero climate stability prevent human habitation. Magnetic field (45) fully neutralizes stellar radiation, but offers no practical benefit without a physical surface.",
    warning: "CRITICAL: Zero surface integrity (0) — no landing or base construction possible, only theoretical atmospheric floating habitats. Atmosphere is unbreathable (0) with completely unstable climate (0/100) and extreme pressure gradients. Hydrosphere (80) is entirely inaccessible without surface infrastructure. Uninhabitable."
  },

  // --- ALPHA CENTAURI / PROXIMA SYSTEM ---
  {
    planet: "PROXIMA B", name: "PROXIMA B", star: "Proxima Centauri", type: "Terrestrial", img: 'assets/alpha-centauri-a/proxima-b-max.jpg',
    cis_params: { habitable_zone: 75, surface: 100, hydrosphere: 40, atmosphere: 30, breathability: 0, climate: 35, gravity: 95, magnetic: 20, star_radiation: 85 },
    description: "Marginally habitable candidate with excellent surface (100) and near-Earth gravity (95). Position in habitable zone is favorable (75), but atmosphere is critically thin (30) with zero breathability. Magnetic field is weak (20), blocking only 16 units of intense stellar radiation — effective exposure remains dangerously high at 69/100. Limited hydrosphere (40) and unstable climate (35) require sealed habitats and imported water for sustained settlement.",
    warning: "WARNING: High stellar radiation (85 raw, 69 effective after weak magnetic shielding) poses long-term health risks. Thin atmosphere (30) offers negligible pressure protection — exterior operations require full suits. Zero breathability and limited water reserves (40) make self-sustaining life support impossible. Climate instability (35) requires reinforced dome infrastructure. Colonization viable only with heavy technological support."
  },
  {
    planet: "PROXIMA C", name: "PROXIMA C", star: "Proxima Centauri", type: "Super-Earth", img: 'assets/alpha-centauri-a/proxima-c-max.jpg',
    cis_params: { habitable_zone: 20, surface: 30, hydrosphere: 60, atmosphere: 50, breathability: 0, climate: 10, gravity: 60, magnetic: 30, star_radiation: 45 },
    description: "Planet is unsuitable for colonization. Located at the extreme edge of the habitable zone (20) with a heavily degraded surface (30) and unstable climate (10). While it possesses a moderate atmosphere (50) and hydrosphere (60), the air is completely unbreathable (0). Gravity is manageable (60), but the weak magnetic field (30) fails to fully protect the surface from stellar radiation.",
    warning: "WARNING: Zero breathability requires full life-support systems despite a 50% atmospheric density. Magnetic shielding is weak (30), leaving an effective radiation exposure of 21/100 on the surface. Climate stability is critically low (10) with severe weather patterns. Surface degradation (30) makes landing and base construction highly hazardous."
  },
  {
    planet: "PROXIMA D", name: "PROXIMA D", star: "Proxima Centauri", type: "Sub-Earth", img: 'assets/alpha-centauri-a/proxima-d-max.jpg',
    cis_params: { habitable_zone: 50, surface: 100, hydrosphere: 10, atmosphere: 10, breathability: 0, climate: 20, gravity: 25, magnetic: 10, star_radiation: 95 },
    description: "Planet is unsuitable for colonization despite a perfect solid surface (100). Located at the edge of the habitable zone (50) with extremely low gravity (25), making long-term human health unsustainable. Atmosphere is nearly absent (10) with zero breathability, and hydrosphere is minimal (10). Magnetic field is critically weak (10), failing to shield the surface from intense stellar radiation",
    warning: "CRITICAL: Extreme stellar radiation (95 raw, 87 effective after minimal magnetic shielding) makes surface exposure lethal within hours. Near-vacuum atmosphere (10) requires full pressure suits for all exterior operations. Ultra-low gravity (25) causes rapid muscle atrophy and bone density loss in colonists. Climate instability (20) and scarce water reserves (10) prevent self-sustaining settlement. Uninhabitable."
  },

  // --- EPSILON ERIDANI SYSTEM ---
  {
    planet: "EPSILON ERIDANI C", name: "EPSILON ERIDANI C", star: "Epsilon Eridani", type: "Gas Giant", img: 'assets/epsilon-eridani/epsilon-eridani-c-max.jpg',
    cis_params: { habitable_zone: 5, surface: 0, hydrosphere: 10, atmosphere: 10, breathability: 0, climate: 0, gravity: 80, magnetic: 60, star_radiation: 25 },
    description: "Gas giant unsuitable for colonization. Zero surface integrity (0) makes landing and base construction impossible. Located far outside the habitable zone (5) with zero climate stability and zero breathability. Despite strong gravity (80) and a decent magnetic field (60), the lack of atmosphere (10) and hydrosphere (10) prevents any form of human settlement.",
    warning: "CRITICAL: Zero surface integrity — no landing possible, only theoretical atmospheric floating habitats. Zero climate stability (0) with extreme atmospheric turbulence. Atmosphere is unbreathable and too thin (10) to support human life. Magnetic field (60) fully neutralizes low stellar radiation (effective exposure: 0/100), but this offers no benefit without a habitable surface. Uninhabitable."
  },

  // --- TAU CETI SYSTEM ---
  {
    planet: "TAU CETI E", name: "TAU CETI E", star: "Tau Ceti", type: "Super-Earth", img: 'assets/tau-ceti/tau-ceti-e-max.jpg',
    cis_params: { habitable_zone: 70, surface: 80, hydrosphere: 60, atmosphere: 70, breathability: 10, climate: 40, gravity: 60, magnetic: 60, star_radiation: 15 },
    description: "Conditionally habitable candidate with strong surface integrity (80) and favorable position in the habitable zone (70). Atmosphere is moderately dense (70) with significant hydrosphere (60), but breathability is critically low (10) — air is toxic or oxygen-depleted. Magnetic field (60) fully neutralizes stellar radiation (effective exposure: 0/100), making surface operations safe from radiation. Gravity (60) is manageable for long-term human adaptation.",
    warning: "WARNING: Breathability at 10/100 — atmosphere is unbreathable despite decent density. All exterior operations require oxygen supply systems or sealed habitats. Climate instability (40) brings unpredictable weather patterns and seasonal extremes. Surface colonization viable only with atmospheric processing infrastructure and climate-controlled dome settlements. Promising candidate for terraforming efforts."
  },
  {
    planet: "TAU CETI F", name: "TAU CETI F", star: "Tau Ceti", type: "Super-Earth", img: 'assets/tau-ceti/tau-ceti-f-max.jpg',
    cis_params: { habitable_zone: 90, surface: 90, hydrosphere: 80, atmosphere: 80, breathability: 15, climate: 70, gravity: 60, magnetic: 70, star_radiation: 15 },
    description: "Highly habitable candidate with excellent surface integrity (90) and a prime location in the habitable zone (90). Features a dense atmosphere (80) and abundant hydrosphere (80), though the air is largely unbreathable (15) and requires filtration. Strong magnetic field (70) completely neutralizes stellar radiation (effective exposure: 0/100), ensuring a safe surface environment. Gravity (60) and climate stability (70) are well within acceptable limits for long-term human settlement.",
    warning: "WARNING: Breathability is critically low (15/100) despite a thick atmosphere (80) — supplemental oxygen or sealed habitats are mandatory for all exterior operations. Magnetic shielding (70) provides complete protection against stellar radiation (0/100 effective exposure). Climate stability (70) is generally favorable but may feature localized extreme weather events. Excellent candidate for rapid colonization with basic atmospheric processing technology."
  },
  {
    planet: "TAU CETI G", name: "TAU CETI G", star: "Tau Ceti", type: "Super-Earth", img: 'assets/tau-ceti/tau-ceti-g-max.jpg',
    cis_params: { habitable_zone: 50, surface: 90, hydrosphere: 20, atmosphere: 60, breathability: 0, climate: 20, gravity: 70, magnetic: 50, star_radiation: 15 },
    description: "Marginally habitable candidate with excellent surface integrity (90) and acceptable gravity (70). Positioned at the edge of the habitable zone (50) with a moderate atmosphere (60), but the air is completely unbreathable (0). Magnetic field (50) fully neutralizes low stellar radiation (effective exposure: 0/100), making surface operations radiation-safe. However, scarce hydrosphere (20) and unstable climate (20) demand significant infrastructure investment for sustained settlement.",
    warning: "WARNING: Zero breathability despite a 60% atmospheric density — all exterior operations require oxygen supply systems or sealed habitats. Climate instability (20) brings frequent extreme weather events and seasonal volatility. Limited water reserves (20) prevent self-sustaining agriculture; water must be imported or extracted from subsurface deposits. Surface colonization viable only with climate-controlled dome infrastructure and atmospheric processing systems."
  },
  {
    planet: "TAU CETI H", name: "TAU CETI H", star: "Tau Ceti", type: "Super-Earth", img: 'assets/tau-ceti/tau-ceti-h-max.jpg',
    cis_params: { habitable_zone: 60, surface: 80, hydrosphere: 70, atmosphere: 50, breathability: 0, climate: 30, gravity: 75, magnetic: 60, star_radiation: 15 },
    description: "Conditionally habitable candidate with strong surface (80), favorable gravity (75), and abundant hydrosphere (70). Positioned within the habitable zone (60) with a moderate atmosphere (50), but the air is completely unbreathable (0). Magnetic field (60) fully neutralizes low stellar radiation (effective exposure: 0/100), ensuring a radiation-safe surface. Climate instability (30) and zero breathability require sealed habitats and atmospheric processing for sustained colonization.",
    warning: "WARNING: Zero breathability despite moderate atmospheric density (50) — all exterior operations require supplemental oxygen systems. Climate instability (30) brings unpredictable weather patterns and seasonal extremes. Hydrosphere (70) is abundant but requires purification infrastructure. Surface colonization viable with dome habitats and atmospheric processing; promising candidate for terraforming."
  },

  // --- TEEGARDEN'S STAR SYSTEM ---
  {
    planet: "TEEGARDEN B", name: "TEEGARDEN B", star: "Teegarden's Star", type: "Terrestrial", img: 'assets/teegarden/teegarden-b-max.jpg',
    cis_params: { habitable_zone: 85, surface: 90, hydrosphere: 40, atmosphere: 30, breathability: 0, climate: 40, gravity: 95, magnetic: 20, star_radiation: 40 },
    description: "Marginally habitable candidate with excellent surface integrity (90) and near-Earth gravity (95). Positioned well within the habitable zone (85), but the atmosphere is critically thin (30) with zero breathability. Magnetic field is weak (20), blocking only 8 units of stellar radiation — effective exposure remains elevated at 32/100. Limited hydrosphere (40) and unstable climate (40) require sealed habitats and imported water for sustained settlement.",
    warning: "WARNING: Weak magnetic shielding (20) allows significant radiation penetration (32/100 effective) — long-term surface exposure poses health risks. Thin atmosphere (30) offers negligible pressure protection; exterior operations require full pressure suits. Zero breathability and limited water reserves (40) make self-sustaining life support impossible. Climate instability (40) requires reinforced dome infrastructure. Colonization viable only with heavy technological support."
  },
  {
    planet: "TEEGARDEN C", name: "TEEGARDEN C", star: "Teegarden's Star", type: "Terrestrial", img: 'assets/teegarden/teegarden-c-max.jpg',
    cis_params: { habitable_zone: 60, surface: 90, hydrosphere: 30, atmosphere: 20, breathability: 0, climate: 20, gravity: 90, magnetic: 20, star_radiation: 40 },
    description: "Marginally habitable candidate with excellent surface integrity (90) and near-Earth gravity (90). Positioned within the habitable zone (60), but the atmosphere is critically thin (20) with zero breathability. Magnetic field is weak (20), blocking only 8 units of stellar radiation — effective exposure remains elevated at 32/100. Limited hydrosphere (30) and unstable climate (20) require sealed habitats and imported water for sustained settlement.",
    warning: "WARNING: Weak magnetic shielding (20) allows significant radiation penetration (32/100 effective) — long-term surface exposure poses health risks. Thin atmosphere (20) offers negligible pressure protection; exterior operations require full pressure suits. Zero breathability and limited water reserves (30) make self-sustaining life support impossible. Climate instability (20) requires reinforced dome infrastructure. Colonization viable only with heavy technological support."
  },

  // --- TRAPPIST-1 SYSTEM ---
  {
    planet: "TRAPPIST-1B", name: "TRAPPIST-1B", star: "TRAPPIST-1", type: "Terrestrial", img: 'assets/trappist-1/trappist-1b-max.jpg',
    cis_params: { habitable_zone: 30, surface: 90, hydrosphere: 10, atmosphere: 20, breathability: 0, climate: 10, gravity: 95, magnetic: 30, star_radiation: 65 },
    description: "Planet is unsuitable for colonization despite excellent surface integrity (90) and near-Earth gravity (95). Located too close to its host star (habitable zone: 30), resulting in extreme stellar radiation exposure. Magnetic field is weak (30), blocking only 19.5 units of radiation — effective surface exposure remains dangerously high at 45.5/100. Atmosphere is critically thin (20) with zero breathability, minimal hydrosphere (10), and unstable climate (10).",
    warning: "WARNING: Elevated stellar radiation (65 raw, 45.5 effective after weak magnetic shielding) poses long-term health risks to colonists. Thin atmosphere (20) offers negligible pressure protection — exterior operations require full pressure suits. Zero breathability and scarce water reserves (10) make self-sustaining life support impossible. Climate instability (10) requires reinforced dome infrastructure. Uninhabitable without massive technological investment."
  },
  {
    planet: "TRAPPIST-1C", name: "TRAPPIST-1C", star: "TRAPPIST-1", type: "Terrestrial", img: 'assets/trappist-1/trappist-1c-max.jpg',
    cis_params: { habitable_zone: 40, surface: 90, hydrosphere: 20, atmosphere: 30, breathability: 0, climate: 15, gravity: 100, magnetic: 30, star_radiation: 60 },
    description: "Marginally habitable candidate with perfect Earth-like gravity (100) and excellent surface integrity (90). However, the atmosphere is critically thin (30) with zero breathability, and hydrosphere is minimal (20). The magnetic field is weak (30), blocking only 18 units of stellar radiation — effective surface exposure remains elevated at 42/100. Unstable climate (15) and edge-of-zone positioning (40) require heavy infrastructure for any sustained settlement.",
    warning: "WARNING: Weak magnetic shielding (30) allows significant radiation penetration (42/100 effective) — long-term surface exposure poses health risks. Thin atmosphere (30) offers negligible pressure protection; exterior operations require full pressure suits. Zero breathability and limited water reserves (20) make self-sustaining life support impossible. Climate instability (15) requires reinforced dome infrastructure. Colonization viable only with heavy technological support."
  },
  {
    planet: "TRAPPIST-1D", name: "TRAPPIST-1D", star: "TRAPPIST-1", type: "Terrestrial", img: 'assets/trappist-1/trappist-1d-max.jpg',
    cis_params: { habitable_zone: 70, surface: 90, hydrosphere: 50, atmosphere: 50, breathability: 5, climate: 40, gravity: 35, magnetic: 40, star_radiation: 50 },
    description: "Marginally habitable candidate with excellent surface integrity (90) and favorable position in the habitable zone (70). Atmosphere and hydrosphere are both moderate (50), but breathability is nearly absent (5). Magnetic field is weak (40), blocking only 20 units of stellar radiation — effective surface exposure remains elevated at 30/100. Critically low gravity (35) would cause severe long-term health degradation in colonists, and climate instability (40) requires reinforced habitat infrastructure.",
    warning: "WARNING: Weak magnetic shielding (40) allows moderate radiation penetration (30/100 effective) — long-term surface exposure poses cumulative health risks. Ultra-low gravity (35) causes rapid muscle atrophy and bone density loss; artificial gravity or rotation habitats mandatory. Near-zero breathability (5) and moderate water reserves (50) require full life-support systems. Climate instability (40) demands sealed dome settlements. Colonization viable only with heavy technological support."
  },
  {
    planet: "TRAPPIST-1E", name: "TRAPPIST-1E", star: "TRAPPIST-1", type: "Terrestrial", img: 'assets/trappist-1/trappist-1e-max.jpg',
    cis_params: { habitable_zone: 85, surface: 95, hydrosphere: 80, atmosphere: 70, breathability: 10, climate: 60, gravity: 90, magnetic: 60, star_radiation: 40 },
    description: "Highly habitable candidate with near-perfect surface integrity (95) and Earth-like gravity (90). Prime location in the habitable zone (85) combined with abundant hydrosphere (80) and moderate atmosphere (70). Magnetic field (60) significantly reduces stellar radiation — effective surface exposure is low at 16/100. Climate stability (60) is acceptable, though breathability is critically low (10) despite atmospheric density.",
    warning: "WARNING: Breathability at 10/100 despite 70% atmospheric density — atmosphere is toxic or oxygen-depleted, requiring supplemental oxygen systems for all exterior operations. Magnetic shielding (60) reduces radiation to safe levels (16/100 effective). Climate stability (60) is generally favorable but may feature localized extreme weather. Excellent candidate for colonization with atmospheric processing infrastructure; one of the most promising targets in the TRAPPIST-1 system."
  },
  {
    planet: "TRAPPIST-1F", name: "TRAPPIST-1F", star: "TRAPPIST-1", type: "Terrestrial", img: 'assets/trappist-1/trappist-1f-max.jpg',
    cis_params: { habitable_zone: 80, surface: 90, hydrosphere: 70, atmosphere: 60, breathability: 5, climate: 50, gravity: 95, magnetic: 50, star_radiation: 35 },
    description: "Conditionally habitable candidate with near-perfect surface integrity (90) and Earth-like gravity (95). Prime location in the habitable zone (80) combined with abundant hydrosphere (70) and moderate atmosphere (60). Magnetic field is weak (50), blocking only 17.5 units of stellar radiation — effective surface exposure remains low at 17.5/100. However, breathability is nearly absent (5) despite atmospheric density, requiring full life-support systems for sustained settlement.",
    warning: "WARNING: Breathability at 5/100 despite 60% atmospheric density — atmosphere is toxic or oxygen-depleted, requiring supplemental oxygen systems for all exterior operations. Weak magnetic shielding (50) allows moderate radiation penetration (17.5/100 effective) — acceptable for short-term missions but poses cumulative risks for long-term colonization. Climate instability (50) brings unpredictable weather patterns. Surface colonization viable with atmospheric processing infrastructure; strong terraforming candidate."
  },
  {
    planet: "TRAPPIST-1G", name: "TRAPPIST-1G", star: "TRAPPIST-1", type: "Terrestrial", img: 'assets/trappist-1/trappist-1g-max.jpg',
    cis_params: { habitable_zone: 70, surface: 90, hydrosphere: 60, atmosphere: 50, breathability: 0, climate: 30, gravity: 90, magnetic: 40, star_radiation: 25 },
    description: "Conditionally habitable candidate with excellent surface integrity (90) and Earth-like gravity (90). Favorable position in the habitable zone (70) with moderate hydrosphere (60) and atmosphere (50), but breathability is completely absent (0). Magnetic field is weak (40), blocking 10 units of stellar radiation — effective surface exposure remains low at 15/100. Climate instability (30) and zero breathability require sealed habitats and atmospheric processing for sustained settlement.",
    warning: "WARNING: Zero breathability despite moderate atmospheric density (50) — atmosphere is toxic or oxygen-depleted, requiring supplemental oxygen systems for all exterior operations. Weak magnetic shielding (40) allows minor radiation penetration (15/100 effective) — acceptable for long-term missions. Climate instability (30) brings unpredictable weather patterns and seasonal extremes. Surface colonization viable with atmospheric processing infrastructure; promising terraforming candidate."
  },
  {
    planet: "TRAPPIST-1H", name: "TRAPPIST-1H", star: "TRAPPIST-1", type: "Terrestrial", img: 'assets/trappist-1/trappist-1h-max.jpg',
    cis_params: { habitable_zone: 40, surface: 90, hydrosphere: 20, atmosphere: 20, breathability: 0, climate: 5, gravity: 75, magnetic: 40, star_radiation: 40 },
    description: "Marginally habitable candidate with excellent surface integrity (90) and good gravity (75). However, positioned at the extreme edge of the habitable zone (40) with a critically thin atmosphere (20) and zero breathability. Magnetic field is weak (40), blocking 16 units of stellar radiation — effective surface exposure is moderate at 24/100. Catastrophic climate instability (5) and minimal hydrosphere (20) make sustained settlement nearly impossible without massive infrastructure.",
    warning: "CRITICAL: Catastrophic climate instability (5/100) — extreme weather volatility makes surface operations highly dangerous and unpredictable. Zero breathability despite thin atmosphere (20) requires full pressure suits and oxygen systems for all exterior operations. Minimal water reserves (20) prevent self-sustaining agriculture. Weak magnetic shielding (40) allows moderate radiation penetration (24/100 effective). Surface colonization theoretically possible but requires extreme technological investment; marginally viable"
  }
];



// Формула для расчетов
//CIS = (habitable_zone × 0.15) +
//     (surface × 0.15) +
//      (hydrosphere × 0.15) +
//      (atmosphere × 0.10) +
//      (breathability × 0.10) +
//      (climate × 0.10) +
//      (gravity × 0.10) +
//      (magnetic × 0.15) 
