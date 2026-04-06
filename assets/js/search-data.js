// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "publications",
          description: "Publications presented in reversed chronological order.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-research-results",
          title: "research results",
          description: "Selected publications presented in chronological order.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/results/";
          },
        },{id: "nav-cv",
          title: "cv",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-projects",
          title: "projects",
          description: "Research projects in cyber-physical systems, energy efficiency, digital health, and cultural heritage preservation",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-projects",
          title: "projects",
          description: "Research projects in cyber-physical systems, energy efficiency, digital health, and cultural heritage preservation",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-blog",
          title: "blog",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/blog/";
          },
        },{id: "nav-repositories",
          title: "repositories",
          description: "Github profile and repositories",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "nav-teaching",
          title: "teaching",
          description: "Academic teaching positions in chronological order.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/teaching/";
          },
        },{id: "post-a-post-with-math",
      
        title: "a post with math",
      
      description: "an example of a blog post with some math",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2015/math/";
        
      },
    },{id: "news-new-preprint-on-text2bim-generating-building-models-using-a-large-language-model-based-multi-agent-framework",
          title: 'New preprint on “Text2BIM: Generating Building Models Using a Large Language Model-based Multi-Agent...',
          description: "",
          section: "News",},{id: "news-new-preprint-on-predictive-modeling-bim-command-recommendation-based-on-large-scale-usage-logs",
          title: 'New preprint on “Predictive Modeling: BIM Command Recommendation Based on Large-scale Usage Logs”!...',
          description: "",
          section: "News",},{id: "projects-ageingatwork",
          title: 'AgeingatWork',
          description: "Smart, Personalized and Adaptive ICT Solutions for Active, Healthy and Productive Ageing with enhanced Workability",
          section: "Projects",handler: () => {
              window.location.href = "/projects/AgeingatWork/";
            },},{id: "projects-cpsosaware",
          title: 'CPSoSaware',
          description: "Cross-layer cognitive optimization tools &amp; methods for the lifecycle support of dependable CPSoS",
          section: "Projects",handler: () => {
              window.location.href = "/projects/CPSoSaware/";
            },},{id: "projects-enerman",
          title: 'EnerMan',
          description: "ENERgy-efficient manufacturing system MANagement",
          section: "Projects",handler: () => {
              window.location.href = "/projects/EnerMan/";
            },},{id: "projects-gamecar",
          title: 'GamECAR',
          description: "Gamification of EcoDriving Behaviours through Intelligent Management of dynamic car and driver information",
          section: "Projects",handler: () => {
              window.location.href = "/projects/GamECAR/";
            },},{id: "projects-warmest",
          title: 'WARMEST',
          description: "loW Altitude Remote sensing for the Monitoring of the state of cultural hEritage Sites - building an inTegrated model for maintenance",
          section: "Projects",handler: () => {
              window.location.href = "/projects/WARMEST/";
            },},{id: "projects-myaircoach",
          title: 'myAirCoach',
          description: "Analysis, modelling and sensing of both physiological and environmental factors for the customized and predictive self-management of Asthma",
          section: "Projects",handler: () => {
              window.location.href = "/projects/myAirCoach/";
            },},{
        id: 'social-dblp',
        title: 'DBLP',
        section: 'Socials',
        handler: () => {
          window.open("https://dblp.org/pid/182/5078.html", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/snousias", "_blank");
        },
      },{
        id: 'social-ieee',
        title: 'IEEE Xplore',
        section: 'Socials',
        handler: () => {
          window.open("https://ieeexplore.ieee.org/author/37086088612/", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/stavrosnousias", "_blank");
        },
      },{
        id: 'social-orcid',
        title: 'ORCID',
        section: 'Socials',
        handler: () => {
          window.open("https://orcid.org/0000-0002-2811-235X", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=HQuAxd0AAAAJ", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
