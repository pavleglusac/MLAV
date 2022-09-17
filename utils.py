
import cv2 as cv

def calculate_landmarks(image, landmarks):
    image_width, image_height = image.shape[1], image.shape[0]

    landmark_point = []

    for _, landmark in enumerate(landmarks.landmark):
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)
        landmark_z = landmark.z
        landmark_point.append([landmark_x, landmark_y, landmark_z])

    return landmark_point


def draw_landmarks(image, landmarks):
    if len(landmarks) > 0:
        # Thumb
        landmarks = [(x[0], x[1]) for x in landmarks]


        cv.line(image, tuple(landmarks[2]), tuple(landmarks[3]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[2]), tuple(landmarks[3]),
                (255, 255, 255), 2)
        cv.line(image, tuple(landmarks[3]), tuple(landmarks[4]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[3]), tuple(landmarks[4]),
                (255, 255, 255), 2)

        # Index finger
        cv.line(image, tuple(landmarks[5]), tuple(landmarks[6]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[5]), tuple(landmarks[6]),
                (255, 255, 255), 2)
        cv.line(image, tuple(landmarks[6]), tuple(landmarks[7]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[6]), tuple(landmarks[7]),
                (255, 255, 255), 2)
        cv.line(image, tuple(landmarks[7]), tuple(landmarks[8]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[7]), tuple(landmarks[8]),
                (255, 255, 255), 2)

        # Middle finger
        cv.line(image, tuple(landmarks[9]), tuple(landmarks[10]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[9]), tuple(landmarks[10]),
                (255, 255, 255), 2)
        cv.line(image, tuple(landmarks[10]), tuple(landmarks[11]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[10]), tuple(landmarks[11]),
                (255, 255, 255), 2)
        cv.line(image, tuple(landmarks[11]), tuple(landmarks[12]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[11]), tuple(landmarks[12]),
                (255, 255, 255), 2)

        # Ring finger
        cv.line(image, tuple(landmarks[13]), tuple(landmarks[14]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[13]), tuple(landmarks[14]),
                (255, 255, 255), 2)
        cv.line(image, tuple(landmarks[14]), tuple(landmarks[15]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[14]), tuple(landmarks[15]),
                (255, 255, 255), 2)
        cv.line(image, tuple(landmarks[15]), tuple(landmarks[16]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[15]), tuple(landmarks[16]),
                (255, 255, 255), 2)

        # Little finger
        cv.line(image, tuple(landmarks[17]), tuple(landmarks[18]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[17]), tuple(landmarks[18]),
                (255, 255, 255), 2)
        cv.line(image, tuple(landmarks[18]), tuple(landmarks[19]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[18]), tuple(landmarks[19]),
                (255, 255, 255), 2)
        cv.line(image, tuple(landmarks[19]), tuple(landmarks[20]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[19]), tuple(landmarks[20]),
                (255, 255, 255), 2)

        # Palm
        cv.line(image, tuple(landmarks[0]), tuple(landmarks[1]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[0]), tuple(landmarks[1]),
                (255, 255, 255), 2)
        cv.line(image, tuple(landmarks[1]), tuple(landmarks[2]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[1]), tuple(landmarks[2]),
                (255, 255, 255), 2)
        cv.line(image, tuple(landmarks[2]), tuple(landmarks[5]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[2]), tuple(landmarks[5]),
                (255, 255, 255), 2)
        cv.line(image, tuple(landmarks[5]), tuple(landmarks[9]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[5]), tuple(landmarks[9]),
                (255, 255, 255), 2)
        cv.line(image, tuple(landmarks[9]), tuple(landmarks[13]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[9]), tuple(landmarks[13]),
                (255, 255, 255), 2)
        cv.line(image, tuple(landmarks[13]), tuple(landmarks[17]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[13]), tuple(landmarks[17]),
                (255, 255, 255), 2)
        cv.line(image, tuple(landmarks[17]), tuple(landmarks[0]),
                (0, 0, 0), 6)
        cv.line(image, tuple(landmarks[17]), tuple(landmarks[0]),
                (255, 255, 255), 2)

    # Key Points
    for index, landmark in enumerate(landmarks):
        if index == 0:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 1:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 2:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 3:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 4:
            cv.circle(image, (landmark[0], landmark[1]), 8, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 8, (0, 0, 0), 1)
        if index == 5:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 6:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 7:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 8:
            cv.circle(image, (landmark[0], landmark[1]), 8, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 8, (0, 0, 0), 1)
        if index == 9:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 10:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 11:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 12:
            cv.circle(image, (landmark[0], landmark[1]), 8, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 8, (0, 0, 0), 1)
        if index == 13:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 14:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 15:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), 1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 16:
            cv.circle(image, (landmark[0], landmark[1]), 8, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 8, (0, 0, 0), 1)
        if index == 17:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 18:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 19:
            cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
        if index == 20:
            cv.circle(image, (landmark[0], landmark[1]), 8, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 8, (0, 0, 0), 1)

    return image

