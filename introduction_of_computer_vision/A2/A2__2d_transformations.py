import cv2
import numpy as np
import math

def get_transformed_image(img, M):
    board = np.full((801,801),255)
    cornery, cornerx =[], []
    for h in range(1,img.shape[0]-1):
        for w in range(1,img.shape[1]-1):
            T = np.dot(M,[[h-img.shape[0]//2],[w-img.shape[1]//2],[1]])

            y = int(round(T[0][0]-401))
            x = int(round(T[1][0]-401))
            cornerx.append(x)
            cornery.append(y)
            y_up, y_down = math.ceil(T[0][0] - 401), math.floor(T[0][0] - 401)
            x_up, x_down = math.ceil(T[1][0] - 401), math.floor(T[1][0] - 401)
            board[y_up, x_down], board[y_up, x_up], board[y_down, x_down]= img[h,w],img[h,w],img[h,w]

    board= board.astype(np.uint8)

    cv2.arrowedLine(board, (0,400), (800,400), 0,  tipLength=0.02)
    cv2.arrowedLine(board, (400,800),(400,0), 0,  tipLength=0.02)
    return board

img = cv2.imread("smile.png", cv2.IMREAD_GRAYSCALE)

M=[[1,0,0],[0,1,0],[0,0,1]]
plane=get_transformed_image(img, M)
alpha=math.cos(5 * math.pi / 180)
beta=math.sin(5 * math.pi / 180)

finish=False
while not finish:
    cv2.imshow("test", plane)
    key=cv2.waitKey(0)
    if key == ord('a'):
        M_a=[[1,0,0],[0,1,-5],[0,0,1]]
        M = np.dot(M_a, M)
    elif key ==ord('d'):
        M_d = [[1, 0, 0], [0, 1, 5], [0, 0, 1]]
        M = np.dot(M_d, M)
    elif key == ord('w'):
        M_w= [[1, 0, -5], [0, 1, 0], [0, 0, 1]]
        M = np.dot(M_w, M)
    elif key ==ord('s'):
        M_s = [[1, 0, 5], [0, 1, 0], [0, 0, 1]]
        M = np.dot(M_s, M)
    elif key ==ord('r'):
        M_r = [[alpha, -beta, 0],[beta, alpha, 0],[0, 0, 1]]
        M = np.dot(M_r, M)
    elif key ==ord('R'):
        M_r = [[alpha, beta, 0],[-beta, alpha, 0],[0, 0, 1]]
        M = np.dot(M_r, M)
    elif key ==ord('F'):
        M_f = [[-1,0,0],[0,1,0],[0,0,1]]
        M = np.dot(M_f, M)
    elif key ==ord('f'):
        M_f = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
        M = np.dot(M_f, M)
    elif key ==ord('y'):
        M_x = [[0.95,0,0],[0,1,0],[0,0,1]]
        M = np.dot(M_x, M)
    elif key ==ord('Y'):
        M_x = [[1.05,0,0],[0,1,0],[0,0,1]]
        M = np.dot(M_x, M)
    elif key ==ord('x'):
        M_y = [[1, 0, 0], [0, 0.95, 0], [0, 0, 1]]
        M = np.dot(M_y, M)
    elif key ==ord('X'):
        M_y = [[1, 0, 0], [0, 1.05, 0], [0, 0, 1]]
        M = np.dot(M_y, M)
    elif key ==ord('H'):
        M = [[1,0,0],[0,1,0],[0,0,1]]
    elif key ==ord('Q'):
        finish=True
    plane = get_transformed_image(img, M)

