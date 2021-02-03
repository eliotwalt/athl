from datetime import datetime

# Static arguments
url = 'https://www.swiss-athletics.ch/fr/page-daccueil-listes-des-meilleurs/'
prefix = 'form_anonym:bestlist'
fields = {
	'year': f'{prefix}Year',
	'season': f'{prefix}Season',
	'category': f'{prefix}Category',
	'discipline': f'{prefix}Discipline_label',
	'list_type': f'{prefix}Type',
	'max_res': f'{prefix}Tops',
}
year_now = datetime.now.year
years = list(range(2006, year_now+1))
season = f'{prefix}Season_0'
men_category = f'{prefix}Category_1'
women_category = f'{prefix}Category_2'
list_type = f'{prefix}Type_1' # 1 result per athlet
max_res = f'{prefix}Tops_4' # 5000 results
submit_button = 'form_anonym:loadDataBtn'
disciplines = ['800',
               '1500',
               '3000',
               '3000steeple',
               '5000',
               '10000']

# helpers
def year_id(year_target):
	global year_now
	global prefix
	return f'{prefix}Year_{str(year_target - year_now + 1)}'
def discipline_id(num):
	global prefix
	return f'{prefix}Discipline_{str(num)}'

# Disciplines ids
discipline_cfg = {
	'2006': {
		'men': {
			'800': discipline_id(10),
			'1500': discipline_id(12),
			'3000': discipline_id(14),
			'3000steeple': discipline_id(30),
			'5000': discipline_id(15),
			'10000': discipline_id(16),
		},
		'women': {
			'800': discipline_id(10),
			'1500': discipline_id(12),
			'3000': discipline_id(15),
			'3000steeple': discipline_id(27),
			'5000': discipline_id(16),
			'10000': discipline_id(17),
		}
	},
	'2007': {
		'men': {
			'800': discipline_id(10),
			'1500': discipline_id(12),
			'3000': discipline_id(14),
			'3000steeple': discipline_id(32),
			'5000': discipline_id(15),
			'10000': discipline_id(16),
		},
		'women': {
			'800': discipline_id(10),
			'1500': discipline_id(12),
			'3000': discipline_id(14),
			'3000steeple': discipline_id(27),
			'5000': discipline_id(15),
			'10000': discipline_id(16),
		}
	},
	'2008': {
		'men': {
			'800': discipline_id(10),
			'1500': discipline_id(12),
			'3000': discipline_id(14),
			'3000steeple': discipline_id(30),
			'5000': discipline_id(15),
			'10000': discipline_id(16),
		},
		'women': {
			'800': discipline_id(10),
			'1500': discipline_id(12),
			'3000': discipline_id(14),
			'3000steeple': discipline_id(26),
			'5000': discipline_id(15),
			'10000': discipline_id(16),
		}
	},
	'2009': {
		'men': {
			'800': discipline_id(10),
			'1500': discipline_id(12),
			'3000': discipline_id(15),
			'3000steeple': discipline_id(32),
			'5000': discipline_id(16),
			'10000': discipline_id(17),
		},
		'women': {
			'800': discipline_id(10),
			'1500': discipline_id(12),
			'3000': discipline_id(14),
			'3000steeple': discipline_id(26),
			'5000': discipline_id(15),
			'10000': discipline_id(16),
		}
	},
	'2010': {
		'men': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(15),
			'3000steeple': discipline_id(32),
			'5000': discipline_id(16),
			'10000': discipline_id(17),
		},
		'women': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(15),
			'3000steeple': discipline_id(28),
			'5000': discipline_id(16),
			'10000': discipline_id(17),
		}
	},
	'2011': {
		'men': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(35),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
		},
		'women': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(32),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
		}
	},
	'2012': {
		'men': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(35),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
		},
		'women': {
			'800': discipline_id(10),
			'1500': discipline_id(12),
			'3000': discipline_id(15),
			'3000steeple': discipline_id(31),
			'5000': discipline_id(16),
			'10000': discipline_id(17),
		}
	},
	'2013': {
		'men': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(37),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
		},
		'women': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(31),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
	},
	'2014': {
		'men': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(34),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
		},
		'women': {
			'800': discipline_id(12),
			'1500': discipline_id(14),
			'3000': discipline_id(17),
			'3000steeple': discipline_id(31),
			'5000': discipline_id(18),
			'10000': discipline_id(19),
		}
	},
	'2015': {
		'men': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(34),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
		},
		'women': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(33),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
		}
	},
	'2016': {
		'men': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(36),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
		},
		'women': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(31),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
		}
	},
	'2017': {
		'men': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(36),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
		},
		'women': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(32),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
		}
	},
	'2018': {
		'men': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(15),
			'3000steeple': discipline_id(34),
			'5000': discipline_id(16),
			'10000': discipline_id(17),
		},
		'women': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(15),
			'3000steeple': discipline_id(31),
			'5000': discipline_id(16),
			'10000': discipline_id(17),
		}
	},
	'2019': {
		'men': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(40),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
		},
		'women': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(34),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
		}
	},
	'2020': {
		'men': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(38),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
		},
		'women': {
			'800': discipline_id(11),
			'1500': discipline_id(13),
			'3000': discipline_id(16),
			'3000steeple': discipline_id(33),
			'5000': discipline_id(17),
			'10000': discipline_id(18),
		}
	},
}
