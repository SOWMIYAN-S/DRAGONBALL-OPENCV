import cv2
from cvzone.HandTrackingModule import HandDetector
import keyboard  # Using the keyboard library

# Initialize video capture
video = cv2.VideoCapture(0)

cv2.namedWindow("DragonBall Controller", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("DragonBall Controller", cv2.WND_PROP_TOPMOST, 1)

detector = HandDetector(detectionCon=0.7, maxHands=2)

while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:
        for hand in hands:
            finger = detector.fingersUp(hand)

            if hand["type"] == "Right":
                if finger == [1, 0, 0, 0, 0]:  # Left gesture
                    print("Left")
                    cv2.putText(img, "Left", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press("a")
                    keyboard.release("d")
                    keyboard.release("w")
                    keyboard.release("s")

                elif finger == [0, 0, 0, 0, 1]:  # Right gesture
                    print("Right")
                    cv2.putText(img, "Right", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press("d")
                    keyboard.release("a")
                    keyboard.release("w")
                    keyboard.release("s")

                elif finger == [0, 1, 0, 0, 0]:  # Up gesture
                    print("Up")
                    cv2.putText(img, "Up", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press("w")
                    keyboard.release("a")
                    keyboard.release("d")
                    keyboard.release("s")

                elif finger == [0, 1, 1, 0, 0]:  # Down gesture
                    print("Down")
                    cv2.putText(img, "Down", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press("s")
                    keyboard.release("a")
                    keyboard.release("d")
                    keyboard.release("w")

            if hand["type"] == "Left":
                if finger == [1, 0, 0, 0, 0]:  # Left punch
                    print("LEFT PUNCH")
                    cv2.putText(img, "LEFT PUNCH", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press('u')
                    keyboard.release('i')
                    keyboard.release('k')
                    keyboard.release('j')
                    keyboard.release('l')
                    keyboard.release("a")
                    keyboard.release('o')
                    keyboard.release('p')
                    keyboard.release(';')

                elif finger == [0, 0, 0, 0, 1]:  # Right punch
                    print("RIGHT PUNCH")
                    cv2.putText(img, "RIGHT PUNCH", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press("i")
                    keyboard.release("u")
                    keyboard.release("k")
                    keyboard.release("j")
                    keyboard.release("l")
                    keyboard.release("o")
                    keyboard.release("p")
                    keyboard.release("a")
                    keyboard.release(";")

                elif finger == [0, 0, 1, 0, 0]:  # Kick
                    print("KICK")
                    cv2.putText(img, "KICK", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press("k")
                    keyboard.release("u")
                    keyboard.release("i")
                    keyboard.release("j")
                    keyboard.release("l")
                    keyboard.release("o")
                    keyboard.release("p")
                    keyboard.release(";")
                    keyboard.release("a")

                elif finger == [0, 1, 0, 0, 0]:  # Attack 1
                    print("ATTACK 1")
                    cv2.putText(img, "ATTACK 1", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press("j")
                    keyboard.release("u")
                    keyboard.release("i")
                    keyboard.release("k")
                    keyboard.release("l")
                    keyboard.release("o")
                    keyboard.release("p")
                    keyboard.release("a")
                    keyboard.release(";")

                elif finger == [1, 1, 1, 1, 1]:  # Power attack
                    print("POWER ATTACK")
                    cv2.putText(img, "POWER ATTACK", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press("p")
                    keyboard.release("u")
                    keyboard.release("i")
                    keyboard.release("k")
                    keyboard.release("j")
                    keyboard.release("l")
                    keyboard.release("o")
                    keyboard.release(";")
                    keyboard.release("a")

                elif finger == [0, 1, 1, 0, 0]:  # Attack 2
                    print("ATTACK 2")
                    cv2.putText(img, "ATTACK 2", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press(";")
                    keyboard.release("a")
                    keyboard.release("u")
                    keyboard.release("i")
                    keyboard.release("k")
                    keyboard.release("j")
                    keyboard.release("l")
                    keyboard.release("o")
                    keyboard.release("p")

                elif finger == [1, 1, 0, 0, 0]:  # Player 2
                    print("PLAYER 2")
                    cv2.putText(img, "PLAYER 2", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press("l")
                    keyboard.release("u")
                    keyboard.release("i")
                    keyboard.release("k")
                    keyboard.release("j")
                    keyboard.release("o")
                    keyboard.release("p")
                    keyboard.release(";")
                    keyboard.release("a")

                elif finger == [1, 1, 1, 0, 0]:  # Player 3
                    print("PLAYER 3")
                    cv2.putText(img, "PLAYER 3", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press("o")
                    keyboard.release("a")
                    keyboard.release("u")
                    keyboard.release("i")
                    keyboard.release("k")
                    keyboard.release("j")
                    keyboard.release("l")
                    keyboard.release("p")
                    keyboard.release(";")

    # Show the image
    cv2.imshow("DragonBall Controller", img)
    
    # Exit condition
    if cv2.waitKey(1) == ord("q"):
        break

# Clean up
video.release()
cv2.destroyAllWindows()
