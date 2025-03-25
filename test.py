from fontTools.svgLib import parse_path

mbti_images = {
    # Analysts (Intuitive & Thinking)
    "INTJ": "https://practicaltyping.com/wp-content/uploads/2025/01/intjanime.png",
    "INTP": "https://practicaltyping.com/wp-content/uploads/2025/01/intpanime.png",
    "ENTJ": "https://practicaltyping.com/wp-content/uploads/2025/01/entjanime.png",
    "ENTP": "https://practicaltyping.com/wp-content/uploads/2025/01/entpanime.png",

    # Diplomats (Intuitive & Feeling)
    "INFJ": "https://practicaltyping.com/wp-content/uploads/2025/01/infjanime.png",
    "INFP": "https://practicaltyping.com/wp-content/uploads/2025/01/infpanime.png",
    "ENFJ": "https://practicaltyping.com/wp-content/uploads/2025/01/enfjanime.png",
    "ENFP": "https://practicaltyping.com/wp-content/uploads/2025/01/enfpanime.png",

    # Sentinels (Observant & Judging)
    "ISTJ": "https://practicaltyping.com/wp-content/uploads/2025/01/istjanime.png",
    "ISFJ": "https://practicaltyping.com/wp-content/uploads/2025/01/isfjanime.png",
    "ESTJ": "https://practicaltyping.com/wp-content/uploads/2025/01/estjanime.png",
    "ESFJ": "https://practicaltyping.com/wp-content/uploads/2025/01/esfjanime.png",

    # Explorers (Observant & Prospecting)
    "ISTP": "https://practicaltyping.com/wp-content/uploads/2025/01/istpanime.png",
    "ISFP": "https://practicaltyping.com/wp-content/uploads/2025/01/isfpanime.png",
    "ESTP": "https://practicaltyping.com/wp-content/uploads/2025/01/estpanime.png",
    "ESFP": "https://practicaltyping.com/wp-content/uploads/2025/01/esfpanime.png"
}

strand_weights = {
    "STEM": {
        "Math": 1.4,
        "Science": 1.3,
        "English": 1.2,  # Raised slightly
        "Filipino": 1.0,
        "Social Studies": 0.9,
        "Business": 0.8,
        "Computer & IT": 1.2,
        "Arts & Design": 0.9,
        "Public Speaking": 0.8
    },
    "ABM": {
        "Math": 1.2,
        "Science": 1.1,
        "English": 1.2,
        "Filipino": 1.1,  # Lowered slightly
        "Social Studies": 1.3,
        "Business": 1.4,
        "Computer & IT": 1.0,
        "Arts & Design": 1.0,
        "Public Speaking": 1.2
    },
    "HUMSS": {
        "Math": 0.9,  # Lowered slightly
        "Science": 0.9,  # Lowered slightly
        "English": 1.3,
        "Filipino": 1.2,
        "Social Studies": 1.4,
        "Business": 0.8,
        "Computer & IT": 0.9,
        "Arts & Design": 1.3,
        "Public Speaking": 1.4  # Increased slightly
    }
}

personality_types = {
    #analysts
        "INTJ": {
        "category": "The Architect",
        "description": "Imaginative and strategic thinkers with a plan for everything. Architects are independent, value deep analysis, and prefer innovation over convention.",
        "quote": "“Thought constitutes the greatness of man. Man is a reed, the feeblest thing in nature, but he is a thinking reed.” – Blaise Pascal",
        "mbti_traits": ["Introverted", "Intuitive", "Thinking", "Judging"],
        "strand_fit": {
            "STEM": "Your curiosity and love for abstract ideas align well with STEM, as it requires deep analysis and logical reasoning.",
            "ABM": "Your ability to find unconventional solutions and analyze data critically makes you a unique fit for ABM.",
            "HUMSS": "INTPs thrive in HUMSS due to their ability to challenge ideas and explore complex philosophical discussions."
        },
        "strengths": [
            "Quick", "Imaginative", "Strategic", "Self-Confident",
            "Independent", "Decisive", "Hard-Working", "Determined",
            "Open-Minded", "Jacks-of-all-Trades"
        ],
        "weaknesses": [
            "Arrogant", "Judgmental", "Overly Analytical",
            "Loathe Highly Structured Environments",
            "Clueless in Romance"
        ],
        "career_paths": [
            "Project Managers", "Systems Engineers", "Marketing Strategists",
            "Systems Analysts", "Military Strategists"
        ],
        "famous_people": [
            "Friedrich Nietzsche", "Michelle Obama", "Elon Musk",
            "Christopher Nolan", "Vladimir Putin", "Arnold Schwarzenegger",
            "Colin Powell"
        ]
        },
        "INTP": {
            "category": "The Logician",
            "description": "Innovative inventors with an unquenchable thirst for knowledge. INTPs are deep thinkers who love exploring abstract concepts and challenging established norms.",
            "quote": "“The important thing is not to stop questioning. Curiosity has its own reason for existing.” – Albert Einstein",
            "mbti_traits": ["Introverted", "Intuitive", "Thinking", "Perceiving"],
            "strand_fit": {
                "STEM": "INTPs thrive in STEM due to their analytical minds and love for problem-solving, making them natural scientists, engineers, and programmers.",
                "ABM": "While less common, INTPs who enjoy logical systems and innovative business models may excel in entrepreneurship and market analysis.",
                "HUMSS": "Their deep thinking and philosophical nature can lead them toward careers in academia, research, or psychology."
            },
            "strengths": [
                "Curious", "Intellectual", "Objective", "Independent",
                "Original Thinkers", "Logical", "Open-Minded"
            ],
            "weaknesses": [
                "Overly Theoretical", "Disorganized", "Insensitive",
                "Prone to Overthinking", "Struggles with Practicality"
            ],
            "career_paths": [
                "Software Engineer", "Physicist", "Mathematician",
                "Philosopher", "Academic Researcher", "Psychologist"
            ],
            "famous_people": [
                "Albert Einstein", "Isaac Newton", "Marie Curie",
                "Bill Gates", "Socrates", "Mark Zuckerberg"
            ]
        },
        "ENTJ": {
            "category": "The Commander",
            "description": "Bold, imaginative, and strong-willed leaders, always finding a way—or making one. ENTJs are natural strategists who excel at organizing people and resources to achieve ambitious goals.",
            "quote": "“If you really want to do something, you'll find a way. If you don’t, you'll find an excuse.” – Jim Rohn",
            "mbti_traits": ["Extraverted", "Intuitive", "Thinking", "Judging"],
            "strand_fit": {
                "STEM": "ENTJs may thrive in STEM fields that involve leadership, management, or large-scale problem-solving, such as engineering or IT.",
                "ABM": "ABM is a perfect fit, as ENTJs naturally excel in business, finance, and executive roles due to their strategic thinking and leadership abilities.",
                "HUMSS": "ENTJs who enjoy debate and law may find fulfillment in political science, law, or media-related careers."
            },
            "strengths": [
                "Charismatic", "Confident", "Efficient", "Strategic",
                "Strong-Willed", "Decisive", "Inspiring"
            ],
            "weaknesses": [
                "Dominant", "Insensitive", "Stubborn",
                "Workaholic", "Struggles with Emotions"
            ],
            "career_paths": [
                "CEO", "Entrepreneur", "Lawyer",
                "Investment Banker", "Management Consultant", "Military Leader"
            ],
            "famous_people": [
                "Steve Jobs", "Margaret Thatcher", "Franklin D. Roosevelt",
                "Gordon Ramsay", "Sheryl Sandberg", "Napoleon Bonaparte"
            ]
        },

        "ENTP": {
            "category": "The Debater",
            "description": "Smart and curious thinkers who cannot resist an intellectual challenge. ENTPs are energetic, quick-witted, and love debating ideas, making them natural problem-solvers and innovators.",
            "quote": "“The unexamined life is not worth living.” – Socrates",
            "mbti_traits": ["Extraverted", "Intuitive", "Thinking", "Perceiving"],
            "strand_fit": {
                "STEM": "ENTPs may do well in STEM fields where innovation and critical thinking are required, such as engineering, technology, or research.",
                "ABM": "ENTPs’ persuasive skills and entrepreneurial mindset make them great fits for business, marketing, and sales.",
                "HUMSS": "HUMSS is a natural fit for ENTPs who enjoy philosophy, debate, politics, and media."
            },
            "strengths": [
                "Energetic", "Quick Thinker", "Charismatic", "Creative",
                "Persuasive", "Adaptable", "Knowledgeable"
            ],
            "weaknesses": [
                "Argumentative", "Insensitive", "Easily Bored",
                "Struggles with Structure", "Can Be Overly Competitive"
            ],
            "career_paths": [
                "Entrepreneur", "Lawyer", "Journalist",
                "Marketing Specialist", "Comedian", "Politician"
            ],
            "famous_people": [
                "Mark Twain", "Walt Disney", "Theodore Roosevelt",
                "Tom Hanks", "Barack Obama", "Sacha Baron Cohen"
            ]
        },
        #diplomats
        "INFJ": {
            "category": "The Advocate",
            "description": "Deep thinkers who are driven by purpose and values. Advocates seek meaning in everything they do and are passionate about helping others.",
            "quote": "“The only thing necessary for the triumph of evil is for good men to do nothing.” – Edmund Burke",
            "mbti_traits": ["Introverted", "Intuitive", "Feeling", "Judging"],
            "strand_fit": {
                "STEM": "Your ability to see the bigger picture and strong sense of responsibility make you a great fit for psychology, medicine, and environmental sciences. Your deep analytical skills can also be valuable in research-heavy fields like genetics and neuroscience.",
                "ABM": "Your leadership potential and strong communication skills allow you to excel in human resources, corporate leadership, and social entrepreneurship. Careers in ethical business practices and non-profit management align with your values.",
                "HUMSS": "Your empathy and deep understanding of people make you a natural fit for counseling, social work, philosophy, and advocacy. You may also thrive as a journalist, humanitarian worker, or diplomat."
            },
            "strengths": [
                "Insightful", "Principled", "Passionate",
                "Determined", "Altruistic", "Creative"
            ],
            "weaknesses": [
                "Overly Idealistic", "Sensitive to Criticism",
                "Prone to Burnout", "Too Private"
            ],
            "career_paths": [
                "Psychologist", "Counselor", "Social Worker",
                "Writer", "Diplomat", "Human Rights Advocate"
            ],
            "famous_people": [
                "Mahatma Gandhi", "Mother Teresa", "Carl Jung",
                "Martin Luther King Jr.", "Nelson Mandela"
            ]
        },
        "INFP": {
            "category": "The Mediator",
            "description": "Creative and deeply introspective individuals who value authenticity. Mediators are dreamers with a strong sense of purpose and imagination.",
            "quote": "“The only way to do great work is to love what you do.” – Steve Jobs",
            "mbti_traits": ["Introverted", "Intuitive", "Feeling", "Perceiving"],
            "strand_fit": {
                "STEM": "Your curiosity and love for understanding emotions can lead you to psychology, neuroscience, or environmental science. Fields that involve creativity, like game development and animation, may also be fulfilling.",
                "ABM": "Your ability to connect with people makes you a strong fit for branding, marketing, and social entrepreneurship. If you prefer creative independence, consider freelance writing or running a personal business.",
                "HUMSS": "Your love for storytelling and self-expression aligns well with careers in literature, philosophy, film, and the arts. INFPs also thrive in humanitarian work and counseling due to their empathetic nature."
            },
            "strengths": [
                "Creative", "Empathetic", "Open-Minded",
                "Loyal", "Passionate", "Insightful"
            ],
            "weaknesses": [
                "Overly Idealistic", "Easily Stressed",
                "Too Reserved", "Prone to Self-Doubt"
            ],
            "career_paths": [
                "Writer", "Poet", "Artist",
                "Therapist", "Humanitarian", "Musician"
            ],
            "famous_people": [
                "William Shakespeare", "J.R.R. Tolkien", "Princess Diana",
                "Johnny Depp", "Tim Burton"
            ]
        },
        "ENFJ": {
            "category": "The Protagonist",
            "description": "Charismatic and inspiring individuals who thrive on guiding others. Protagonists are natural-born leaders with a strong sense of purpose.",
            "quote": "“A leader is one who knows the way, goes the way, and shows the way.” – John C. Maxwell",
            "mbti_traits": ["Extroverted", "Intuitive", "Feeling", "Judging"],
            "strand_fit": {
                "STEM": "Your structured thinking and motivation to help others make you a great fit for healthcare, psychology, and public health. Research-based fields that allow you to make an impact, such as sustainability and climate studies, may also be fulfilling.",
                "ABM": "Your natural leadership and persuasive abilities allow you to excel in corporate management, public relations, and social entrepreneurship. You thrive in people-centered careers like HR and marketing.",
                "HUMSS": "With your charisma and ability to inspire others, you can thrive in politics, motivational speaking, education, and community organizing. You may also find fulfillment in journalism and media."
            },
            "strengths": [
                "Charismatic", "Inspiring", "Altruistic",
                "Confident", "Determined", "Empathetic"
            ],
            "weaknesses": [
                "Overly Idealistic", "Too Self-Sacrificing",
                "Prone to Burnout", "Can Be Overbearing"
            ],
            "career_paths": [
                "Teacher", "Politician", "Public Speaker",
                "Entrepreneur", "Community Organizer"
            ],
            "famous_people": [
                "Barack Obama", "Oprah Winfrey", "Maya Angelou",
                "Nelson Mandela", "Martin Luther King Jr."
            ]
        },
        "ENFP": {
            "category": "The Campaigner",
            "description": "Enthusiastic and free-spirited individuals who thrive on social connections. Campaigners are energetic, creative, and always ready to explore new ideas.",
            "quote": "“Stay hungry, stay foolish.” – Steve Jobs",
            "mbti_traits": ["Extroverted", "Intuitive", "Feeling", "Perceiving"],
            "strand_fit": {
                "STEM": "Your creativity and curiosity make you well-suited for psychology, neuroscience, and user experience (UX) design. You might also enjoy careers in technology-driven creative fields like game development.",
                "ABM": "Your enthusiasm and persuasive abilities make you an excellent fit for sales, advertising, and public relations. You thrive in fast-paced environments and excel in branding and entrepreneurship.",
                "HUMSS": "Your passion for storytelling and emotional depth make you a great fit for journalism, media, and the performing arts. You may also enjoy careers in social work, humanitarian work, or motivational speaking."
            },
            "strengths": [
                "Energetic", "Creative", "Sociable",
                "Inspiring", "Open-Minded", "Curious"
            ],
            "weaknesses": [
                "Easily Distracted", "Overly Idealistic",
                "Can Be Disorganized", "Prone to Overcommitting"
            ],
            "career_paths": [
                "Journalist", "Actor", "Entrepreneur",
                "Public Relations Specialist", "Motivational Speaker"
            ],
            "famous_people": [
                "Robin Williams", "Mark Twain", "Ellen DeGeneres",
                "Quentin Tarantino", "Walt Disney"
            ]
        },
#sentinels
        "ISTJ": {
            "category": "The Logistician",
            "description": "Responsible and dedicated individuals who value tradition, structure, and efficiency. Logisticians are practical and uphold high standards in everything they do.",
            "quote": "“Discipline is the bridge between goals and accomplishment.” – Jim Rohn",
            "mbti_traits": ["Introverted", "Sensing", "Thinking", "Judging"],
            "strand_fit": {
                "STEM": "Your methodical and detail-oriented nature makes STEM an excellent choice. With your strong analytical skills and precision, fields like engineering, accounting, and computer science suit your structured mindset. Your preference for efficiency also makes you well-suited for research-based careers in healthcare, such as medical laboratory science or pharmacy.",
                "ABM": "Your organizational skills and strategic thinking are highly valuable in business. As someone who values rules and structure, you may thrive in financial management, logistics, or operations. Your ability to analyze data and follow detailed procedures makes you a strong candidate for roles in accounting, auditing, and corporate management.",
                "HUMSS": "While ISTJs prefer structure over abstract ideas, their reliability and discipline make them well-suited for law, history, and governance. If you enjoy analyzing facts and enforcing regulations, careers in the legal field, public administration, or historical research may be fulfilling."
            },
            "strengths": [
                "Honest", "Strong-Willed", "Responsible",
                "Practical", "Organized", "Reliable", "Hardworking"
            ],
            "weaknesses": [
                "Stubborn", "Insensitive", "Always by the Book",
                "Uncomfortable with Change", "Judgmental"
            ],
            "career_paths": [
                "Accountant", "Military Officer", "Judge",
                "Auditor", "Financial Analyst"
            ],
            "famous_people": [
                "Angela Merkel", "George Washington", "Natalie Portman",
                "Henry Ford", "Jeff Bezos"
            ]
        },
        "ISFJ": {
            "category": "The Defender",
            "description": "Warm, caring, and dependable individuals who are deeply committed to their responsibilities. Defenders are protective and find fulfillment in helping others.",
            "quote": "“Success is not how high you have climbed, but how you make a positive difference to the world.” – Roy T. Bennett",
            "mbti_traits": ["Introverted", "Sensing", "Feeling", "Judging"],
            "strand_fit": {
                "STEM": "Your attention to detail, reliability, and strong work ethic make you well-suited for healthcare fields like nursing, physical therapy, and medical technology. ISFJs often excel in patient care because of their ability to work systematically while providing emotional support.",
                "ABM": "Your patience and sense of responsibility align well with human resources, hospitality management, and customer service roles. As a people-focused and organized individual, you can thrive in positions where maintaining workplace harmony and assisting others are key priorities.",
                "HUMSS": "Your natural empathy and desire to help others make careers in education, social work, and psychology excellent choices. ISFJs tend to form deep emotional connections, making them great counselors, teachers, and guidance advisers. Fields like journalism or advocacy may also be fulfilling as they allow you to amplify voices that need support."
            },
            "strengths": [
                "Supportive", "Reliable", "Patient",
                "Hardworking", "Loyal", "Practical", "Dedicated"
            ],
            "weaknesses": [
                "Too Altruistic", "Reluctant to Change", "Takes Things Personally",
                "Overcommitted", "Shy Around Strangers"
            ],
            "career_paths": [
                "Nurse", "Teacher", "Social Worker",
                "Human Resources Manager", "Psychologist"
            ],
            "famous_people": [
                "Mother Teresa", "Kate Middleton", "Queen Elizabeth II",
                "Vin Diesel", "Selena Gomez"
            ]
        },

        "ESTJ": {
            "category": "The Executive",
            "description": "Natural-born leaders who value order and efficiency. Executives are strong-willed, practical, and excellent at enforcing rules and structure.",
            "quote": "“Leadership is the capacity to translate vision into reality.” – Warren Bennis",
            "mbti_traits": ["Extroverted", "Sensing", "Thinking", "Judging"],
            "strand_fit": {
                "STEM": "Your structured mindset, leadership ability, and results-driven approach make fields like engineering, data science, and project management ideal for you. Your ability to enforce structure and optimize processes allows you to excel in technical fields that require precision, such as civil engineering, cybersecurity, or industrial engineering.",
                "ABM": "You naturally thrive in leadership roles, making management, entrepreneurship, and corporate finance great career paths. Your confidence and decisiveness suit high-pressure environments like investment banking, executive management, and business operations. Your ability to organize and enforce discipline is also valuable in supply chain management.",
                "HUMSS": "While you are more practical than philosophical, your confidence and leadership skills allow you to succeed in governance, law, and politics. If you enjoy making executive decisions and leading organizations, careers in public administration, corporate law, or international relations may align with your strengths."
            },
            "strengths": [
                "Dedicated", "Strong-Willed", "Direct",
                "Honest", "Loyal", "Organized", "Efficient"
            ],
            "weaknesses": [
                "Inflexible", "Stubborn", "Insensitive",
                "Bossy", "Unwilling to Listen to Others"
            ],
            "career_paths": [
                "CEO", "Judge", "Military Officer",
                "Operations Manager", "Government Official"
            ],
            "famous_people": [
                "Margaret Thatcher", "Franklin D. Roosevelt", "Judge Judy",
                "John D. Rockefeller", "Michelle Obama"
            ]
        },

        "ESFJ": {
            "category": "The Consul",
            "description": "Caring and social individuals who thrive in maintaining harmony. Consuls are highly attuned to the emotions of others and enjoy bringing people together.",
            "quote": "“The best way to find yourself is to lose yourself in the service of others.” – Mahatma Gandhi",
            "mbti_traits": ["Extroverted", "Sensing", "Feeling", "Judging"],
            "strand_fit": {
                "STEM": "Your teamwork skills, strong communication, and reliability make healthcare and education within STEM excellent choices. Nursing, medical assistance, and healthcare administration suit your ability to care for others while working in structured environments. If you enjoy teamwork, careers in environmental science or food and nutrition may also be fulfilling.",
                "ABM": "Your people skills, enthusiasm, and ability to manage social dynamics make you a strong candidate for sales, marketing, and public relations. You excel in customer-facing roles, whether as a hotel manager, HR professional, or business consultant. Careers that require maintaining harmony, such as event planning, are also great fits.",
                "HUMSS": "With your sociability and emotional intelligence, you can thrive in fields such as teaching, media, and counseling. ESFJs naturally excel in education, public relations, and humanitarian work. Journalism, motivational speaking, and hosting are also excellent paths due to your ability to engage and inspire others."
            },
            "strengths": [
                "Supportive", "Outgoing", "Loyal",
                "Sensitive", "Hardworking", "Team-Oriented", "Warm"
            ],
            "weaknesses": [
                "Overly Selfless", "Need for Validation", "Too Sensitive",
                "Resistant to Change", "Worried About Social Status"
            ],
            "career_paths": [
                "Teacher", "Social Worker", "Public Relations Specialist",
                "Nurse", "Customer Service Manager"
            ],
            "famous_people": [
                "Taylor Swift", "Jennifer Lopez", "Bill Clinton",
                "Hugh Jackman", "Oprah Winfrey"
            ]
        },
#explorers
        "ISTP": {
            "category": "The Virtuoso",
            "description": "Bold and practical experimenters, masters of all kinds of tools. ISTPs love taking things apart, learning how they work, and finding innovative ways to improve them.",
            "quote": "“The important thing is not to stop questioning. Curiosity has its own reason for existing.” – Albert Einstein",
            "mbti_traits": ["Introverted", "Sensing", "Thinking", "Perceiving"],
            "strand_fit": {
                "STEM": "Your hands-on approach and love for problem-solving align well with STEM fields such as engineering, mechanics, and technology.",
                "ABM": "Your ability to adapt, take risks, and think critically makes you a strong fit for the business world, particularly in entrepreneurship.",
                "HUMSS": "While not a typical fit, ISTPs with an interest in human behavior may enjoy areas like psychology or philosophy."
            },
            "strengths": [
                "Practical", "Creative Problem-Solver", "Curious", "Adaptable",
                "Logical Thinker", "Independent", "Energetic"
            ],
            "weaknesses": [
                "Insensitive", "Easily Bored", "Risk-Taking",
                "Difficulty with Long-Term Commitments", "Impulsive"
            ],
            "career_paths": [
                "Engineer", "Mechanic", "Forensic Scientist",
                "Entrepreneur", "Software Developer", "Pilot"
            ],
            "famous_people": [
                "Steve Jobs", "Bruce Lee", "Michael Jordan",
                "Amelia Earhart", "Tom Cruise"
            ]
        },
        "ISFP": {
            "category": "The Adventurer",
            "description": "Flexible and charming artists, always ready to explore and experience something new. ISFPs are deeply in touch with their emotions and have a strong appreciation for beauty and aesthetics.",
            "quote": "“Every artist was first an amateur.” – Ralph Waldo Emerson",
            "mbti_traits": ["Introverted", "Sensing", "Feeling", "Perceiving"],
            "strand_fit": {
                "STEM": "ISFPs who enjoy hands-on learning may excel in applied sciences, environmental studies, or design-related fields.",
                "ABM": "Their creative and innovative mindset makes them suitable for marketing, branding, and customer experience roles in business.",
                "HUMSS": "ISFPs thrive in HUMSS, as they are expressive, artistic, and deeply connected to emotions, making careers in literature, music, and psychology appealing."
            },
            "strengths": [
                "Creative", "Artistic", "Independent", "Spontaneous",
                "Sensitive to Aesthetics", "Adventurous", "Kind"
            ],
            "weaknesses": [
                "Easily Stressed", "Avoids Conflict", "Indecisive",
                "Dislikes Criticism", "Private"
            ],
            "career_paths": [
                "Graphic Designer", "Musician", "Photographer",
                "Fashion Designer", "Social Worker", "Writer"
            ],
            "famous_people": [
                "Frida Kahlo", "Lana Del Rey", "Bob Dylan",
                "Britney Spears", "Kevin Costner"
            ]
        },

        "ESTP": {
            "category": "The Entrepreneur",
            "description": "Smart, energetic, and perceptive, ESTPs love engaging in the moment and taking risks. They are action-oriented and enjoy solving problems with quick thinking and adaptability.",
            "quote": "“Opportunities multiply as they are seized.” – Sun Tzu",
            "mbti_traits": ["Extraverted", "Sensing", "Thinking", "Perceiving"],
            "strand_fit": {
                "STEM": "ESTPs who enjoy high-energy environments may excel in fields like engineering, sports science, or emergency medical services.",
                "ABM": "Their confidence and charisma make them ideal for sales, marketing, and business leadership roles.",
                "HUMSS": "ESTPs with an interest in communication and debate may thrive in law, media, or political science."
            },
            "strengths": [
                "Charismatic", "Energetic", "Bold", "Practical Thinker",
                "Direct", "Spontaneous", "Natural Leader"
            ],
            "weaknesses": [
                "Impulsive", "Competitive", "Insensitive",
                "Easily Bored", "Risk-Taking"
            ],
            "career_paths": [
                "Entrepreneur", "Sales Executive", "Stockbroker",
                "Athlete", "Lawyer", "Media Personality"
            ],
            "famous_people": [
                "Donald Trump", "Madonna", "Eddie Murphy",
                "Samuel L. Jackson", "Ernest Hemingway"
            ]
        },

        "ESFP": {
            "category": "The Entertainer",
            "description": "Spontaneous, energetic, and enthusiastic people—life is never boring around them. ESFPs live in the moment and love to spread joy, making them natural entertainers.",
            "quote": "“You only live once, but if you do it right, once is enough.” – Mae West",
            "mbti_traits": ["Extraverted", "Sensing", "Feeling", "Perceiving"],
            "strand_fit": {
                "STEM": "While not a common choice, ESFPs may excel in health sciences or sports-related fields where interaction and hands-on work are emphasized.",
                "ABM": "Their natural charm makes them excellent in sales, marketing, and public relations.",
                "HUMSS": "ESFPs are a perfect fit for HUMSS, as they thrive in artistic, expressive, and social environments like acting, media, and journalism."
            },
            "strengths": [
                "Energetic", "Social", "Optimistic", "Creative",
                "Observant", "Spontaneous", "Lively"
            ],
            "weaknesses": [
                "Easily Distracted", "Impulsive", "Struggles with Long-Term Plans",
                "Sensitive to Criticism", "Dislikes Structure"
            ],
            "career_paths": [
                "Actor", "Dancer", "Musician",
                "Public Speaker", "Social Media Influencer", "Event Planner"
            ],
            "famous_people": [
                "Elvis Presley", "Marilyn Monroe", "Jamie Foxx",
                "Miley Cyrus", "Hugh Jackman"
            ]
        },
    }
#Weighted Scoring Algorithm (Main Formula for Strand Recommendation)
def calculate_strand_score(confidence_levels, weights):
    return sum(confidence_levels[i] * weights[i] for i in range(len(confidence_levels)))

# Example for STEM
confidence_levels = [5, 4, 3]  # Example confidence values
weights = [1.2, 0.5, 0.3]  # Corresponding weights
stem_score = calculate_strand_score(confidence_levels, weights)
print("STEM Score:", stem_score)

range_leveler = {
    "ss":{

   }
}
#Sorting Algorithm (Ranking the Strands)
strand_scores = {"STEM": 8.9, "ABM": 7.5, "HUMSS": 6.2}
sorted_strands = sorted(strand_scores.items(), key=lambda x: x[1], reverse=True)

print(sorted_strands)  # [('STEM', 8.9), ('ABM', 7.5), ('HUMSS', 6.2)]
