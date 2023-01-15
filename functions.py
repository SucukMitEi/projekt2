CHAR = "▀"

def calculateBG(color, background):
	alpha = color[3] / 255
	oneminusalpha = 1 - alpha

	newR = (color[0] * alpha) + (oneminusalpha * background[0])
	newG = (color[1] * alpha) + (oneminusalpha * background[1])
	newB = (color[2] * alpha) + (oneminusalpha * background[2])
	return [newR, newG, newB]


def FG_RGB(r, g, b):
	return f"\x1b[38;2;{round(r)};{round(g)};{round(b)}m"


def BG_RGB(r, g, b):
	return f"\x1b[48;2;{round(r)};{round(g)};{round(b)}m"


def chunks(l, n):
	return [l[i : i + n] for i in range(0, len(l), n)]
