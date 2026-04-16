#Modifed by Prof.Kim
import cv2

def main():
    # 0번 카메라(기본 웹캠) 연결
    cap = cv2.VideoCapture(0)

    # 카메라가 정상적으로 열렸는지 확인
    if not cap.isOpened():
        print("에러: 웹캠을 열 수 없습니다. 카메라 연결을 확인해주세요.")
        return

    print("웹캠이 실행되었습니다. 종료하려면 'q' 키를 누르세요.")

    while True:
        # 카메라에서 프레임(이미지) 읽기
        ret, frame = cap.read()

        # 프레임을 제대로 읽어오지 못한 경우
        if not ret:
            print("에러: 프레임을 수신할 수 없습니다.")
            break

        # 거울처럼 보이게 하려면 좌우 반전 (주석 해제 시 적용)
        # frame = cv2.flip(frame, 1)

        # 읽어온 프레임을 화면에 표시 (창 이름: 'Webcam')
        cv2.imshow('Webcam', frame)

        # 1ms 대기하며 키보드 입력 확인
        # 'q' 키를 누르면 무한 루프 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("웹캠을 종료합니다.")
            break

    # 사용이 끝난 카메라 자원 해제 및 모든 창 닫기
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
