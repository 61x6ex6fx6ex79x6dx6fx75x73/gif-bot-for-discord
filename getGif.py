import tenorpy

CONFIDENCE_MIN = 1

def getGif(name):

	if "trap" in name:
		return None, 0

	toSeach = "anime" + name.replace("_", " ")

	t = tenorpy.Tenor()

	confidence = len(t.search(toSeach)["results"]) * 10
	
	if confidence >= CONFIDENCE_MIN:
		return t.random(toSeach), confidence
	else:
		return None, confidence


