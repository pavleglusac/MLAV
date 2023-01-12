import cv2 as cv


def calculate_keypoints(image, keypoints):
	image_width, image_height = image.shape[1], image.shape[0]

	landmark_point = []

	for _, landmark in enumerate(keypoints.landmark):
		landmark_x = min(int(landmark.x * image_width), image_width - 1)
		landmark_y = min(int(landmark.y * image_height), image_height - 1)
		landmark_z = landmark.z
		landmark_point.append([landmark_x, landmark_y, landmark_z])

	return landmark_point


def draw_keypoints(image, keypoints):
	if len(keypoints) > 0:
		keypoints = [(x[0], x[1]) for x in keypoints]

		cv.line(image, tuple(keypoints[0]), tuple(keypoints[9]), (0, 0, 200), 6)

		# Thumb

		cv.line(image, tuple(keypoints[2]), tuple(keypoints[3]), (255, 255, 255), 6)
		cv.line(image, tuple(keypoints[3]), tuple(keypoints[4]), (255, 255, 255), 6)
		# Index finger
		cv.line(image, tuple(keypoints[5]), tuple(keypoints[6]), (255, 255, 255), 6)

		cv.line(image, tuple(keypoints[6]), tuple(keypoints[7]), (255, 255, 255), 6)

		cv.line(image, tuple(keypoints[7]), tuple(keypoints[8]), (255, 255, 255), 6)

		# Middle finger
		cv.line(image, tuple(keypoints[9]), tuple(keypoints[10]), (255, 255, 255), 6)
		cv.line(image, tuple(keypoints[10]), tuple(keypoints[11]), (255, 255, 255), 6)

		cv.line(image, tuple(keypoints[11]), tuple(keypoints[12]), (255, 255, 255), 6)

		# Ring finger
		cv.line(image, tuple(keypoints[13]), tuple(keypoints[14]), (255, 255, 255), 6)

		cv.line(image, tuple(keypoints[14]), tuple(keypoints[15]), (255, 255, 255), 6)

		cv.line(image, tuple(keypoints[15]), tuple(keypoints[16]), (255, 255, 255), 6)

		# Little finger
		cv.line(image, tuple(keypoints[17]), tuple(keypoints[18]), (255, 255, 255), 6)

		cv.line(image, tuple(keypoints[18]), tuple(keypoints[19]), (255, 255, 255), 6)

		cv.line(image, tuple(keypoints[19]), tuple(keypoints[20]), (255, 255, 255), 6)

		# Palm
		cv.line(image, tuple(keypoints[0]), tuple(keypoints[1]), (255, 255, 255), 6)

		cv.line(image, tuple(keypoints[1]), tuple(keypoints[2]), (255, 255, 255), 6)

		cv.line(image, tuple(keypoints[2]), tuple(keypoints[5]), (255, 255, 255), 6)

		cv.line(image, tuple(keypoints[5]), tuple(keypoints[9]), (255, 255, 255), 6)

		cv.line(image, tuple(keypoints[9]), tuple(keypoints[13]), (255, 255, 255), 6)

		cv.line(image, tuple(keypoints[13]), tuple(keypoints[17]), (255, 255, 255), 6)

		cv.line(image, tuple(keypoints[17]), tuple(keypoints[0]), (255, 255, 255), 6)

	# Key Points
	for index, landmark in enumerate(keypoints):
		if index == 0:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 1:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 2:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 3:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 4:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 5:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 6:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 7:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 8:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 9:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 10:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 11:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 12:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 13:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 14:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 15:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 16:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 17:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 18:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 19:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)
		if index == 20:
			cv.circle(image, (landmark[0], landmark[1]), 5, (0, 255, 0), -1)

	return image
