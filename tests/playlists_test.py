import src.spotimy_playlists as sp

def test_get_num():

	x = sp.Playlists()
	num = x.get_num()
	assert (num >=0) and (num < 1)
