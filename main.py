import person_detection


if __name__ == "__main__":
	for i in range(1, 4):
		person_detection.detector(f"{str(i)}.jpg")