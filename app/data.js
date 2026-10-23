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
  { min: 70, max: 100, label: "HIGHLY HABITABLE", class: "status-habitable", color: "#2ecc71", desc: "Идеальна для колонизации, жизнь вероятна" },
  { min: 50, max: 69, label: "CONDITIONALLY HABITABLE", class: "status-limited", color: "#f1c40f", desc: "Условно пригодна, требуются рекомендации" },
  { min: 35, max: 49, label: "MARGINALLY HABITABLE", class: "status-uninhabitable", color: "#e74c3c", desc: "Мало пригодна, требуется разведка зонда" },
  { min: 0, max: 34, label: "UNINHABITABLE", class: "status-dead", color: "#7f8c8d", desc: "Непригодна, безнадёжна для земной жизни" }
];

window.CisPlanet = [
  // --- SOL SYSTEM ---
  {
    id: "mercury", name: "Mercury", star: "Sol", type: "Terrestrial",
    cis_params: { habitable_zone: 10, surface: 100, hydrosphere: 0, atmosphere: 0, breathability: 0, climate: 5, gravity: 38, magnetic: 5, stellar_flares: 80 },
    description: "The smallest planet and closest to the Sun. Extreme temperature fluctuations and lack of atmosphere make it completely hostile.",
    warning: "CRITICAL: Extreme thermal variations, vacuum conditions, high solar radiation."
  },
  {
    id: "venus", name: "Venus", star: "Sol", type: "Terrestrial",
    cis_params: { habitable_zone: 60, surface: 10, hydrosphere: 0, atmosphere: 0, breathability: 0, climate: 0, gravity: 90, magnetic: 0, stellar_flares: 70 },
    description: "Earth's 'evil twin'. Similar in size and mass, but its runaway greenhouse effect creates a hellish surface environment.",
    warning: "CRITICAL: Crushing atmospheric pressure (90 atm), toxic sulfuric acid clouds, extreme heat."
  },
  {
    id: "earth", name: "Earth", star: "Sol", type: "Terrestrial",
    cis_params: { habitable_zone: 100, surface: 100, hydrosphere: 100, atmosphere: 100, breathability: 100, climate: 100, gravity: 100, magnetic: 100, stellar_flares: 100 }, // stellar_flares = 100 для идеального эталона
    description: "The home world of humanity. The absolute baseline and gold standard for all planetary habitability comparisons.",
    warning: "None. Optimal conditions."
  },
  {
    id: "mars", name: "Mars", star: "Sol", type: "Terrestrial",
    cis_params: { habitable_zone: 85, surface: 100, hydrosphere: 10, atmosphere: 20, breathability: 0, climate: 30, gravity: 38, magnetic: 10, stellar_flares: 60 },
    description: "The Red Planet. Cold and dry, but possesses a solid surface, water ice, and a day length similar to Earth's.",
    warning: "WARNING: Thin atmosphere, high radiation, requires pressurized habitats and life support."
  },
  {
    id: "uranus", name: "Uranus", star: "Sol", type: "Ice Giant",
    cis_params: { habitable_zone: 10, surface: 0, hydrosphere: 80, atmosphere: 10, breathability: 0, climate: 0, gravity: 89, magnetic: 40, stellar_flares: 10 },
    description: "An ice giant with a unique sideways rotation. Lacks a solid surface for colonization.",
    warning: "CRITICAL: No solid surface, extreme cold, crushing atmospheric pressure at depth."
  },
  {
    id: "neptune", name: "Neptune", star: "Sol", type: "Ice Giant",
    cis_params: { habitable_zone: 5, surface: 0, hydrosphere: 80, atmosphere: 10, breathability: 0, climate: 0, gravity: 100, magnetic: 40, stellar_flares: 5 },
    description: "The windiest and most distant major planet. Dark, cold, and whipped by supersonic winds.",
    warning: "CRITICAL: No solid surface, extreme cold, supersonic atmospheric dynamics."
  },

  // --- ALPHA CENTAURI / PROXIMA SYSTEM ---
  {
    id: "proxima-b", name: "Proxima Centauri b", star: "Proxima Centauri", type: "Terrestrial",
    cis_params: { habitable_zone: 75, surface: 100, hydrosphere: 40, atmosphere: 30, breathability: 0, climate: 35, gravity: 95, magnetic: 20, stellar_flares: 10 },
    description: "The closest known exoplanet to Earth, orbiting in the habitable zone of a red dwarf.",
    warning: "CRITICAL: Extreme stellar flare activity from host star, uncertain atmosphere."
  },
  {
    id: "proxima-c", name: "Proxima Centauri c", star: "Proxima Centauri", type: "Super-Earth",
    cis_params: { habitable_zone: 20, surface: 30, hydrosphere: 60, atmosphere: 50, breathability: 0, climate: 10, gravity: 60, magnetic: 30, stellar_flares: 30 },
    description: "A super-Earth or mini-Neptune orbiting far from its star. Likely a cold, icy world with high gravity.",
    warning: "WARNING: Far outside habitable zone, extremely cold, high gravity."
  },
  {
    id: "proxima-d", name: "Proxima Centauri d", star: "Proxima Centauri", type: "Sub-Earth",
    cis_params: { habitable_zone: 50, surface: 100, hydrosphere: 10, atmosphere: 10, breathability: 0, climate: 20, gravity: 25, magnetic: 10, stellar_flares: 5 },
    description: "A lightweight sub-Earth orbiting very close to its star.",
    warning: "CRITICAL: Very close to active red dwarf, likely no atmosphere, extreme radiation."
  },

  // --- EPSILON ERIDANI SYSTEM ---
  {
    id: "epsilon-eridani-c", name: "Epsilon Eridani c", star: "Epsilon Eridani", type: "Gas Giant",
    cis_params: { habitable_zone: 5, surface: 0, hydrosphere: 10, atmosphere: 10, breathability: 0, climate: 0, gravity: 80, magnetic: 60, stellar_flares: 50 },
    description: "A massive gas giant orbiting far beyond the habitable zone of a young, active star.",
    warning: "CRITICAL: No solid surface, extreme cold, high radiation environment from young host star."
  },

  // --- TAU CETI SYSTEM ---
  {
    id: "tau-ceti-e", name: "Tau Ceti e", star: "Tau Ceti", type: "Super-Earth",
    cis_params: { habitable_zone: 70, surface: 80, hydrosphere: 60, atmosphere: 70, breathability: 10, climate: 40, gravity: 60, magnetic: 60, stellar_flares: 15 },
    description: "A massive super-Earth near the inner edge of the habitable zone.",
    warning: "WARNING: High gravity (approx 1.6g), potential runaway greenhouse effect."
  },
  {
    id: "tau-ceti-f", name: "Tau Ceti f", star: "Tau Ceti", type: "Super-Earth",
    cis_params: { habitable_zone: 90, surface: 90, hydrosphere: 80, atmosphere: 80, breathability: 15, climate: 70, gravity: 60, magnetic: 70, stellar_flares: 15 },
    description: "The most promising candidate in the Tau Ceti system. Located squarely in the habitable zone.",
    warning: "WARNING: Higher gravity than Earth. Atmospheric composition remains unconfirmed."
  },
  {
    id: "tau-ceti-g", name: "Tau Ceti g", star: "Tau Ceti", type: "Super-Earth",
    cis_params: { habitable_zone: 50, surface: 90, hydrosphere: 20, atmosphere: 60, breathability: 0, climate: 20, gravity: 70, magnetic: 50, stellar_flares: 15 },
    description: "A super-Earth orbiting too close to its star. Likely experienced a runaway greenhouse effect.",
    warning: "CRITICAL: High surface temperatures, probable loss of surface water."
  },
  {
    id: "tau-ceti-h", name: "Tau Ceti h", star: "Tau Ceti", type: "Super-Earth",
    cis_params: { habitable_zone: 60, surface: 80, hydrosphere: 70, atmosphere: 50, breathability: 0, climate: 30, gravity: 75, magnetic: 60, stellar_flares: 15 },
    description: "A cold super-Earth at the outer edge of the habitable zone.",
    warning: "WARNING: Low average temperatures, likely requires subsurface or heavily insulated habitats."
  },

  // --- TEEGARDEN'S STAR SYSTEM ---
  {
    id: "teegarden-b", name: "Teegarden's Star b", star: "Teegarden's Star", type: "Terrestrial",
    cis_params: { habitable_zone: 85, surface: 90, hydrosphere: 40, atmosphere: 30, breathability: 0, climate: 40, gravity: 95, magnetic: 20, stellar_flares: 40 },
    description: "One of the most Earth-like exoplanets discovered by mass and orbital position.",
    warning: "WARNING: Atmospheric retention is uncertain due to host star type."
  },
  {
    id: "teegarden-c", name: "Teegarden's Star c", star: "Teegarden's Star", type: "Terrestrial",
    cis_params: { habitable_zone: 60, surface: 90, hydrosphere: 30, atmosphere: 20, breathability: 0, climate: 20, gravity: 90, magnetic: 20, stellar_flares: 40 },
    description: "A slightly more massive cousin of planet b, orbiting near the outer edge of the habitable zone.",
    warning: "CRITICAL: Outer habitable zone edge, high probability of global glaciation."
  },

  // --- TRAPPIST-1 SYSTEM ---
  {
    id: "trappist-1b", name: "TRAPPIST-1 b", star: "TRAPPIST-1", type: "Terrestrial",
    cis_params: { habitable_zone: 30, surface: 90, hydrosphere: 10, atmosphere: 20, breathability: 0, climate: 10, gravity: 95, magnetic: 30, stellar_flares: 60 },
    description: "The innermost planet. Receives about 4 times the radiation Earth gets from the Sun.",
    warning: "CRITICAL: Extreme heat, probable runaway greenhouse effect, high stellar radiation."
  },
  {
    id: "trappist-1c", name: "TRAPPIST-1 c", star: "TRAPPIST-1", type: "Terrestrial",
    cis_params: { habitable_zone: 40, surface: 90, hydrosphere: 20, atmosphere: 30, breathability: 0, climate: 15, gravity: 100, magnetic: 30, stellar_flares: 60 },
    description: "Slightly further out, but still likely too hot for liquid water.",
    warning: "WARNING: High surface temperatures, uncertain atmospheric composition."
  },
  {
    id: "trappist-1d", name: "TRAPPIST-1 d", star: "TRAPPIST-1", type: "Terrestrial",
    cis_params: { habitable_zone: 70, surface: 90, hydrosphere: 50, atmosphere: 50, breathability: 5, climate: 40, gravity: 35, magnetic: 40, stellar_flares: 50 },
    description: "The lightest planet in the system, orbiting at the inner edge of the habitable zone.",
    warning: "WARNING: Low gravity, moderate stellar flare exposure."
  },
  {
    id: "trappist-1e", name: "TRAPPIST-1 e", star: "TRAPPIST-1", type: "Terrestrial",
    cis_params: { habitable_zone: 85, surface: 95, hydrosphere: 80, atmosphere: 70, breathability: 10, climate: 60, gravity: 90, magnetic: 60, stellar_flares: 40 },
    description: "The crown jewel of the system. Most likely to have a rocky surface, liquid water oceans, and a stable climate.",
    warning: "INFO: Best candidate for habitability. Conditions on the day-night boundary may be Earth-like."
  },
  {
    id: "trappist-1f", name: "TRAPPIST-1 f", star: "TRAPPIST-1", type: "Terrestrial",
    cis_params: { habitable_zone: 80, surface: 90, hydrosphere: 70, atmosphere: 60, breathability: 5, climate: 50, gravity: 95, magnetic: 50, stellar_flares: 40 },
    description: "Located in the middle of the habitable zone. Likely possesses a thick atmosphere.",
    warning: "WARNING: May require subsurface or heavily insulated habitats."
  },
  {
    id: "trappist-1g", name: "TRAPPIST-1 g", star: "TRAPPIST-1", type: "Terrestrial",
    cis_params: { habitable_zone: 70, surface: 90, hydrosphere: 60, atmosphere: 50, breathability: 0, climate: 30, gravity: 90, magnetic: 50, stellar_flares: 40 },
    description: "The largest planet in the system, orbiting near the outer edge of the habitable zone.",
    warning: "WARNING: Low average temperatures, high probability of global glaciation."
  },
  {
    id: "trappist-1h", name: "TRAPPIST-1 h", star: "TRAPPIST-1", type: "Terrestrial",
    cis_params: { habitable_zone: 40, surface: 90, hydrosphere: 20, atmosphere: 20, breathability: 0, climate: 5, gravity: 75, magnetic: 40, stellar_flares: 40 },
    description: "The outermost known planet. Too far from the star to maintain liquid water on the surface.",
    warning: "CRITICAL: Extreme cold, likely no surface liquid water."
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
