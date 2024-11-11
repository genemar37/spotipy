""" The list 'data' contains information about 10 artists, and each of them is represented as a dictionary with the following keys: name, email, registration date, listeners and songs which is a list of dictionaries, where each dictionary represents a song by the artist with: title, streams and duration """


data = [

	# Information about Billie Eilish
	{
		"name": "Billie Eilish",
		"email": "billie@email.com",
		"registration_date" : "31-12-2015",
		"listeners": 107622710,
		"songs": [
			{
				"title": "BIRDS OF A FEATHER",
				"streams": 864283865,
				"duration": "03:30"
			},
			{
				"title": "Guess",
				"streams": 122657920,
				"duration": "02:23"
			},
			{
				"title": "LUNCH",
				"streams": 464059474,
				"duration": "02:59"
			},
			{
				"title": "CHIHIRO",
				"streams": 375007589,
				"duration": "05:03"
			},
			{
				"title": "WILDFLOWER",
				"streams": 259599050,
				"duration": "04:21"
			}
		]
	},


	# Information about The Weeknd
	{
		"name": "The Weeknd",
		"email": "theweeknd@email.com",
		"registration_date" : "14-07-2011",
		"listeners": 105320511,
		"songs": [
			{
				"title": "One Of The Girls",
				"streams": 1160986353,
				"duration": "04:04"
			},
			{
				"title": "Blinding Lights",
				"streams": 4416175981,
				"duration": "03:20"
			},
			{
				"title": "Starboy",
				"streams": 3430885989,
				"duration": "03:50"
			},
			{
				"title": "Die For You",
				"streams": 2381044926,
				"duration": "04:20"
			},
			{
				"title": "Popular",
				"streams": 902000426,
				"duration": "03:35"           
			}
		]
	},


	# Information about Taylor Swift
	{
		"name": "Taylor Swift",
		"email": "taylor@email.com",
		"registration_date" : "15-08-2011",
		"listeners": 95847075,
		"songs": [
			{
				"title": "Cruel Summer",
				"streams": 2415554506,
				"duration": "02:58"
			},
			{
				"title": "Fortnight",
				"streams": 605902363,
				"duration": "03:48"
			},
			{
				"title": "I Can Do It With a Broken Heart",
				"streams": 403790954,
				"duration": "03:38"
			},
			{
				"title": "august",
				"streams": 1205711572,
				"duration": "04:21"
			},
			{
				"title": "Lover",
				"streams": 1509091504,
				"duration": "03:41"
			}
		]
	},


	# Information about Bruno Mars
	{
		"name": "Bruno Mars",
		"email": "bruno@email.com",
		"registration_date" : "16-09-2011",
		"listeners": 88579433,
		"songs": [
			{
				"title": "Die With A Smile",
				"streams": 93624759,
				"duration": "04:11"
			},
			{
				"title": "When I Was Your Man",
				"streams": 2220463100,
				"duration": "03:33"
			},
			{
				"title": "Locked out of Heaven",
				"streams": 2135034273,
				"duration": "03:53"
			},
			{
				"title": "Just the Way You Are",
				"streams": 2215109245,
				"duration": "03:40"
			},
			{
				"title": "That's What I Like",
				"streams": 2168363698,
				"duration": "03:26"
			}
		]
	},


	# Information about Rihanna
	{
		"name": "Rihanna",
		"email": "rihanna@email.com",
		"registration_date" : "17-10-2011",
		"listeners": 84890256,
		"songs": [
			{
				"title": "We Found Love",
				"streams": 1758996294,
				"duration": "03:35" 
			},
			{
				"title": "This Is What You Came For",
				"streams": 1833251946,
				"duration": "03:41" 
			},
			{
				"title": "Only Girl (In The World)",
				"streams": 1164166203,
				"duration": "03:55" 
			},
			{
				"title": "Umbrella",
				"streams": 1610578608,
				"duration": "04:35" 
			},
			{
				"title": "S&M",
				"streams": 1101284049,
				"duration": "04:03" 
			}
		]
	},


	# Information about Ariana Grande
	{
		"name": "Ariana Grande",
		"email": "ariana@email.com",
		"registration_date" : "30-12-2011",
		"listeners": 76886482,
		"songs": [
			{
				"title": "we can't be friends (wait for your love)",
				"streams": 824534939,
				"duration": "03:48"
			},
			{
				"title": "the boy is mine",
				"streams": 288066739,
				"duration": "02:53"
			},
			{
				"title": "intro (end of the world)",
				"streams": 297434684,
				"duration": "01:32"
			},
			{
				"title": "Save Your Tears (Remix)",
				"streams": 161640992,
				"duration": "03:11"
			},
			{
				"title": "yes, and?",
				"streams": 481610607,
				"duration": "03:34"
			}
		]
	},


	# Information about Dua Lipa
	{
		"name": "Dua Lipa",
		"listeners": 72287110,
		"email": "dua@email.com",
		"registration_date" : "02-06-2017",
		"songs": [
			{
				"title": "Cold Heart - PNAU Remix",
				"streams": 2106992357,
				"duration": "03:22"
			},
			{
				"title": "Training Season",
				"streams": 352743782, 
				"duration": "03:29"           
			},
			{
				"title": "Don't Start Now",
				"streams": 2699187853,
				"duration": "03:03"
			},
			{
				"title": "Houdini",
				"streams": 586811729, 
				"duration": "03:05"           
			},
			{
				"title": "One Kiss",
				"streams": 2253569954,
				"duration": "03:34"
			}
		]
	},


	# Information about Kendrick Lamar
	{
		"name": "Kendrick Lamar",
		"email": "kendrick@email.com",
		"registration_date" : "18-11-2011",
		"listeners": 70739936,
		"songs": [
			{
				"title": "Not Like Us",
				"streams": 713004250,
				"duration": "04:34"            
			},
			{
				"title": "Like That",
				"streams": 497507169,
				"duration": "04:27"            
			},
			{
				"title": "All The Stars",
				"streams": 1740970789,
				"duration": "03:52"
			},
			{
				"title": "Money Trees",
				"streams": 1563067806,
				"duration": "06:26"
			},
			{
				"title": "HUMBLE.",
				"streams": 2312568855,
				"duration": "02:57"
			}
		]
	},


	# Information about Bad Bunny
	{
		"name": "Bad Bunny",
		"email": "badbunny@email.com",
		"registration_date" : "26-08-2016",
		"listeners": 65341600,
		"songs": [
			{
				"title": "ADIVINO",
				"streams": 246154185,
				"duration": "04:38"
			},
			{
				"title": "PERRO NEGRO",
				"streams": 799475751,
				"duration": "02:42"
			},
			{
				"title": "LA CANCIÓN",
				"streams": 1784589610,
				"duration": "04:02",
			},
			{
				"title": "Me Porto Bonito",
				"streams": 1883361384,
				"duration": "02:58",
			},
			{
				"title": "un x100to",
				"streams": 1072446134,
				"duration": "03:14",
			}
		]
	},
	

	# Information about Shakira
	{
		"name": "Shakira",
		"listeners": 65134527,
		"email": "shakira@email.com",
		"registration_date" : "19-12-2011",
		"songs": [
			{
				"title": "Hips Don't Lie",
				"streams": 1748115828,
				"duration": "03:38"
			},
			{
				"title": "TQG",
				"streams": 1096746867,
				"duration": "03:17"
			},
			{
				"title": "Dia de Enero",
				"streams": 401040817,
				"duration": "02:53"
			},
			{
				"title": "Antologia",
				"streams": 418617373,
				"duration": "04:14"
			},
			{
				"title": "Inevitable",
				"streams": 394198855,
				"duration": "03:12"
			}
		]
	}
]